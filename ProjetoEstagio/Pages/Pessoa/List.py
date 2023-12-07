import streamlit as st
import Controllers.PessoaController as PessoaController
import Pages.Pessoa.Create as PageCreateCliente


def Read():
    params = st.experimental_get_query_params()
    if params.get("id") == None:
        st.experimental_set_query_params()
        colms = st.columns((1, 2, 2, 2, 2, 1, 1))
        campos = ['ID', 'Nome', 'RA ', 'CPF', 'idVeiculo', 'Excluir', 'Alterar']
        for col, campo_nome in zip(colms, campos):
            col.write(campo_nome)

        for x, item in enumerate(PessoaController.SelecionarTodos()):
            col1, col2, col3, col4, col5, col6, col7 = st.columns((1, 2, 2, 2, 2, 1, 1))
            col1.write(item.id)
            col2.write(item.nome)
            col3.write(item.ra)
            col4.write(item.cpf)
            col5.write(item.idVeiculo)
            button_space_excluir = col6.empty()
            on_click_excluir = button_space_excluir.button(
                'Excluir', 'btnExcluir' + str(item.id))
            button_space_alterar = col7.empty()
            on_click_alterar = button_space_alterar.button(
                'Alterar', 'btnAlterar' + str(item.id))

            if on_click_excluir:
                PessoaController.Excluir(item.id)

            if on_click_alterar:
                st.experimental_set_query_params(
                    id=[item.id]

                )
                st.write(item.id)
                st.experimental_rerun()



    else:
        on_click_voltar = st.button("Voltar")
        if on_click_voltar:
            st.experimental_set_query_params()
            st.experimental_rerun()
        PageCreateCliente.Incluir()
