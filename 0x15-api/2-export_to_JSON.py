#!/usr/bin/python3
"""
export user todos to json
"""


def create_todo(todo, username):
    """
    create todo object
    """
    return {
        "task": todo.get("title"),
        "completed": todo.get("completed"),
        "username": username
    }


def predicate(todo, userId):
    """is user owner of todo"""
    return todo.get("userId") == userId


if __name__ == "__main__":
    import requests
    import sys
    import json

    userId = int(sys.argv[1])
    user_res = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                            .format(userId))

    user = user_res.json()
    name = user.get('name')
    username = user.get('username')

    todos = requests.get('https://jsonplaceholder.typicode.com/todos')

    filename = "{}.json".format(userId)
    with open(filename, 'w', newline='') as file:
        filtred_todos = filter(lambda x: predicate(x, userId), todos.json())
        tasks = map(lambda todo: create_todo(todo, username), filtred_todos)
        data = {}
        data[userId] = list(tasks)
        json.dump(data, file)
