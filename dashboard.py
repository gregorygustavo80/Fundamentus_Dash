import streamlit as st
import pandas as pd
import re
import plotly.graph_objects as go

data = pd.read_excel('comparacao_fundos.xlsx')
df = pd.DataFrame(data)

df = df.sort_values(by='Preço', ascending=True)

def clean_and_convert(value):
    cleaned_value = re.sub(r'[^\d.,]', '', value)  
    cleaned_value = cleaned_value.replace(',', '.') 
    return float(cleaned_value)

df['Preço'] = df['Preço'].apply(clean_and_convert)
df['Dividend Yield'] = df['Dividend Yield'].apply(clean_and_convert)
df['Último Rendimento'] = df['Último Rendimento'].apply(clean_and_convert)
df['PVP'] = df['PVP'].apply(clean_and_convert)

st.set_page_config(layout="wide")
st.markdown("<h1 style='text-align: center;'>Compare Fundos Imobiliários</h1>", unsafe_allow_html=True)

fig1 = go.Figure()
fig1.add_trace(go.Bar(x=df['Ticket'], y=df['Preço'], text=df['Ticket'], name='Preço', marker_color='blue'))
fig1.update_layout(title='Preço (R$)', xaxis_title='Ticket', yaxis_title='Preço (R$)', title_x=0.5, yaxis_tickprefix='R$')

fig2 = go.Figure()
fig2.add_trace(go.Bar(x=df['Ticket'], y=df['Dividend Yield'], text=df['Ticket'], name='Dividend Yield', marker_color='green'))
fig2.update_layout(title='Dividend Yield', xaxis_title='Ticket', yaxis_title='Dividend Yield', title_x=0.5)

fig3 = go.Figure()
fig3.add_trace(go.Bar(x=df['Ticket'], y=df['Último Rendimento'], text=df['Ticket'], name='Último Rendimento', marker_color='orange'))
fig3.update_layout(title='Último Rendimento (R$)', xaxis_title='Ticket', yaxis_title='Último Rendimento (R$)', title_x=0.5, yaxis_tickprefix='R$')

fig4 = go.Figure()
fig4.add_trace(go.Bar(x=df['Ticket'], y=df['PVP'], text=df['Ticket'], name='P/VP dos Fundos', marker_color='purple'))
fig4.update_layout(title='P/VP dos Fundos', xaxis_title='Ticket', yaxis_title='P/VP', title_x=0.5)

col1, col2 = st.columns(2)

col1.plotly_chart(fig1)
col1.plotly_chart(fig3)
col2.plotly_chart(fig2)
col2.plotly_chart(fig4)
