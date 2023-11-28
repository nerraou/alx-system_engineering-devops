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


def find_user_by_id(users, userId):
    """find user by id"""
    for user in users:
        if user.get("id") == userId:
            return user
    return None


if __name__ == "__main__":
    import requests
    import json

    users_res = requests.get("https://jsonplaceholder.typicode.com/users")
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')

    users = users_res.json()
    todos = todos.json()

    filename = "todo_all_employees.json"
    with open(filename, 'w', newline='') as file:
        data = {}

        for todo in todos:
            userId = todo.get("userId")
            if userId in data:
                username = data[userId][0]["username"]
                data[userId].append(create_todo(todo, username))
            else:
                username = find_user_by_id(users, userId).get("username")
                data[userId] = [create_todo(todo, username)]

        json.dump(data, file)
