content = input()

file = open("input.txt", "a", encoding="utf-8")
file.write(content)
file.close()
