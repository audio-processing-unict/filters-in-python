from argparse import ArgumentParser
from ffmpeg import FFmpeg


def tremolo_filter_string(frequency: int, depth: float) -> str:
    return f"tremolo=f={frequency}:d={depth}"


def main():
    parser = ArgumentParser()
    parser.add_argument("input")
    parser.add_argument("output")
    parser.add_argument("frequency", type=int)
    parser.add_argument("depth", type=float)
    args = parser.parse_args()

    ffmpeg = (
        FFmpeg()
        .option("y")
        .input(args.input)
        .output(
            args.output, af=tremolo_filter_string(args.frequency, args.depth)
        )
    )

    ffmpeg.execute()


if __name__ == "__main__":
    main()
