from argparse import ArgumentParser

from broken_silence.create import create_broken_silence
from broken_silence.time import Time


def main():
    parser = ArgumentParser()

    parser.add_argument("out_dur", help="Output duration in hh:mm:ss format")
    parser.add_argument("min_delay", help="Minimum delay in hh:mm:ss format")
    parser.add_argument("max_delay", help="Maximum delay in hh:mm:ss format")
    parser.add_argument("img_file", help="File path of the image to be displayed for the entire video")
    parser.add_argument("out_name", help="Output file name")
    parser.add_argument(
        "-s",
        "--sounds-glob",
        help="Glob pattern used to collect all sound effects for the video",
        default="sounds/*.mp3",
    )

    args = parser.parse_args()

    with open(f"{args.out_name}.txt", "w") as log:
        print("Output duration:", args.out_dur, file=log)
        print("Minimum delay:", args.min_delay, file=log)
        print("Maximum delay:", args.max_delay, file=log)
        print("Image:", args.img_file, file=log)
        print("Sounds:", args.sounds_glob, file=log)
        print(file=log)

        create_broken_silence(
            out_dur=Time.parse(args.out_dur),
            min_delay=Time.parse(args.min_delay),
            max_delay=Time.parse(args.max_delay),
            img_file=args.img_file,
            out_name=args.out_name,
            sounds_glob=args.sounds_glob,
            log_buffer=log,
        )
