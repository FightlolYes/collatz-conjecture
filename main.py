no = int(input("Enter a number: "))

while no != 1:
    if no % 2 == 0:
        no = no/2

    else:
        no = (no * 3) + 1

    print(int(no))