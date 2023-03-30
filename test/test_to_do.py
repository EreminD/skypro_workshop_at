import requests


def test_delete():
    body = {"title":"generated","completed":False}
    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
    id = response.json()["id"]
    
    requests.delete('https://todo-app-sky.herokuapp.com/'+str(id))

    new_response = requests.get("https://todo-app-sky.herokuapp.com/"+str(id))
    assert new_response.status_code == 404