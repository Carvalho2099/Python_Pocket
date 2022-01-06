import requests
import pandas as pd
from datetime import datetime
import time
# para rodar o codigo varias vezes durante o dia é necessário importar time e colocar todo o codigo dentro de um
# while True, definindo o tempo de espera no final do código
# while True:
#   código
#   time.sleep(60) tempo em segundos
# pode ser utilizado for caso queira rodar uma determinada quantidade de vezes


requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

requisicao_dict = requisicao.json()
cotacao_dolar = requisicao_dict["USDBRL"]["bid"]
cotacao_euro = requisicao_dict["EURBRL"]["bid"]
cotacao_btc = requisicao_dict["BTCBRL"]["bid"]

tabela = pd.read_excel("Cotações.xlsx", engine="openpyxl")
tabela.loc[0, "Cotação"] = float(cotacao_dolar)
tabela.loc[1, "Cotação"] = float(cotacao_euro)
tabela.loc[0, "Data Útima Verificação"] = f'{datetime.now():%d/%m/%y}'

tabela.to_excel("Cotações.xlsx", index=False)
print(f"Cotação Atualizada. {datetime.now():%d/%m/%y}")
