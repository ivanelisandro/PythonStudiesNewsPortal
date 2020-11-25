with open("users.json") as users_file:
    objects = json.load(users_file)
    print(len(objects["users"]))
