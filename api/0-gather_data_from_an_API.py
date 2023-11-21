#!/usr/bin/python3
'''Write a Python script that, using this REST API,
for a given employee ID, returns information
about his/her TODO list progress.
'''
import requests


def gather_data_fr_API(employee_id):
    '''accept employee ID, and display the employee TODO list'''
    url = 'https://jsonplaceholder.typicode.com'
    employee_url = f"{url}/users/{employee_id}"
    todo_url = f"{url}/users/{employee_id}/todos"

    employee_data = requests.get(employee_url).json()
    todo_data = requests.get(todo_url).json()

    employee_name = employee_data.get("name")
    finished_tasks = [task["title"] for task in todo_data if task["completed"]]
    done_tasks = len(finished_tasks)
    total_tasks = len(todo_data)

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, done_tasks, total_tasks))
    for t in finished_tasks:
        print(f"\t {t}")


if __name__ == "__main__":
    from sys import argv

    gather_data_fr_API(int(sys.argv[1]))
