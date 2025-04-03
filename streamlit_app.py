import streamlit as st

# Configuração da página
st.set_page_config(page_title="Meu Site Streamlit", page_icon="🌎", layout="wide")

# Barra lateral
st.sidebar.title("Navegação")
pagina = st.sidebar.radio("Selecione uma página:", ["Home", "Sobre", "Contato"])

# Página inicial
if pagina == "Home":
    st.title("🌟 Bem-vindo ao Meu Site com Streamlit!")
    st.write("Este é um site simples criado com Streamlit.")
    st.image("https://source.unsplash.com/800x400/?technology", caption="Imagem ilustrativa")

    # Criando um botão interativo
    if st.button("Clique aqui!"):
        st.success("Você clicou no botão! 🎉")

# Página "Sobre"
elif pagina == "Sobre":
    st.title("📌 Sobre Nós")
    st.write("Aqui você pode adicionar informações sobre o projeto, empresa ou equipe.")
    st.info("Esta aplicação foi criada usando Python + Streamlit.")

# Página "Contato"
elif pagina == "Contato":
    st.title("📞 Contato")
    st.write("Entre em contato preenchendo o formulário abaixo.")
    
    nome = st.text_input("Seu nome:")
    email = st.text_input("Seu e-mail:")
    mensagem = st.text_area("Sua mensagem:")

    if st.button("Enviar"):
        st.success(f"Obrigado, {nome}! Entraremos em contato pelo e-mail {email}.")

# Rodapé
st.markdown("---")
st.markdown("📌 Criado com ❤️ usando Streamlit")
