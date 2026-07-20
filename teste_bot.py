import requests
from config import TELEGRAM_TOKEN


url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/getMe"


resposta = requests.get(url)


print(resposta.json())