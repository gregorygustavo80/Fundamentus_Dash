import tkinter as tk
from bs4 import BeautifulSoup
import requests
import pandas as pd
import os 
import time

def get_fund_details(ticker):

    url = f'https://www.fundsexplorer.com.br/funds/{ticker}'
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Erro ao acessar {url}: {response.status_code}")
        return None
    soup = BeautifulSoup(response.content, 'html.parser')

# Encontra o Ticket

    def ticket():
        ticket_element = soup.find('h1', class_='headerTicker__content__title')
        if ticket_element:
            return ticket_element.text.strip()
        else:
            return None
        
# Encontra o preço 
    def price():
        price_element = soup.find('div', class_='headerTicker__content__price')
        if price_element:
            return price_element.find('p').text.strip()
        else:
            return None
        
#Encontra o Dividend Yield

    def DY():
        dy_element = soup.find('p', string='Dividend Yield')
        if dy_element:
            b_element = dy_element.find_next('b')
            if b_element:
                return b_element.get_text(strip=True)
        return None
    
# Encontra o último rendimento mensal

    def rendimento():
        rendimento_element = soup.find('p', string='Último Rendimento')
        if rendimento_element:
            b_element = rendimento_element.find_next('b')
            if b_element:
                return b_element.get_text(strip=True)
        return None
    
# Encontra o preço sobre o valor patrimonial da cota

    def PVP():
        pvp_element = soup.find('p', string='P/VP')
        if pvp_element:
            b_element = pvp_element.find_next('b')
            if b_element:
                return b_element.get_text(strip=True)
        return None

    details = {
        'Ticket': ticket(),
        'Preço': price(),
        'Dividend Yield': DY(),
        'Último Rendimento': rendimento(),
        'PVP': PVP()
    }

    return details

def salvar_resultados(tickets):
    data = []
    for ticket in tickets:
        details = get_fund_details(ticket)
        if details:
            data.append({
                'Ticket': details["Ticket"],
                'Preço': details["Preço"].strip(),
                'Dividend Yield': details["Dividend Yield"],
                'Último Rendimento': details["Último Rendimento"],
                'PVP': details["PVP"]
            })

    df = pd.DataFrame(data)
    nome_arquivo = 'comparacao_fundos.xlsx'

    df.to_excel(nome_arquivo, index=False)
    print(f'Resultados salvos em {nome_arquivo}')



def transicao():
    wait()
    janela.after(3000, mostrar_mensagem)

def wait():
    label.config(text="Carregando...")

def restaurar_texto_original():
    label.config(text="Digite aqui seus Tickets")

def mostrar_mensagem():
    texto1 = caixa_texto1.get()
    texto2 = caixa_texto2.get()
    texto3 = caixa_texto3.get()
    texto4 = caixa_texto4.get()

    tickets = [texto1, texto2, texto3, texto4]
    salvar_resultados(tickets)
    restaurar_texto_original()

def restaurar_texto_original():
    label.config(text="Digite aqui seus Tickets")

janela = tk.Tk()
janela.title("Comparador de Fundos Imobiliários")

# Caixas de texto
caixa_texto1 = tk.Entry(janela, width=30)
caixa_texto1.pack(pady=10)

caixa_texto2 = tk.Entry(janela, width=30)
caixa_texto2.pack(pady=10)

caixa_texto3 = tk.Entry(janela, width=30)
caixa_texto3.pack(pady=10)

caixa_texto4 = tk.Entry(janela, width=30)
caixa_texto4.pack(pady=10)

label = tk.Label(janela, text="Digite aqui seus Tickets")
label.pack(pady=10)

botao = tk.Button(janela, text="Comparar", width=50, command=transicao)
botao.pack(pady=10)

janela.mainloop()

os.system('streamlit run dashboard.py')