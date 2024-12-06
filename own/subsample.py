from argparse import ArgumentParser
from typing import List

from own.io import read_samples, write_samples


def resample(original: List[int], original_rate: int, target_rate: int) -> List[int]:
    original_num_samples = len(original)
    ratio = target_rate / original_rate
    target_num_samples = int(original_num_samples * ratio)
    output = [0] * target_num_samples

    for output_index in range(0, target_num_samples):
        original_sample_index = round(output_index / ratio)
        output[output_index] = original[original_sample_index]

    return output


def main():
    parser = ArgumentParser()
    parser.add_argument("input")
    parser.add_argument("output")
    parser.add_argument("rate", type=int)
    args = parser.parse_args()

    samples, sample_rate = read_samples(args.input)
    subsampled = resample(samples, sample_rate, args.rate)
    write_samples(subsampled, args.rate, args.output)


if __name__ == "__main__":
    main()
