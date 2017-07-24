import matplotlib.pyplot as plt
from itertools import islice

def alternate():
    n = 0
    while True:
        yield n
        n = (n + 1) % 2

def pulses(n):
    num = 0
    while num < n:
        yield num
        num += 1

sp = plt.step(list(pulses(9)),
              list(islice(alternate(), 0, 9)))

plt.show()
