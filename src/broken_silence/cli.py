from argparse import ArgumentParser

from broken_silence.create import create_broken_silence
from broken_silence.time import Time


def main():
    parser = ArgumentParser("uv run cli")

    parser.add_argument("out_dur", help="Output duration in hh:mm:ss format")
    parser.add_argument("min_delay", help="Minimum delay in hh:mm:ss format")
    parser.add_argument("max_delay", help="Maximum delay in hh:mm:ss format")
    parser.add_argument("img_file", help="File path of the image to be displayed for the entire video")
    parser.add_argument("out_name", help="Output file name")
    parser.add_argument(
        "-s",
        "--sounds-glob",
        help="Glob pattern used to collect all sound effects for the video (default: sounds/*.mp3)",
        default="sounds/*.mp3",
    )

    args = parser.parse_args()

    create_broken_silence(
        out_dur=Time.parse(args.out_dur),
        min_delay=Time.parse(args.min_delay),
        max_delay=Time.parse(args.max_delay),
        img_file=args.img_file,
        out_name=args.out_name,
        sounds_glob=args.sounds_glob,
    )
