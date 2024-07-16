import argparse
import random

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--seed', '-s', type = int, required = False)
    parser.add_argument('--number', '-n', type = int, required = True)
    parser.add_argument('--min-frequency', '-f', type = float, default = 100.0)
    parser.add_argument('--max-frequency', '-F', type = float, default = 12000.0)
    parser.add_argument('--min-offset', '-o', type = float, default = 0.0)
    parser.add_argument('--max-offset', '-O', type = float, default = 0.5)
    parser.add_argument('--min-amp', '-a', type = float, default = 0.0)
    parser.add_argument('--max-amp', '-A', type = float, default = 1.0)
    args = parser.parse_args()

    if args.seed is not None:
        random.seed(args.seed)

    for i in range(args.number):
        freq = args.min_frequency + random.random() * (args.max_frequency - args.min_frequency)
        offset = args.min_offset + random.random() * (args.max_offset - args.min_offset)
        amp = args.min_amp + random.random() * (args.max_amp - args.min_amp)
        print(random.choice([
            f'{amp} * sin({freq} * (t + {offset}))',
            f'{amp} * sin({freq} * (t + {offset})**2)',
            f'{amp} * sin({freq} * (t + {offset} + 1)**-2)',
            f'{amp} * sqr({freq} * (t + {offset}))',
            f'{amp} * wno(t)',
        ]))
