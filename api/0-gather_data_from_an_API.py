#!/usr/bin/python3
'''Write a Python script that, using this REST API,
for a given employee ID, returns information
about his/her TODO list progress.
'''
import requests
from sys import argv


def gather_data_fr_API(employee_id):
    '''accept employee ID, and display the employee TODO list'''
    url = 'https://jsonplaceholder.typicode.com'
    employee_url = f"{url}/users/{employee_id}"
    todo_url = f"{url}/users/{employee_id}/todos"

    employee_requ = requests.get(employee_url)
    todo_requ = requests.get(todo_url)
    employee_data = employee_requ.json()
    todo_data = todo_requ.json()

    e_name = employee_data.get("name")
    finished_tasks = [task["title"] for task in todo_data if task["completed"]]
    done_tasks = len(finished_tasks)
    total_tasks = len(todo_data)

    print("Employee {} is done with tasks({}/{}):"
          .format(e_name, done_tasks, total_tasks))
    for t in finished_tasks:
        print(f"\t {t}")


if __name__ == "__main__":
    emplye_id = int(sys.argv[1])
    gather_data_fr_API(emplye_id)
