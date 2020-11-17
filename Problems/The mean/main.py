current_entry = -1
total = 0
quantity = 0

while current_entry != '.':
    current_entry = input()
    try:
        number = int(current_entry)
        total += number
        quantity += 1
    except ValueError:
        pass

average = total / quantity
print(average)
