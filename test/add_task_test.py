import requests


def my_test_add_P():
    body = {"title":"Positive","completed":False}
    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
    id = response.json()["id"]
    
    body = {"order": 0}
    response = requests.patch(f'https://todo-app-sky.herokuapp.com/{id}', json=body)


def my_test_add_N():
    body = {"title":"Negative","completed":False}
    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
    id = response.json()["id"]
    
    body = {"order": -1}
    response = requests.patch(f'https://todo-app-sky.herokuapp.com/{id}', json=body)

def my_test_add_PN():
    body = {"title":"TestSK","completed":False}
    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
    id = response.json()["id"]
    
    



