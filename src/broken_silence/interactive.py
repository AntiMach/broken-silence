from broken_silence.create import create_broken_silence
from broken_silence.time import Time


def main():
    out_dur = input("Output duration> ")
    min_delay = input("Minimum delay> ")
    max_delay = input("Maximum delay> ")
    img_file = input("Image file> ")
    sounds_glob = input("Sounds (default: sounds/*.mp3)> ") or "sounds/*.mp3"
    out_name = input("Output name> ")

    with open(f"{out_name}.txt", "w") as log:
        print("Output duration:", out_dur, file=log)
        print("Minimum delay:", min_delay, file=log)
        print("Maximum delay:", max_delay, file=log)
        print("Image:", img_file, file=log)
        print("Sounds:", sounds_glob, file=log)
        print(file=log)

        create_broken_silence(
            out_dur=Time.parse(out_dur),
            min_delay=Time.parse(min_delay),
            max_delay=Time.parse(max_delay),
            img_file=img_file,
            out_name=out_name,
            sounds_glob=sounds_glob,
            log_buffer=log,
        )
