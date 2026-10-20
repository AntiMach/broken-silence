from broken_silence.create import create_broken_silence
from broken_silence.time import Time


def main():
    out_dur = Time.parse(input("Output duration> "))
    min_delay = Time.parse(input("Minimum delay> "))
    max_delay = Time.parse(input("Maximum delay> "))
    img_file = input("Image file> ")
    sounds_glob = input("Sounds (default: sounds/*.mp3)> ") or "sounds/*.mp3"
    out_name = input("Output name> ")

    create_broken_silence(
        out_dur=out_dur,
        min_delay=min_delay,
        max_delay=max_delay,
        img_file=img_file,
        out_name=out_name,
        sounds_glob=sounds_glob,
    )
