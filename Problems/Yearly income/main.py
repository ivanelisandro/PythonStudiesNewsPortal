with open("salary.txt") as monthly,\
        open("salary_year.txt", "w") as yearly:
    for line in monthly:
        yearly.write(str(int(line) * 12) + "\n")
