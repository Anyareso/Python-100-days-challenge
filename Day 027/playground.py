def add(*args):
    som = 0
    for n in args:
        som += n
    return som


print(add(3, 5, 6))
