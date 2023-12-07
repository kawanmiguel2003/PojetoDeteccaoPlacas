import this
from turtle import onclick
import streamlit as st
import Controllers.VeiculoController as VeiculoController
import models.Veiculo as veiculo

def Incluir():
    idAlteracaoVeiculo = st.experimental_get_query_params()
    st.experimental_set_query_params()
    veiculoRecuperado = None
    if idAlteracaoVeiculo.get("id") != None:
        idAlteracaoVeiculo = idAlteracaoVeiculo.get("id")[0]
        veiculoRecuperado = VeiculoController.SelecionarVeiculoById(idAlteracaoVeiculo)
        st.experimental_set_query_params(
            id=[veiculoRecuperado.id]
        )
        st.title("Alterar Veiculo")
    else:
        st.title("Incluir Veiculo")

    with st.form(key="include_veiculo"):
        if veiculoRecuperado ==None:
            input_modelo = st.text_input(label="Insira o modelo do veiculo")
            input_cor = st.text_input(label="Insira a cor do veiculo")
            input_placa = st.text_input(label="Insira a placa do veiculo")


        else:
            input_modelo = st.text_input(label="Insira o modelo do veiculo", value = veiculoRecuperado.modelo)
            input_cor = st.text_input(label="Insira a cor do veiculo", value= veiculoRecuperado.cor)
            input_placa = st.text_input(label="Insira a placa do veiculo", value= veiculoRecuperado.placa)
        input_button_submit = st.form_submit_button("Enviar")


    if input_button_submit:
        if veiculoRecuperado == None:
            VeiculoController.IncluirVeiculos(veiculo.Veiculo(0, input_modelo, input_cor, input_placa))
            st.success("Veiculo adicionado com sucesso!")
        else:
            st.experimental_set_query_params()
            VeiculoController.IncluirVeiculos(veiculo.Veiculo(veiculoRecuperado.id, input_modelo, input_cor, input_placa))
            st.success("Veiculo alterado com sucesso!")