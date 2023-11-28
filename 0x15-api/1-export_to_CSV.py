#!/usr/bin/python3
"""
export user todos
"""


if __name__ == "__main__":
    import requests
    import sys
    import csv

    userId = int(sys.argv[1])
    user_res = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                            .format(userId))

    user = user_res.json()
    name = user.get('name')

    todos = requests.get('https://jsonplaceholder.typicode.com/todos')

    filename = "{}.csv".format(userId)
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=',', quoting=csv.QUOTE_ALL)
        for task in todos.json():
            if task.get('userId') == userId:
                row = [userId,
                       user.get('username'),
                       task.get('completed'),
                       task.get('title')]
                writer.writerow(row)
