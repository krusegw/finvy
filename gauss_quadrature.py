import numpy as np
import sys
import datetime
import math
import csv

def f(x):
    return x**5 - 5*x**4 + 10*x**3 - 10*x**2 + 5*x - 1

def composite_gauss_quadrature(f, a, b, n_intervals, n_points):
    # 获取高斯-勒让德节点和权重
    nodes, weights = np.polynomial.legendre.leggauss(n_points)
    h = (b - a) / n_intervals
    total = 0.0
    for i in range(n_intervals):
        sub_a = a + i * h
        sub_b = sub_a + h
        # 将节点从 [-1, 1] 映射到当前子区间 [sub_a, sub_b]
        transformed_nodes = 0.5 * (sub_b - sub_a) * nodes + 0.5 * (sub_b + sub_a)
        total += 0.5 * (sub_b - sub_a) * np.sum(weights * f(transformed_nodes))
    return total


def write_to_csv(data,n_points):
    with open('output{}.csv'.format(n_points + 3), mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

def main(n_samples,k):
    start_time = datetime.datetime.now()
    area = composite_gauss_quadrature(f,0,5,n_samples,k)
    end_time = datetime.datetime.now()
    elapsed_time = (end_time - start_time).total_seconds()
    size_of_float = np.dtype(np.float64).itemsize
    memory_required = 3 * n_samples * size_of_float / (1024**3)
    error = abs(area-682.5)/(682.5)
    write_to_csv([n_samples, area, memory_required, elapsed_time, error],k)

if __name__ == '__main__':
    n_samples,k = int(sys.argv[1]),int(sys.argv[2])
    main(n_samples,k)
