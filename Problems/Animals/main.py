file = open("animals.txt", "r", encoding="utf-8")
new_file = open("animals_new.txt", "w", encoding="utf-8")

new_file.write(file.read().replace("\n", " ").rstrip())

file.close()
new_file.close()
