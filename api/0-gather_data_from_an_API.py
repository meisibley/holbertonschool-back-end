#!/usr/bin/python3
'''Write a Python script that, using this REST API,
for a given employee ID, returns information
about his/her TODO list progress.
'''
import requests
from sys import argv


def gather_data_fr_api(employee_id):
    '''accept employee ID, and display the employee TODO list'''
    name = ''
    task_list = []
    counter = 0
    site_str = 'https://jsonplaceholder.typicode.com/users/'
    user_str = site_str + '{}'.format(employee_id)
    todo_str = site_str + '{}/todos'.format(employee_id)

    usersRes = requests.get(user_str)
    todosRes = requests.get(todo_str)

    name = usersRes.json().get('name')

    todosJson = todosRes.json()

    for task in todosJson:
        if task.get('completed') is True:
            counter += 1
            task_list.append(task.get('title'))

    print('Employee {} is done with tasks({}/{}):'
          .format(name, counter, len(todosJson)))

    for t in task_list:
        print('\t {}'.format(t))
    return

if __name__ == "__main__":
    gather_data_fr_api(sys.argv[1])
