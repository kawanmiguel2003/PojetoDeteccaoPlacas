import streamlit as st
import Controllers.PessoaController as PessoaController
import models.Pessoa as pessoa

def Incluir():
    idAlteracao = st.experimental_get_query_params()
    st.experimental_set_query_params()
    pessoaRecuperada = None
    if idAlteracao.get("id") != None:
        idAlteracao = idAlteracao.get("id")[0]
        pessoaRecuperada = PessoaController.SelecionarById(idAlteracao)
        st.experimental_set_query_params(
            id=[pessoaRecuperada.id]
        )
        st.title("Alterar Pessoa")
    else:
        st.title("Incluir Pessoa")

    with st.form(key="include_pessoa"):
        if pessoaRecuperada == None:
            input_nome = st.text_input(label="Insira seu Nome")
            input_ra = st.text_input(label="Insira seu RA")
            input_cpf = st.text_input(label="Insira seu CPF")
            input_id_veiculo = st.number_input(label="Insira o ID do seu veiculo", format="%d", step=1)
        else:
            input_nome = st.text_input(label="Insira seu Nome", value= pessoaRecuperada.nome)
            input_ra = st.text_input(label="Insira seu RA",value= pessoaRecuperada.ra)
            input_cpf = st.text_input(label="Insira seu CPF", value= pessoaRecuperada.cpf)
            input_id_veiculo = st.number_input(label="Insira o ID do seu veiculo", format="%d", step=1, value= pessoaRecuperada.idVeiculo)
        input_button_submit = st.form_submit_button("Enviar")

    if input_button_submit:
        if pessoaRecuperada == None:
            PessoaController.Incluir(pessoa.Pessoa(0, input_nome, input_ra, input_cpf, input_id_veiculo))
            st.success("Pessoa adicionada com sucesso!")
        else:
            st.experimental_set_query_params()
            PessoaController.Alterar(pessoa.Pessoa(pessoaRecuperada.id, input_nome, input_ra, input_cpf, input_id_veiculo))
            st.success("Pessoa alterada com sucesso!")

