#!/usr/bin/python3
"""This script gets information about a given employee's TODO list progress."""

import csv
import json
import requests
import sys

if __name__ == "__main__":
    # Initialize tasks and grab username
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    user = sys.argv[1]
    # Request the employee ID, then their todo list.
    employee_id = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(user)
    )
    todo_list = requests.get(
        'https://jsonplaceholder.typicode.com/todos/?userId={}'.format(user)
    )
    # Load the information sent back as variables
    user_info = json.loads(employee_id.text)
    todo_info = json.loads(todo_list.text)

    task_list = []
    # Grab the employee's name from your new dictionary
    USERNAME = user_info['username']
    # Gather the information into a dictionary
    for task in todo_info:
        data2csv = {
            'USER_ID': user,
            'USERNAME': USERNAME,
            'TASK_COMPLETED_STATUS': task['completed'],
            'TASK_TITLE': task['title']
        }
        task_list.append(data2csv)
    # Create an array that represents the data to store in the table
    fields = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
    # Open the file to write to
    with open('./{}.csv'.format(USER_ID), 'w', encoding='UTF8',
              newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames,
                                quoting=csv.QUOTE_ALL, quotechar='"')
        writer.writerows(task_list)
