#!/usr/bin/python3
'''using task0, extend python script to export
data in the JSON format
'''
import json
import requests
import sys


def export_data_to_json(employee_id):
    '''records all tasks owned by this employee'''
    # set variables
    userName = ''
    u_dict = {}
    site_str = 'https://jsonplaceholder.typicode.com/users/'
    user_str = site_str + '{}'.format(employee_id)
    todo_str = site_str + '{}/todos'.format(employee_id)

    # get user and todo requests
    user_res = requests.get(user_str)
    todo_res = requests.get(todo_str)

    # from requests get json
    userName = user_res.json().get('username')
    todosJson = todo_res.json()

    u_dict[employee_id] = []

    # get user dictory
    for task in todosJson:
        task_dict = {}
        task_dict['task'] = task.get('title')
        task_dict['username'] = userName
        task_dict['completed'] task.get('completed')

        u_dict[employee_id].append(task_dict)

    # open and write JSON file
    with open('{}.json'.format(employee_id), 'w') as jsonFile:
        json.dump(u_dict, jsonFile)

    return

if __name__ == '__main__':
    export_data_to_json(sys.argv[1])
