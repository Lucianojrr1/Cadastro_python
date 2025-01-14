import streamlit as st

st.title("Cadastro de Clientes")

nome = st.text_input("Digite o nome do Cliente")
endereco = st.text_input("Digite o endereco correto")
dt_nasc = st.date_input("Escolha a data de Nascimento")
tipo_cliente = st.selectbox("Tipo de Cliente", ["Pessoa Física","Pessoa Jurídica"])
cadastrar = st.button("Cadastrar cliente")
if cadastrar:
    with open("clientes.csv", "a", encoding="utf8") as arquivo:
        arquivo.write(f"{nome},{endereco},{dt_nasc},{tipo_cliente}\n")
        st.success("Cliente cadastrado com sucesso.")