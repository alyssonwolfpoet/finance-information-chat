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
    #print(response)
    if response:
        messages = []
        for r in response:
            if 'text' in r:
                messages.append({"type": "text", "content": r['text']})
            if 'buttons' in r:
                buttons = []
                payloads = []
                #print("so deus sabe")
                #print(r["buttons"])  
                for button in r['buttons']:
                    buttons.append(button['title'])
                #for payload in r['buttons']:
                   #payloads.append(payload['payload'])
                #for i in buttons:
                    #print(i)
                messages.append({"type": "buttons", "content": r['buttons']})
                #messages.append({"type": "payload", "content": payloads})

            if 'image' in r:
                messages.append({"type": "image", "content": r['image']})       
        return messages
    else:
        return [{"type": "text", "content": "Desculpe, não consegui obter uma resposta no momento."}]

# Função para exibir os botões
def display_buttons(buttons):
    print("\n\n",buttons,"\n\n")
    
    for i in buttons:
        #print(i)
        # if st.button(i['title']):
        #      print("bnt if")
        #      #st.write(i['payload'])
        #      response = returnText(i['payload'])
        #      return response

        # if i["title"] == "EUA":
        #     with st.chat_message("user"):
        #         prompt = "EUA"
        #         st.markdown(prompt)
        #         # Add user message to chat history
        #         st.session_state.messages.append({"role": "user", "content": prompt, "type": "text"})

        if st.button(i['title']):
            print(i['title'])
            with st.chat_message("user"):
                prompt = i['title']
                st.markdown(prompt)
                # Add user message to chat history
                st.session_state.messages.append({"role": "user", "content": prompt, "type": "text"})

    
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
        if message["type"] == "buttons":
            #print(message,"messege spacy")
            st.write(message["content"])  # Renderizando os 
        if message["type"] == "image":
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
        print(response,"\n\n")

        # Display assistant response in chat message container
        for msg in response:
            if msg["type"] == "text":
                st.session_state.messages.append({"role": "assistant", "content": msg["content"], "type": "text"})
                with st.chat_message("assistant"):
                    st.markdown(f"financito bot: {msg['content']}")
            elif msg["type"] == "image":
                st.session_state.messages.append({"role": "assistant", "content": msg["content"], "type": "image"})
                st.image(msg["content"], caption="Image from bot")
            elif msg["type"] == "buttons":
                #st.write(response)
                #a = "" 
                #for pay in response:
                        #if pay["type"] == "payload":
                            #a = pay
                #st.write(a)
                i = msg["content"]
                res = display_buttons(i)
                #st.write(res),"fim"
                st.session_state.messages.append({"role": "assistant", "content": res, "type": "text"})
                   
ui()