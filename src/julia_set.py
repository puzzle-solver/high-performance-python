import argparse


def create_grid(re_start: float = -1.8, re_end: float = 1.8, im_start: float = -1.8, im_end: float = 1.8, width: int = 30):
    delta_re = (re_end - re_start) / width
    delta_im = (im_end - im_start) / width
    zs = list()
    im = im_start
    while im <= im_end:
        row = list()
        real = re_start
        while real < re_end:
            row.append(complex(real, im))
            real += delta_re
        zs.append(row)
        im += delta_im
    return zs


def calculate_julia(z: complex, c: complex, max_iter: int = 300):
    n = 0
    while abs(z) < 2 and n < max_iter:
        n += 1
        z = z*z + c
    return n


def calculate_julia_set(max_iter: int, width: int = 100, c: complex = -0.62772 - 0.42193j):
    grid = create_grid(width=width)
    output = [[None for _ in row] for row in grid]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            z = grid[i][j]
            output[i][j] = calculate_julia(z, c, max_iter=max_iter)
    return output

