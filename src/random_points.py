import random
from numpy import mean

import math
import matplotlib.pyplot as plt


def random_point(dim):
    return [random.random() for _ in range(dim)]


def distance(point_a, point_b):
    length = len(point_a)
    return math.sqrt(sum((point_a[i] - point_b[i]) ** 2
                         for i in range(length)))


def random_distances(dim, num_pairs):
    return [distance(random_point(dim), random_point(dim))
            for _ in range(num_pairs)]


dimensions = range(1, 101)

avg_distances = []
min_distances = []

random.seed()
for dim in dimensions:
    distances = random_distances(dim, 10000)
    avg_distances.append(mean(distances))
    min_distances.append(min(distances))

plt.plot(dimensions, avg_distances)
plt.plot(dimensions, min_distances)
plt.show()