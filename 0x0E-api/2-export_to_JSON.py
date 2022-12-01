#!/usr/bin/python3
"""This script gets information about a given employee's TODO list progress."""

import json
import requests
import sys

if __name__ == "__main__":
    # Initialize tasks and grab username
    USER_ID = sys.argv[1]
    # Request the employee ID, then their todo list.
    employee_id = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(USER_ID)
    )
    todo_list = requests.get(
        'https://jsonplaceholder.typicode.com/todos/?userId={}'.format(USER_ID)
    )
    # Load the information sent back as variables
    user_info = json.loads(employee_id.text)
    todo_info = json.loads(todo_list.text)

    tasks = {}
    task_list = []
    # Gather the information into a dictionary
    for task in todo_info:
        dictionary = {
            'task': task['title'],
            'completed': task['completed'],
            'username': user_info['username']
        }
        task_list.append(dictionary)
    # Create an array that represents the data to store in the table
    tasks[USER_ID] = task_list
    # Open the file to write to and write it as JSON
    with open('./{}.json'.format(USER_ID), 'w', encoding='UTF8',
              newline='') as outfile:
        outfile.write(json.dumps(tasks))
