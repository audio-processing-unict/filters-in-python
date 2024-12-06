import math
from argparse import ArgumentParser
from typing import List

from own.io import write_samples

def generate_sine_wave(frequency: int, duration=1.0, amplitude=1.0, sample_rate=44100) -> List[float]:
    num_samples = int(duration * sample_rate)
    samples = list()

    for i in range(0, num_samples):
        time = i / sample_rate
        value = amplitude * math.sin(time * frequency * (2 * math.pi))
        samples.append(value)

    return samples

def main():
    parser = ArgumentParser()
    parser.add_argument("-f", "--frequency", type=int, required=True)
    parser.add_argument("-v", "--volume", type=float, default=1.0)
    parser.add_argument("-d", "--duration", type=float, default=1.0)
    parser.add_argument("-sr", "--sample-rate", type=int, default=44100)
    parser.add_argument("output")
    args = parser.parse_args()

    samples = generate_sine_wave(args.frequency, args.duration, args.volume, args.sample_rate)
    write_samples(samples, args.sample_rate, args.output)

if __name__ == "__main__":
    main()
