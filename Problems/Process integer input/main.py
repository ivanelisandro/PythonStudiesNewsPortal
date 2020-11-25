current_input = "1"
numbers_to_print = []

while current_input:
    current_input = input()

    try:
        number = int(current_input)

        if number > 100:
            current_input = ""
        elif number < 10:
            continue
        else:
            numbers_to_print.append(number)
    except ValueError:
        continue

print("\n".join(str(n) for n in numbers_to_print))
