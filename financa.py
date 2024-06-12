import requests
import streamlit as st

BASE_URL = "http://localhost:5005/webhooks/rest/webhook"

def rasa(messege,name):
    url = BASE_URL
    response = requests.post(
        url,
        json=
            {
                "sender": "{name}",
                "message": "{messege}" 
            }
    )
    if response.status_code ==200:
        return response.json()
    else:
        return None

def returnText(messege):
    response = rasa(messege,"alysson")
    print(response)
    texto = response[0]['text']
    print(texto)
    return texto
    
def ui():
    st.title("finance information chat")
    st.write("Bem vindo! diga em que podemos ajudar🕵️‍♂️")

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


    response = f"financito bot: {returnText(prompt)}"
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

ui()