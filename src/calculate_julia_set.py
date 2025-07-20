import argparse

from src.julia_set_cython import calculate_julia_set


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='JuliaSet', description='Calculating a Julia set')
    parser.add_argument('-n', '--max_iter', default=300, type=int)
    parser.add_argument('-w', '--width', default=1000, type=int)
    parser.add_argument('-re', '--re', default=-0.62772, type=float)
    parser.add_argument('-im', '--im', default=-0.42193, type=float)
    args = parser.parse_args()
    c = complex(args.re, args.im)
    julia_set = calculate_julia_set(max_iter=args.max_iter, width=args.width, c=c)


