import requests

BASE_URL = "http://localhost:5005/webhooks/rest/webhook"

def rasa(message, name):
    url = BASE_URL
    response = requests.post(
        url,
        json={
            "sender": name,
            "message": message
        }
    )
    if response.status_code == 200:
        return response.json()
    else:
        print("Erro ao enviar mensagem para o servidor Rasa.")
        return None
def returnText(message, name):
    response = rasa(message, name)
    return response

while(True):
    a = input("digite: ")
    a= returnText(a,"Alysson")
    print(a)