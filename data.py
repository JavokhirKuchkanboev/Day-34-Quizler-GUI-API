import requests
def question_data():
    responce = requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean")
    responce.raise_for_status()

    data = responce.json()

    return data["results"]
    

