import requests

def test_add_change_get():
    body = {"title": "My task","completed": False}
    response = requests.post("https://todo-app-sky.herokuapp.com/", json = body)
    id = response.json()["id"]

    body = {"completed": True}
    path = "https://todo-app-sky.herokuapp.com/{id}".format(id = id)

    requests.patch(path, json = body)

    response = requests.get(path.format(id = id))

    assert response.json()['completed'] == True