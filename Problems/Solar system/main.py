planets = ["Mercury\n", "Venus\n", "Earth\n",
           "Mars\n", "Jupiter\n", "Saturn\n",
           "Uranus\n", "Neptune"]

file = open("planets.txt", "w", encoding="utf-8")
file.writelines(planets)
file.close()
