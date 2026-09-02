'''
instalando o requests, comando: pip install requests;

Divisão dos Papéis & Regras (5 min)

🧑‍💻 Driver (Piloto): Fica no teclado. Escreve a sintaxe Python, cria as variáveis e executa o código no terminal.

🧭 Navigator (Navegador): Não toca no teclado. Analisa a documentação da API, orienta a lógica das requisições e verifica se as variáveis estão em snake_case.  

⏱️ Timer: Troca de papéis a cada 15 minutos.


'''

import requests

url_api = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL"


resposta = requests.get(url_api)

if resposta.status_code == 200:
    dados = resposta.json()
    print("Conexão estabelecida com sucesso!")
else:
    print(f"Erro na requisição: {resposta.status_code}")
    
cotacao_dolar = dados["USDBRL"]["bid"]
nome_moeda = dados["USDBRL"]["name"]

print(f"Moeda: {nome_moeda}")
print(f"Valor atual de compra: R$ {float(cotacao_dolar):.2f}")
