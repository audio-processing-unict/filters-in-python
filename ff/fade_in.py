from argparse import ArgumentParser
from ffmpeg import FFmpeg


def main():
    parser = ArgumentParser()
    parser.add_argument("input")
    parser.add_argument("output")
    parser.add_argument("start_sample", type=int)
    parser.add_argument("num_samples", type=int)
    args = parser.parse_args()

    ffmpeg = FFmpeg().option("y").input(args.input).output(args.output, af=f"afade=t=in:ss={args.start_sample}:ns={args.num_samples}")

    ffmpeg.execute()


if __name__ == "__main__":
    main()
