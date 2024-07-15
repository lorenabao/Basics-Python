def online_count(users):
    #users = list(users.values())
    users = [i for i, status in enumerate(users) if status == "online"]
    return len(users)

statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
    "Adrian": "online",
    "Sara": "online",
    "Nick": "online",
    "Pedro": "offline",
}

print(online_count(statuses))