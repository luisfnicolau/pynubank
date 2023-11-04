from pynubank import Nubank, MockHttpClient
from dotenv import load_dotenv
import json
import os

load_dotenv()

cpf = os.getenv("CPF")
password = os.getenv("PASSWORD")


# nu = Nubank(MockHttpClient())
nu = Nubank()
nu.authenticate_with_cert(cpf, password, "./cert.p12")

# Lista de dicionários contendo todas as transações de seu cartão de crédito
card_statements = nu.get_card_statements()

f = open("extract.json", "w")
extractJson = json_data = json.dumps(card_statements, indent=2)

f.write(extractJson)
f.close()

# Retorna um dicionário contendo os detalhes de uma transação retornada por get_card_statements()
# Contém as parcelas da transação
# card_statement_details = nu.get_card_statement_details(card_statements[0])

# Soma de todas as compras
print(sum([t['amount'] for t in card_statements]))