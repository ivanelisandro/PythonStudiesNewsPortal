file = open("sums.txt", "r")

for line in file:
    numbers = [int(number) for number in line.split(" ")]
    total = 0
    for number in numbers:
        total += number

    print(total)

file.close()
