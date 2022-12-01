#!/usr/bin/python3
"""This script gets information about a given employee's TODO list progress,
and exports as JSON
"""

import json
import requests

if __name__ == "__main__":
    # Request the employee ID.
    employee_id = requests.get(
        'https://jsonplaceholder.typicode.com/users/'
    )
    # Load the information sent back as variables
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
        # Gather the information into a dictionary
        for task in todo_info:
            dictionary = {
                'username': user_info['username'],
                'task': task['title'],
                'completed': task['completed']
            }
            task_list.append(dictionary)
    # Create an array that represents the data to store in the table
        tasks[user_id] = task_list
    # Open the file to write to and write it as JSON
        with open('todo_all_employees.json', 'w', encoding='UTF8',
              newline='') as outfile:
            outfile.write(json.dumps(tasks))
