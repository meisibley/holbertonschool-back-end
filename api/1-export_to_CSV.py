#!/usr/bin/python3
'''using task0 to export data into CSV format'''
import requests
import sys
import csv


def export_data_to_csv(employee_id):
    '''records all tasks owned by this employee'''
    userName = ''
    ttl_tasks = []
    site_str = 'https://jsonplaceholder.typicode.com/users/'
    user_str = site_str + '{}'.format(employee_id)
    todo_str = site_str + '{}/todos'.format(employee_id)

    user_res = requests.get(user_str)
    todo_res = requests.get(todo_str)

    userName = user_res.json().get('username')
    todosJson = todo_res.json()

    for tasks in todosJson:
        task_rows = [employee_id]
        task_rows.append(userName)
        task_rows.append(tasks.get('completed'))
        task_rows.append(tasks.get('title'))

        ttl_tasks.append(task_rows)

    with open('{}.csv'.format(employee_id), 'w') as csvFile:
        csvwriter = csv.writer(csvFile, quoting=csv.QUOTE_ALL)
        csvwriter.writerows(ttl_tasks)

    return

if __name__ == '__main__':
    export_data_to_csv(sys.argv[1])
