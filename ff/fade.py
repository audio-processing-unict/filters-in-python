from argparse import ArgumentParser
from ffmpeg import FFmpeg


def fade_filter_string(fade_type: str, start_sample: int, num_samples: int):
    return f"afade=t={fade_type}:ss={start_sample}:ns={num_samples}"


def main():
    parser = ArgumentParser()
    parser.add_argument("input")
    parser.add_argument("output")
    parser.add_argument(
        "-t", "--type", choices=["in", "out"], action="extend", nargs="+"
    )
    parser.add_argument(
        "-ss", "--start_sample", action="extend", type=int, nargs="+"
    )
    parser.add_argument(
        "-ns", "--num_samples", action="extend", type=int, nargs="+"
    )
    args = parser.parse_args()

    print(args)

    af_string = ",".join(
        [
            fade_filter_string(fade_type, start_sample, num_samples)
            for (fade_type, start_sample, num_samples) in zip(
                args.type, args.start_sample, args.num_samples
            )
        ]
    )

    print(f"Applied audio filter option: {af_string}")

    ffmpeg = (
        FFmpeg()
        .option("y")
        .input(args.input)
        .output(
            args.output,
            af=af_string,
        )
    )

    ffmpeg.execute()


if __name__ == "__main__":
    main()
