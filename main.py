import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()
email = os.getenv('EMAIL')
password = os.getenv('PASSWORD')

base_url = "https://api-tasks.cosasdedevs.com/v1/"

# CREATE USER
def create_user():
    url = base_url + "users"

    #USER DATA
    user = {
        'username': 'luc_test',
        'email': 'lucianno@myemail.com',
        'password': 'user123',
    }

    #HEADERS FORM
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    #REQUESTS
    response = requests.request("POST", url, headers=headers, data=user)
    print_response(response)

#LOGIN
def login():
    url = base_url + "login"

    auth = {
        'email': email,
        'password': password
    }

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.request("POST", url, headers=headers, data=auth)
    if(response.status_code == 200):
        return response.json()['data']['token']
    raise Exception(response.json()['error'])

#GET TASK
def get_task_by_id(id):
    url = base_url + f"tasks/{id}"

    headers = {
        'Authorization': login()
    }

    response = requests.request("GET", url, headers=headers)

    print_response(response)

#CREATE TASK
def create_task():
    url = base_url + "tasks"

    data = {
        "title": "New Task"
    }
    payload = json.dumps(data) #CONVERT DATA TO JSON

    headers = {
        'Authorization': login(),
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print_response(response)

#UPDATE TASK
def update_task(id):
    url = base_url + f"tasks/{id}"

    data = {
        "title": "Task update"
    }
    payload = json.dumps(data) #CONVERT DATA TO JSON

    headers = {
        'Authorization': login(),
        'Content-Type': 'application/json'
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

    print_response(response)

#DELETE TASK
def delete_task(id):
    url = base_url + f"tasks/{id}"

    headers = {
        'Authorization': login()
    }

    response = requests.request("DELETE", url, headers=headers)

    if(response.status_code == 200):
        return 'Deleted successfully'
    raise Exception(204)

# GET USERS (ADMINISTRATOR)
def get_users():
    url = base_url + "users"

    headers = {
        'Authorization': login()
    }

    response = requests.request("GET", url, headers=headers)
    if(response.status_code == 200):
        return print_response(response)
    raise Exception(403)

# GET USER TASKS (ADMINISTRATOR)
def get_user_tasks(user_id):
    url = base_url + f"users/{user_id}/tasks"
    #Filter by is_done:
    # url = base_url + f"users/{user_id}/tasks?page=2&limit=10&is_done=true" 

    headers = {
        'Authorization': login()
    }

    response = requests.request("GET", url, headers=headers)
    
    print_response(response)

# GET USER TASK (ADMINISTRATOR)
def get_user_task_by_id(user_id, task_id):
    url = base_url + f"users/{user_id}/tasks/{task_id}"

    headers = {
        'Authorization': login()
    }

    response = requests.request("GET", url, headers=headers)
    if(response.status_code == 200):
        return print_response(response)
    raise Exception('This task does not belong to the user')

#REQUEST RESPONSE
def print_response(response):
    print(response.text)
    print(response.json())
    print(response.status_code)
    print(response.headers)

if __name__ == '__main__':
    # create_user()
    # login()
    # get_task_by_id(31)
    # create_task()
    # update_task(31)
    # delete_task(151)
    # get_users()
    # get_user_tasks(1)
    get_user_task_by_id(1, 3)