days = int(input())
food_per_day = int(input())
flight_cost = int(input())
night_cost = int(input())

required = (2 * flight_cost) + night_cost * (days - 1) + (food_per_day * days)

print(required)
