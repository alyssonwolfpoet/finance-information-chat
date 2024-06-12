import requests
import streamlit as st

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
        st.error("Erro ao enviar mensagem para o servidor Rasa.")
        return None

def returnText(message, name):
    response = rasa(message, name)
    if response:
        texto = response[0]['text']
        return texto
    else:
        return "Desculpe, não consegui obter uma resposta no momento."

def ui():
    st.title("finance information chat")
    st.write("Bem vindo! Diga em que podemos ajudar 🕵️‍♂️")

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # React to user input
    if prompt := st.chat_input("Digite aqui"):
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Get bot response
        response = returnText(prompt, "alysson")

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(f"financito bot: {response}")
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": f"financito bot: {response}"})

ui()