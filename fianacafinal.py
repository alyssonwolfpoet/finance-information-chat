import streamlit as st
import requests
from PIL import Image
from io import BytesIO
import base64

# URL do seu servidor Rasa
RASA_URL = "http://localhost:5005/webhooks/rest/webhook"

# Função para enviar mensagem para o Rasa e obter a resposta
def send_message(message):
    payload = {
        "sender": "user",
        "message": message
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(RASA_URL, json=payload, headers=headers)
    return response.json()

# Função para exibir a imagem ou GIF no Streamlit
def display_image(image_url):
    if image_url.startswith("data:image"):
        image_base64 = image_url.split(",")[1]
        image_data = base64.b64decode(image_base64)
        image = Image.open(BytesIO(image_data))
        st.image(image, caption='Imagem', use_column_width=True)
    else:
        if image_url.lower().endswith(('.gif', '.jpg', '.jpeg', '.png')):
            st.image(image_url, caption='Imagem', use_column_width=True)
        else:
            st.warning("Formato de imagem não suportado.")

# Função para exibir os botões
def display_buttons(buttons, chat_index):
    num_buttons = len(buttons)
    for idx, button in enumerate(buttons):
        if st.button(button["title"], key=f"button_{chat_index}_{idx}"):
            response = send_message(button["payload"])
            st.session_state.history.append({"user": button["title"], "bot": response})

# Streamlit interface
st.title("Chatbot de Informações Financeiras")
st.write("Bem-vindo! Diga em que podemos ajudar 🕵️‍♂️")

# Inicializar histórico da sessão para chat
if "history" not in st.session_state:
    st.session_state.history = []

# Entrada do usuário usando st.chat_input
user_input = st.chat_input("Digite algo ")

if user_input:
    response = send_message(user_input)
    st.session_state.history.append({"user": user_input, "bot": response})

# Exibir histórico do chat
for chat_index, chat in enumerate(st.session_state.history):
    # Exibir mensagem do usuário
    st.markdown(f"*👤:* {chat['user']}")

    last_bot_response = ""
    for res in chat["bot"]:
        if "text" in res and res["text"] != last_bot_response:
            # Exibir mensagem do bot
            st.markdown(f"*🕵️‍♂️:* {res['text']}")
            last_bot_response = res["text"]
        if "image" in res:
            display_image(res["image"])
        if "buttons" in res:
            display_buttons(res["buttons"], chat_index)