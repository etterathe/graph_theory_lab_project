def euclidean(a, b):
    return sum((x - y) ** 2 for x, y in zip(a, b)) ** 0.5

def manhattan(a, b):
    return sum(abs(x - y) for x, y in zip(a, b))

def maximum(a, b):
    return max(abs(x - y) for x, y in zip(a, b))