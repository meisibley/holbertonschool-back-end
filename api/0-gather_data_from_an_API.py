#!/usr/bin/python3
'''Write a Python script that, using this REST API,
for a given employee ID, returns information
about his/her TODO list progress.
'''
import requests
from sys import argv


def get_employee_tasks(employee_id):
    """returns info about his/her TODO list progress with given employee ID"""
    # set up vars
    name = ''
    task_list = []
    completed_counter = 0
    site_string = 'https://jsonplaceholder.typicode.com/users/'
    ustr = site_string + '{}'.format(employee_id)
    tstr = site_string + '{}/todos'.format(employee_id)

    # get requests
    usersRes = requests.get(ustr)
    todosRes = requests.get(tstr)

    # get json from requests
    name = usersRes.json().get('name')

    todosJson = todosRes.json()

    for tasks in todosJson:
        if tasks.get('completed') is True:
            completed_counter += 1
            task_list.append(tasks.get('title'))

    print('Employee {} is done with tasks({}/{}):'
          .format(name, completed_counter, len(todosJson)))

    for ttl in task_list:
        print('\t {}'.format(ttl))
    return

if __name__ == "__main__":
    get_employee_tasks(sys.argv[1])
