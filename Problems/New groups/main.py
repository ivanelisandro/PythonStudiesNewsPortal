# the list with classes; please, do not modify it
groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']

number_groups = int(input())
kids_by_group = {}

for group in groups:
    if number_groups > 0:
        kids_by_group[group] = int(input())
        number_groups -= 1
    else:
        kids_by_group[group] = None

print(kids_by_group)
