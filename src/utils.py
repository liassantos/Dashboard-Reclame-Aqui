import pandas as pd
import plotly.express as px
import streamlit as st
import time


def criar_serie_temporal(df):
  df_data = df['TEMPO'].value_counts().reset_index()
  df_data.columns = ['Data', 'Qtd de Reclamações']
  df_data = df_data.sort_values(by='Data')
  return df_data


def criar_df_estado(df):
    df_estado = df['ESTADO'].value_counts().reset_index()
    df_estado.columns = ['Estado', 'Qtd de Reclamações']
    df_estado = df_estado.sort_values(by='Qtd de Reclamações', ascending=True)
    return df_estado


def criar_df_status(df):
  df_status = df['STATUS'].value_counts().reset_index()
  df_status.columns = ['Status', 'Qtd de Reclamações']
  df_status = df_status.sort_values(by='Qtd de Reclamações', ascending=True)
  return df_status


def criar_df_tam_texto(df):
  df_tam_texto = df['TAMANHO_TEXTO'].value_counts().reset_index()
  df_tam_texto.columns = ['Caracteres', 'Frequência']
  df_tam_texto = df_tam_texto.sort_values(by='Frequência', ascending=True)
  return df_tam_texto


def filtrar_dados(df_escolhido, option_estado, option_status):
    if option_estado != "TODOS" and option_status != "TODOS":
        dados = df_escolhido[(df_escolhido['ESTADO'] == option_estado) & (df_escolhido['STATUS'] == option_status)]
    elif option_estado != "TODOS" and option_status == "TODOS":
        dados = df_escolhido[df_escolhido['ESTADO'] == option_estado]
    elif option_estado == "TODOS" and option_status != "TODOS":
        dados = df_escolhido[df_escolhido['STATUS'] == option_status]
    else:
        dados = df_escolhido
    return dados


#Criando gráfico Série Temporal
def plotar_serie_temporal(df):
    df_plot = criar_serie_temporal(df)
    fig_serie_temporal = px.line(df_plot,
                x='Data',
                y='Qtd de Reclamações',
                title = 'Série Temporal do Número de Reclamações'
                )
    fig_serie_temporal.update_traces(mode='lines+markers', 
                                marker=dict(size=6, color="#71b36c"), 
                                textposition='top center',
                                line=dict(color="#71b36c")
                                )
    fig_serie_temporal.update_layout(xaxis_title='Data', 
                                yaxis_title='Qtd de Reclamações', 
                                yaxis=dict(range=[0, df_plot['Qtd de Reclamações'].max() + 2])
                                )
    fig_serie_temporal.update_xaxes(minor=dict(ticks="inside", showgrid=True))
    return fig_serie_temporal


#Criando gráfico Frequência por Estado
def plotar_estados(df):
    fig_estado = px.bar(criar_df_estado(df),
                x='Qtd de Reclamações',
                y='Estado',
                title ='Reclamações por Estado',
                orientation ='h',
                text='Qtd de Reclamações'
                )
    fig_estado.update_traces(textposition='outside',
                             marker_color="#71b36c",
                             textfont=dict(color="white")
                             )
    fig_estado.update_layout(xaxis_title='Estado', yaxis_title='Qtd de Reclamações')
    fig_estado.update_xaxes(
        showgrid=False,
        title_text='Quantidade de Reclamações',
        title_font=dict(color='white'),  
        tickfont=dict(color='white')     
    )
    fig_estado.update_yaxes(
        showgrid=False,
        title_text='Estado',
        title_font=dict(color='white'),  
        tickfont=dict(color='white')
    )
    fig_estado.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        width=800,
        height=450
    )
    return fig_estado


#Criando gráfico Frequência por Status
def plotar_status(df):
    fig_status = px.bar(criar_df_status(df),
                x='Qtd de Reclamações',
                y='Status',
                title ='Reclamações por Status',
                orientation ='h',
                text='Qtd de Reclamações'
                )
    fig_status.update_traces(textposition='inside',
                             marker_color="#71b36c",
                             textfont=dict(color="white")
                             )
    fig_status.update_layout(xaxis_title='Status', yaxis_title='Qtd de Reclamações')
    fig_status.update_xaxes(
        showgrid=False,
        title_text='Quantidade de Reclamações',
        title_font=dict(color='white'),  
        tickfont=dict(color='white')     
    )
    fig_status.update_yaxes(
        showgrid=False,
        title_text='Status',
        title_font=dict(color='white'),  
        tickfont=dict(color='white')
    )
    fig_status.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        width=800,
        height=450
    )
    return fig_status


#Criando gráfico Distribuição do tamanho do texto
def plotar_tam_texto(df):
    fig_tam_texto = px.histogram(criar_df_tam_texto(df),
                x='Caracteres',
                title ='Distribuição do Tamanho do Texto'
                )

    fig_tam_texto.update_layout(xaxis_title='Qtd de Caracteres', 
                                yaxis_title='Frequência'
                                )
    fig_tam_texto.update_traces(marker_color="#71b36c")
    fig_tam_texto.update_xaxes(
        showgrid=False,
        title_text='Quantidade de Caracteres',
        title_font=dict(color='white'),  
        tickfont=dict(color='white')     
    )
    fig_tam_texto.update_yaxes(
        title_text='Frequência',
        title_font=dict(color='white'),  
        tickfont=dict(color='white')
    )
    fig_tam_texto.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        width=800,
        height=450
    )
    return fig_tam_texto


def mostrar_dados(func):
    TEXTO = "Os dados relacionados ao gráfico podem ser vistos abaixo. Você pode ordenar as colunas clicando no cabeçalho delas:"

    for word in TEXTO.split(" "):
        yield word + " "
        time.sleep(0.02)

    yield func


def mostrar_gráficos(df_filtrado):
    tab1, tab2, tab3, tab4 = st.tabs(["📈 Série Temporal", "🗺️ Estados", "🔄️ Status", "✍️ Tamanho do Texto"])
    with tab1:
        st.plotly_chart(plotar_serie_temporal(df_filtrado), use_container_width=True)
        if st.button("Dados Série Temporal"):
            st.write_stream(mostrar_dados(criar_serie_temporal(df_filtrado)))
    with tab2:
        st.plotly_chart(plotar_estados(df_filtrado), use_container_width=True)
        if st.button("Dados dos Estados"):
            st.write_stream(mostrar_dados(criar_df_estado(df_filtrado)))
    with tab3:
        st.plotly_chart(plotar_status(df_filtrado), use_container_width=True)
        if st.button("Dados dos Status"):
            st.write_stream(mostrar_dados(criar_df_status(df_filtrado)))
    with tab4:
        st.plotly_chart(plotar_tam_texto(df_filtrado), use_container_width=True)
        if st.button("Dados de Texto"):
            st.write_stream(mostrar_dados(criar_df_tam_texto(df_filtrado)))

