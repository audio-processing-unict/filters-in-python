from argparse import ArgumentParser
from typing import List

from own.io import read_samples, write_samples


def change_volume(
    original: List[int], factor: float
) -> List[int]:
    return [sample * factor for sample in original]

def main():
    parser = ArgumentParser()
    parser.add_argument("input")
    parser.add_argument("output")
    parser.add_argument("factor", type=float)
    args = parser.parse_args()

    samples, sample_rate = read_samples(args.input)
    volume_changed = change_volume(samples, args.factor)
    write_samples(volume_changed, sample_rate, args.output)

if __name__ == "__main__":
    main()
