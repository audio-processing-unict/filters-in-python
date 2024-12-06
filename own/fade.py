import copy
from argparse import ArgumentParser
from typing import List

from own.io import read_samples, write_samples


def apply_fade(
    original: List[int], fade_type: str, start_sample: int, num_samples: int
) -> List[int]:
    if fade_type not in ["in", "out"]:
        print(f"Unknown fade type {fade_type}")
        return

    output = copy.deepcopy(original)

    for i in range(0, num_samples):
        value = output[start_sample + i]
        progress = i / num_samples

        if fade_type == "in":
            new_value = progress * value
        elif fade_type == "out":
            new_value = (1.0 - progress) * value

        output[start_sample + i] = new_value

    return output


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

    samples, sample_rate = read_samples(args.input)
    processed_samples = samples
    for fade_type, start_sample, num_samples in zip(
        args.type, args.start_sample, args.num_samples
    ):
        print(
            f"Applying fade-{fade_type} from sample {start_sample} for {num_samples} samples"
        )
        processed_samples = apply_fade(
            processed_samples, fade_type, start_sample, num_samples
        )

    write_samples(processed_samples, sample_rate, args.output)


if __name__ == "__main__":
    main()
