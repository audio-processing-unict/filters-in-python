from typing import List
import wavfile

def read_samples(path: str):
    wavread = wavfile.open(path, "r")
    samples = wavread.read(None)
    return list(samples), wavread.sample_rate

def write_samples(samples: List[int], rate: int, path: str):
    wavfile.write(path, samples, rate)

