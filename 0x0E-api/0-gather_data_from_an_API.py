#!/usr/bin/python3
"""This script gets information about a given employee's TODO list progress."""

import json
import requests
import sys

if __name__ == "__main__":
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    user = sys.argv[1]

    employee_id = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(user)
    )
    todo_list = requests.get(
        'https://jsonplaceholder.typicode.com/todos/?userId={}'.format(user)
    )
    user_info = json.loads(employee_id.text)
    todo_info = json.loads(todo_list.text)

    EMPLOYEE_NAME = user_info['name']

    for task in todo_info:
        TOTAL_NUMBER_OF_TASKS += 1
        if task['completed']:
            NUMBER_OF_DONE_TASKS += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS)
          )

    for task in todo_info:
        if task['completed']:
            print("\t {}".format(task['title']))
