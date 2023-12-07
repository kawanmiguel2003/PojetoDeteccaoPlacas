import streamlit as st
import Controllers.VeiculoController as VeiculoController
import Pages.Veiculo.Create as PageCreateVeiculo

def Read():
    paramId= st.experimental_get_query_params()
    if paramId == {}:
        st.experimental_set_query_params()
        colms = st.columns((1,2,2,2,1,1))
        campos = ['ID', 'Modelo', 'Cor ', 'Placa', 'Excluir', 'Alterar']
        for col, campo_nome in zip(colms, campos):
            col.write(campo_nome)

        for item in VeiculoController.SelecionarTodosVeiculos():
            col1, col2, col3, col4, col5, col6, = st.columns((1,2,2,2,1,1))
            col1.write(item.id)
            col2.write(item.modelo)
            col3.write(item.cor)
            col4.write(item.placa)
            button_space_excluir_veiculo = col5.empty()
            on_click_excluir_veiculo = button_space_excluir_veiculo.button('Excluir', 'btnExcluirVeiculo' + str(item.id))
            button_space_alterar_veiculo = col6.empty()
            on_click_alterar_veiculo = button_space_alterar_veiculo.button('Alterar', 'btnAlterarVeiculo' + str(item.id))

            if on_click_excluir_veiculo:
                VeiculoController.ExcluirVeiculo(item.id)
                button_space_excluir_veiculo.button(
                    'Excluido', 'btnExcluirVeiculo' + str(item.id))

            if on_click_alterar_veiculo:
                st.experimental_set_query_params(
                    id =[item.id]
                )
                st.rerun()

        else:
            on_click_voltar = st.button("Voltar", key= 10)
            if on_click_voltar:
                st.experimental_set_query_params()
                st.experimental_rerun()
            PageCreateVeiculo.Incluir()