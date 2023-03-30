import requests

def test_add():
    body = {"title":"generated","completed":False}
    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
    response_body = response.json()
    
    assert response.status_code == 201
    assert response_body['completed'] == False


def test_create_1():
    body = {"title":"generated123"}
    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
    response_body = response.json()

    assert response_body['title'] == body['title']
    assert response_body['completed'] == False


def test_create_2():
    body = {"title":"generated", "completed":False}
    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
    response_body = response.json()

    assert response_body['title'] == body['title']
    assert response_body['completed'] == body['completed']
