from dotenv import load_dotenv
import os


load_dotenv()


nome = os.getenv("NOME_UTENTE")
città = os.getenv("CITTA")
api_key = os.getenv("API_KEY")

print(nome)
print(città)
print(api_key)