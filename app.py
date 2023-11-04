from pynubank import Nubank, MockHttpClient
from dotenv import load_dotenv
import os

load_dotenv()

cpf = os.getenv("CPF")
password = os.getenv("SENHA")


nu = Nubank(MockHttpClient())
nu.authenticate_with_cert("qualquer-cpf", "qualquer-senha", "./cert.p12")

# Lista de dicionários contendo todas as transações de seu cartão de crédito
card_statements = nu.get_card_statements()

# Retorna um dicionário contendo os detalhes de uma transação retornada por get_card_statements()
# Contém as parcelas da transação
# card_statement_details = nu.get_card_statement_details(card_statements[0])

print(card_statements)
# Soma de todas as compras
print(sum([t['amount'] for t in card_statements]))