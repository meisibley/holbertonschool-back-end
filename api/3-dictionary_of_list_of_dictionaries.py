#!/usr/bin/python3
'''using task0, extend python script to export
data in the JSON format
'''
import json
import requests


def export_all_data_to_json(employee_id):
    '''records all tasks from all employees'''
    # set variables
    users_and_tasks = {}
    site_str = 'https://jsonplaceholder.typicode.com/users/'
    user_str = site_str + 'users'
    todo_str = site_str + 'todos'

    userJson = requests.get(user_str).json()
    todoJson = requests.get(todo_str).json()

    user_data = {}

    for user in userJson:
        user_data[user['id']] = user['username']

    for task in todoJson:
        if users_and_tasks.get(task['userId'], False) is False:
            users_and_tasks[task['userId']] = []
        task_dict = {}
        task_dict['task'] = task['title']
        task_dict['username'] = user_data[tasks['userId']]
        task_dict['completed'] = task['completed']
        users_and_tasks[task['userId']].append(task_dict)

    with open('todo_all_employees.json', 'w') as jsonFile:
        json.dump(users_and_tasks, jsonFile)

    return

if __name__ == '__main__':
    export_all_data_to_json()
