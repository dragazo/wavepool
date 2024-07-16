import numpy as np
import argparse
import sys
import matplotlib.pyplot as plt
from scipy import signal

def sqr(t):
    s = np.sin(t)
    return np.abs(s)**1e-10 * np.sign(s)
def wno(t):
    return np.random.random(t.shape)
sin = np.sin
cos = np.cos
abs = np.abs

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--seed', '-s', type = int, required = False)
    parser.add_argument('--frequency', '-f', type = float, default = 8000)
    parser.add_argument('--duration', '-d', type = float, default = 1.0)
    args = parser.parse_args()

    if args.seed is not None:
        np.random.seed(args.seed)

    t = np.linspace(0, args.duration, round(args.frequency * args.duration))
    s = t * 0

    for line in sys.stdin:
        line = line.strip()
        if line == '': continue

        s += eval(f'lambda t: {line}')(t)

    f, t, Sxx = signal.spectrogram(s, args.frequency)
    plt.pcolormesh(t, f, Sxx, shading = 'gouraud')
    plt.show()
