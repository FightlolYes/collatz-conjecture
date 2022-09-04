import matplotlib.pyplot as plt
import numpy as np
import pandas

no = int(input("Enter a number: "))

while no != 1:
    if no % 2 == 0:
        no = no/2

    else:
        no = (no * 3) + 1

    print(int(no))

x=  [1, 2, 3]
y = [1, 4, 9]

plt.plot(x, y)
plt.show()