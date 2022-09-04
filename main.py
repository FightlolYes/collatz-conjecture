import matplotlib.pyplot as plt
import numpy as np
import pandas 

from pathlib import Path

cwd = Path(__file__).parents[0]
cwd = str(cwd)
print(f"{cwd}\n---")

def length(list):
    count = 0
    for element in list:
        count += 1
    return count

no = int(input("Enter a number: "))

graph = [no]

while no != 1:
    if no%2 == 0:
        no = no/2
        graph.append(int(no))

    else:
        no = (no * 3) + 1
        graph.append(int(no))

    print(int(no))

print(graph)

x = range(1, length(graph)+ 1)
y = graph

plt.plot(x, y)
plt.savefig(cwd+f"/graphs/plot_{str(int(no))}.png")
plt.show()
