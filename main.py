import streamlit as st
import requests

# Função para enviar requisição para o servidor Rasa
def send_message(message):
    url = 'http://localhost:5005/webhooks/rest/webhook'  # URL do servidor Rasa
    payload = {'sender': 'user', 'message': message}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

# Função para processar e exibir a resposta do Rasa
def handle_response(response):
    for r in response:
        if 'text' in r:
            st.text(r['text'])
            if 'buttons' in r:
                for button in r['buttons']:
                    if 'title' in button and 'payload' in button:
                        st.button(button['title'], key=button['title'], on_click=lambda payload=button['payload']: send_message(payload))
        elif 'image' in r:
            st.image(r['image'])

# Interface Streamlit
def main():
    st.title('Chatbot com Rasa')

    message = st.text_input('Digite sua mensagem:')
    if st.button('Enviar'):
        if message:
            response = send_message(message)
            handle_response(response)

if __name__ == '__main__':
    main()