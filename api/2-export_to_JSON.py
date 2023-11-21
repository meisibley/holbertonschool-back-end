#!/usr/bin/python3
'''using task0 to export data into JSON format'''
import json
import requests
import sys


def export_data_to_json(employee_id):
    '''records all tasks owned by this employee'''
    userName = ''
    u_dict = {}
    site_str = 'https://jsonplaceholder.typicode.com/users/'
    user_str = site_str + '{}'.format(employee_id)
    todo_str = site_str + '{}/todos'.format(employee_id)

    user_res = requests.get(user_str)
    todo_res = requests.get(todo_str)

    userName = user_res.json().get('username')
    todosJson = todo_res.json()

    u_dict[employee_id] = []

    for task in todosJson:
        task_dict = {}
        task_dict['task'] = task.get('title')
        task_dict['username'] = userName
        task_dict['completed'] task.get('completed')

        u_dict[employee_id].append(task_dict)

    with open('{}.json'.format(employee_id), 'w') as jsonFile:
        json.dump(u_dict, jsonFile)

    return

if __name__ == '__main__':
    export_data_to_json(sys.argv[1])