import requests
import streamlit as st

BASE_URL = "https://api.github.com" #https://api.github.com/users/facebook

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
            st.markdown(
                f'''
                <div class="card" style="width: 18rem;">
                    <img class="card-img-top" src="{inforUsuario['avatar_url']}" alt="Card image cap">
                    <div class="card-body">
                        <h5 class="card-title">{inforUsuario['login']}</h5>
                        <p class="card-text">{inforUsuario['bio']}</p>
                        <a href="{inforUsuario['html_url']}" style="color: white; text-decoration: none;" class="btn btn-primary">ver perfil</a>
                    </div>
                </div>

                ''', unsafe_allow_html=True)

ui()


