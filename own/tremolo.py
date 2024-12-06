from argparse import ArgumentParser
from typing import List

from own.io import read_samples, write_samples
from own.sine import generate_sine_wave


def apply_tremolo(
    original: List[int], frequency: int, depth: float, sample_rate: int
) -> List[int]:
    num_samples = len(original)
    sine_wave = generate_sine_wave(
        frequency / 2.0, num_samples / sample_rate, depth, sample_rate
    )

    return [
        original_value * (1.0 - depth + sine_value)
        for (original_value, sine_value) in zip(original, sine_wave)
    ]


def main():
    parser = ArgumentParser()
    parser.add_argument("input")
    parser.add_argument("output")
    parser.add_argument("frequency", type=int)
    parser.add_argument("depth", type=float)
    args = parser.parse_args()

    samples, sample_rate = read_samples(args.input)
    tremoloed = apply_tremolo(samples, args.frequency, args.depth, sample_rate)
    write_samples(tremoloed, sample_rate, args.output)


if __name__ == "__main__":
    main()
