import requests
import streamlit as st

BASE_URL = "http://localhost:5005/webhooks/rest/webhook"

def returnText(message, name):
    response = rasa(message, name)
    if response:
        messages = []
        for r in response:
            if 'text' in r:
                messages.append({"type": "text", "content": r['text']})
            elif 'buttons' in r:
                buttons = []
                for button in r['buttons']:
                    buttons.append(button['title'])
                messages.append({"type": "buttons", "content": buttons})
            elif 'image' in r:
                messages.append({"type": "image", "content": r['image']})
        return messages
    else:
        return [{"type": "text", "content": "Desculpe, não consegui obter uma resposta no momento."}]

def ui():
    st.title("finance information chat")
    st.write("Bem vindo! Diga em que podemos ajudar 🕵️‍♂️")

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        if message["type"] == "text":
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
        elif message["type"] == "buttons":
            st.write(message["content"])  # Renderizando os botões
        elif message["type"] == "image":
            st.image(message["content"])

    # React to user input
    if prompt := st.chat_input("Digite aqui"):
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt, "type": "text"})

        # Get bot response
        response = returnText(prompt, "alysson")

        # Display assistant response in chat message container
        for msg in response:
            if msg["type"] == "text":
                st.session_state.messages.append({"role": "assistant", "content": msg["content"], "type": "text"})
                with st.chat_message("assistant"):
                    st.markdown(f"financito bot: {msg['content']}")
            elif msg["type"] == "image":
                st.session_state.messages.append({"role": "assistant", "content": msg["content"], "type": "image"})
                st.image(msg["content"], caption="Image from bot")

ui()