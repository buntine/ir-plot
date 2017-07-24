import sys, re
import matplotlib.pyplot as plt
from itertools import islice

def alternate():
    n = 0
    while True:
        yield n
        n = (n + 1) % 2

def pulses(data):
    i = 0
    total = 0
    while i < len(data):
        yield total
        total += data[i]
        i += 1

data = []

for line in sys.stdin.readlines():
    duration = int(re.sub(r'\D+', '', line))
    data.append(duration)

sp = plt.step(list(pulses(data)),
              list(islice(alternate(), 0, len(data))))

plt.show()
