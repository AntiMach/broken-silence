import glob
import random
from io import TextIOWrapper
from pathlib import Path

import ffmpeg

from broken_silence.sfx import SFX
from broken_silence.time import Time


def create_broken_silence(
    out_dur: float,
    min_delay: float,
    max_delay: float,
    out_name: str,
    img_file: str,
    sounds_glob: str,
):
    with open(f"{out_name}.txt", "w") as logger:
        print("Output duration:", Time.format(out_dur, show_zeros=True), file=logger)
        print("Minimum delay:", Time.format(min_delay, show_zeros=True), file=logger)
        print("Maximum delay:", Time.format(max_delay, show_zeros=True), file=logger)
        print("Image:", img_file, file=logger)
        print("Sounds:", sounds_glob, file=logger)
        print(file=logger)

        _create_broken_silence(
            out_dur,
            min_delay,
            max_delay,
            out_name,
            img_file,
            sounds_glob,
            logger,
        )


def _create_broken_silence(
    out_dur: float,
    min_delay: float,
    max_delay: float,
    out_name: str,
    img_file: str,
    sounds_glob: str,
    logger: TextIOWrapper,
):

    sfxs: list[SFX] = [SFX.from_path(sfx_file) for sfx_file in glob.glob(sounds_glob, recursive=True)]

    res_dur = 0.0
    segments = []
    sfx_bag = [*sfxs]

    while res_dur < out_dur:
        if len(sfx_bag) == 0:
            sfx_bag = [*sfxs]

        sfx = sfx_bag.pop(random.randint(0, len(sfx_bag) - 1))

        if res_dur + sfx.dur < out_dur:
            sfx_path = Path(sfx.file)
            print(f"{Time.format(int(res_dur), True)}) {sfx_path.name}", file=logger)
            res_dur += sfx.dur

        silence_dur = round(random.random() * (max_delay - min_delay) + min_delay, 2)

        if res_dur + silence_dur > out_dur:
            silence_dur = out_dur - res_dur

        res_dur += silence_dur

        silence = ffmpeg.input(f"anullsrc=r=48000:d={silence_dur:.2f}", f="lavfi")
        segments.append(ffmpeg.concat(sfx.stream, silence, v=0, a=1))

    sound = ffmpeg.concat(*segments, v=0, a=1)
    image = ffmpeg.input(img_file)

    image = image.filter("scale", "trunc(iw/2)*2", "trunc(ih/2)*2")
    image = image.filter("loop", "-1", "1")
    image = image.filter("trim", "0", out_dur)
    image = image.filter("setpts", "PTS-STARTPTS")

    output = ffmpeg.output(
        image,
        sound,
        f"{out_name}.mp4",
        movflags="faststart",
        pix_fmt="yuv420p",
        crf=40,
        r=1,
    )
    output.run(overwrite_output=True)
