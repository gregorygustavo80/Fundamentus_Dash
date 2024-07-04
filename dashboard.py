import streamlit as st
import pandas as pd
import re
import plotly.graph_objects as go


data = pd.read_excel('comparacao_fundos.xlsx')
df = pd.DataFrame(data)

# Função para limpar e converter valores
def clean_and_convert(value):
    if isinstance(value, str):
        cleaned_value = re.sub(r'[^\d.,]', '', value)
        cleaned_value = cleaned_value.replace(',', '.')
        return float(cleaned_value)
    return value

# Aplicando a função de limpeza e conversão
df['Preço'] = df['Preço'].apply(clean_and_convert)
df['Dividend Yield'] = df['Dividend Yield'].apply(clean_and_convert)
df['Último Rendimento'] = df['Último Rendimento'].apply(clean_and_convert)
df['PVP'] = df['PVP'].apply(clean_and_convert)

# Configurando a página do Streamlit
st.set_page_config(layout="wide")
st.markdown("<h1 style='text-align: center;'>Compare Fundos Imobiliários</h1>", unsafe_allow_html=True)

# Criando os gráficos ordenados de forma ascendente

# Gráfico de Preço
df_sorted = df.sort_values(by='Preço', ascending=True)
fig1 = go.Figure()
fig1.add_trace(go.Bar(x=df_sorted['Ticket'], y=df_sorted['Preço'], text=df_sorted['Ticket'], name='Preço', marker=dict(
    color=df_sorted['Preço'], colorscale='Viridis')))
fig1.update_layout(title='Preço (R$)', xaxis_title='Ticket', yaxis_title='Preço (R$)', title_x=0.5, yaxis_tickprefix='R$')

# Gráfico de Dividend Yield
df_sorted = df.sort_values(by='Dividend Yield', ascending=True)
fig2 = go.Figure()
fig2.add_trace(go.Bar(x=df_sorted['Ticket'], y=df_sorted['Dividend Yield'], text=df_sorted['Ticket'], name='Dividend Yield', marker=dict(
    color=df_sorted['Dividend Yield'], colorscale='cividis')))
fig2.update_layout(title='Dividend Yield', xaxis_title='Ticket', yaxis_title='Dividend Yield (%)', title_x=0.5)

# Gráfico de Último Rendimento
df_sorted = df.sort_values(by='Último Rendimento', ascending=True)
fig3 = go.Figure()
fig3.add_trace(go.Bar(x=df_sorted['Ticket'], y=df_sorted['Último Rendimento'], text=df_sorted['Ticket'], name='Último Rendimento', marker=dict(
    color=df_sorted['Último Rendimento'], colorscale='Blues')))
fig3.update_layout(title='Último Rendimento (R$)', xaxis_title='Ticket', yaxis_title='Último Rendimento (R$)', title_x=0.5, yaxis_tickprefix='R$')

# Gráfico de PVP
df_sorted = df.sort_values(by='PVP', ascending=True)
fig4 = go.Figure()
fig4.add_trace(go.Bar(x=df_sorted['Ticket'], y=df_sorted['PVP'], text=df_sorted['Ticket'], name='P/VP dos Fundos', marker=dict(
    color=df_sorted['PVP'], colorscale='Greens')))
fig4.update_layout(title='P/VP dos Fundos', xaxis_title='Ticket', yaxis_title='P/VP', title_x=0.5)

# Dividindo a tela em duas colunas
col1, col2 = st.columns(2)

# Exibindo os gráficos nas colunas
col1.plotly_chart(fig1)
col1.plotly_chart(fig3)
col2.plotly_chart(fig2)
col2.plotly_chart(fig4)
