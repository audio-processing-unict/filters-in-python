import numpy
from typing import List
from scipy.io import wavfile


def read_samples(path: str):
    sample_rate, data = wavfile.read(path)
    return list(data), sample_rate


def write_samples(samples: List[int | float], rate: int, path: str):
    wavfile.write(path, rate, numpy.array(samples))
