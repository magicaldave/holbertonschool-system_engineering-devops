#!/usr/bin/python3
"""This script gets information about a given employee's TODO list progress,
and exports as JSON
"""

import json
import requests

if __name__ == "__main__":
    employee_id = requests.get(
        'https://jsonplaceholder.typicode.com/users/'
    )
    user_info = json.loads(employee_id.text)

    tasks = {}
    for user in user_info:
        user_id = user['id']
        todo_list = requests.get(
            'https://jsonplaceholder.typicode.com/todos/?userId={}'
            .format(user_id)
        )
        todo_info = json.loads(todo_list.text)

        task_list = []
        for task in todo_info:
            dictionary = {
                'username': user['username'],
                'task': task['title'],
                'completed': task['completed']
            }
            task_list.append(dictionary)

        tasks[user_id] = task_list

        with open('todo_all_employees.json', 'w', encoding='UTF8',
                  newline='') as f:
            f.write(json.dumps(tasks))
