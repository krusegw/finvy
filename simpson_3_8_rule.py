import numpy as np
import sys
import datetime
import math
import csv

def f(x):
    return 10*np.sqrt(1 - (x**2) / 25)


def simpson_3_8_rule(f, a, b, n):
    if n % 3 != 0:
        raise ValueError("n must be a multiple of 3 for Simpson's 3/8 rule.")
    h = (b - a) / n
    total = f(a) + f(b)
    for i in range(1, n):
        xi = a + i * h
        if i % 3 == 0:
            weight = 2
        else:
            weight = 3
        total += weight * f(xi)
    return 3 * h * total / 8

def write_to_csv(data):
    with open('output4.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

def main(n_samples):
    start_time = datetime.datetime.now()
    area = simpson_3_8_rule(f,0,5,n_samples)
    end_time = datetime.datetime.now()
    elapsed_time = (end_time - start_time).total_seconds()
    size_of_float = np.dtype(np.float64).itemsize
    memory_required = 3 * n_samples * size_of_float / (1024**3)
    error = abs(area-12.5*math.pi)/(12.5*math.pi)
    write_to_csv([n_samples, area, memory_required, elapsed_time, error])

if __name__ == '__main__':
    n_samples = int(sys.argv[1])
    main(n_samples)