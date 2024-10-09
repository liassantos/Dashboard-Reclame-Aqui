import streamlit as st
from tratamento_dados import estados_hapvida, estados_ibyte, estados_nagem, lista_status, df_hapvida, df_ibyte, df_nagem
import utils as ut
from config import LOGO_RECLAME_PATH

def main():           
    st.title("Análise Reclame Aqui 🔍")

    #opção empresa
    with st.sidebar:
        option_empresa = st.selectbox(
            "Selecione uma Empresa",
            ("Escolha uma opção", "Hapvida", "Nagem", "Ibyte"),
        )


    #opção estado
    if option_empresa == "Hapvida":
        with st.sidebar:
            option_estado = st.selectbox(
                "Selecione um Estado",
                estados_hapvida,
            )
            #opção status
            option_status = st.selectbox(
                "Selecione um Status",
                lista_status,
            )
        df_escolhido = df_hapvida
        ut.mostrar_gráficos(ut.filtrar_dados(df_escolhido, option_estado, option_status))
    elif option_empresa == "Ibyte":
        with st.sidebar:
            option_estado = st.selectbox(
                "Selecione um Estado",
                estados_ibyte,
            )
            #opção status
            option_status = st.selectbox(
                "Selecione um Status",
                lista_status,
            )
        df_escolhido = df_ibyte
        ut.mostrar_gráficos(ut.filtrar_dados(df_escolhido, option_estado, option_status))
    elif option_empresa == "Nagem":
        with st.sidebar:
            option_estado = st.selectbox(
                "Selecione um Estado",
                estados_nagem,
            )
            #opção status
            option_status = st.selectbox(
                "Selecione um Status",
                lista_status,
            )
        df_escolhido = df_nagem
        ut.mostrar_gráficos(ut.filtrar_dados(df_escolhido, option_estado, option_status))
    else:
        with st.sidebar:
            st.write("Para começar a análise, selecione uma empresa.")
        st.image(LOGO_RECLAME_PATH)
        st.write("""Bem-vindo ao nosso aplicativo de Análise de reclamações do Reclame Aqui! Aqui, você pode explorar e analisar as reclamações registradas no site Reclame Aqui para três empresas: Hapvida, Ibyte e Nagem. Nossa plataforma oferece insights detalhados sobre as experiências dos consumidores, permitindo que você entenda melhor a reputação dessas empresas e identifique padrões de reclamação. Navegue pelos dados e descubra informações valiosas que podem auxiliar na tomada de decisões e na melhoria do atendimento ao cliente.
    """)

if __name__ == "__main__":
    main()
