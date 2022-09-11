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

save_no = no

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

ask = input("Save the graph? Y/N")

plt.title(f"A Collatz Conjecture graph for {save_no}")
plt.xlabel("No of steps")
plt.ylabel("Returned value")

plt.plot(x, y)

if ask == "Y" or "y":
    plt.savefig(cwd+f"/graphs/plot_{str(int(save_no))}.png")

else:
    pass

plt.show()

#test