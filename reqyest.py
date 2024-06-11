import requests

url = "http://localhost:5005/webhooks/rest/webhook"

response = requests.post(
    url,
    json=
        {
            "sender": "Alysson",
            "message": "hello" 
        }
)
print(response.json())