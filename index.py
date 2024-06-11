import requests
import streamlit as st

BASE_URL = "http://localhost:5005/webhooks/rest/webhook" #https://api.github.com/users/facebook

def selecionarUsuario(username):
    url = f'{BASE_URL}/users/{username}'
    response = requests.get(url)
    if response.status_code ==200:
        return response.json()
    else:
        return None
    
def ui():
    st.markdown('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">', unsafe_allow_html=True)

    st.title("consulta git hub")
    username = st.text_input("Insira o username de usuário do Github")

    if st.button("Buscar"):
        inforUsuario = selecionarUsuario(username)
        if inforUsuario is not None:
            st.write(inforUsuario)

ui()


