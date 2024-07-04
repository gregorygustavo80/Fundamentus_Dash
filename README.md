# Comparador de Fundos Imobiliários

Este é um projeto para comparar diferentes Fundos Imobiliários utilizando dados do site [Funds Explorer](https://www.fundsexplorer.com.br/). O programa é desenvolvido em Python e usa bibliotecas como `tkinter`, `BeautifulSoup`, `requests` e `pandas`.

## Funcionalidades

- Interface gráfica para entrada de até quatro tickets de fundos imobiliários.
- Coleta de informações como Preço, Dividend Yield, Último Rendimento e P/VP dos fundos imobiliários.
- Exportação dos dados coletados para um arquivo Excel.
- Integração com o Streamlit para exibição dos dados em um dashboard interativo.

## Requisitos

+ Python 3.x
+ tkinter
+ BeautifulSoup
+ requests
+ pandas
+ openpyxl
+ streamlit

## Instalação

1. Clone este repositório:
    ```sh
    git clone https://github.com/gregorygustavo80/Fundamentus_Dash.git
    ```

2. Navegue até o diretório do projeto:
    ```sh
    cd Fundamentus_Dash
    ```

3. Crie um ambiente virtual e instale as dependências:
    ```
    python -m venv venv 

    venv/Scripts/activate 

    pip install -r requirements.txt
    ```

## Uso

1. Execute o script `main.py` para abrir a interface gráfica:
    ```
    python main.py
    ```

2. Digite os tickets dos fundos imobiliários que deseja comparar e clique no botão "Comparar".

3. Os resultados serão salvos em um arquivo Excel chamado `comparacao_fundos.xlsx`.

4. Após a coleta dos dados, feche a interface gráfica. Um dashboard interativo será aberto utilizando Streamlit.

## Estrutura do Código

- `main.py`: Contém a lógica principal do programa, incluindo a interface gráfica e a coleta de dados.
- `dashboard.py`: Script para exibir o dashboard interativo com os dados coletados.

## Contribuição

Contribuições são bem-vindas! Se você tiver alguma sugestão ou encontrar algum problema, por favor abra uma issue ou envie um pull request.

---


