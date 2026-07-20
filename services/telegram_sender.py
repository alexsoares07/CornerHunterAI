import requests
from config import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID



class TelegramSender:


    def __init__(self):

        self.token = TELEGRAM_TOKEN
        self.chat_id = TELEGRAM_CHAT_ID



    def send(self, signal):


        if not signal:

            print("Nenhum sinal para enviar")
            return False



        corners = signal.get(
            "corners",
            {}
        )



        mensagem = f"""
🚨 OPORTUNIDADE DE CANTOS

⚽ Jogo:
{signal.get('match', '')}

⏱ Minuto:
{signal.get('minute', '')}

📊 Placar:
{signal.get('result', '')}

🚩 Escanteios:
{corners.get('total_corners', 0)}

🔥 Confiança:
{signal.get('confidence', 0)} pontos

📌 Motivos:
"""



        for motivo in signal.get(
            "reasons",
            []
        ):

            mensagem += f"\n• {motivo}"



        url = (
            f"https://api.telegram.org/"
            f"bot{self.token}/sendMessage"
        )



        data = {

            "chat_id": self.chat_id,

            "text": mensagem

        }



        try:


            resposta = requests.post(

                url,

                data=data,

                timeout=10

            )



            print("\nSTATUS TELEGRAM:")

            print(
                resposta.status_code
            )



            print("\nRETORNO TELEGRAM:")

            print(
                resposta.text
            )



            return resposta.json()



        except Exception as e:


            print("\nERRO TELEGRAM:")

            print(e)


            return None