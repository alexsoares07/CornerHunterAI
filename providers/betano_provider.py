from playwright.sync_api import sync_playwright



class BetanoProvider:


    def __init__(self):

        self.url = "https://www.betano.bet.br/live/"



    def get_live_matches(self):


        jogos = []


        with sync_playwright() as p:


            browser = p.chromium.launch(
                headless=False
            )


            page = browser.new_page()


            try:


                page.goto(
                    self.url,
                    timeout=60000
                )


                page.wait_for_timeout(10000)



                texto = page.locator(
                    "body"
                ).inner_text()



                linhas = [

                    x.strip()

                    for x in texto.split("\n")

                    if x.strip()

                ]



                for i in range(len(linhas)-4):


                    horario = linhas[i]


                    if ":" not in horario:

                        continue



                    casa = linhas[i+1]

                    fora = linhas[i+2]

                    placar_casa = linhas[i+3]

                    placar_fora = linhas[i+4]



                    if not (
                        placar_casa.isdigit()
                        and placar_fora.isdigit()
                    ):

                        continue



                    nome_jogo = (
                        casa + " " + fora
                    ).lower()



                    # filtros

                    bloqueados = [

                        "esports",

                        "efootball",

                        "(f)",

                        "feminino",

                        "u17",

                        "u20",

                        "u21"

                    ]



                    if any(
                        x in nome_jogo
                        for x in bloqueados
                    ):

                        continue



                    if horario == "0:00":

                        continue



                    jogos.append({

                        "home": casa,

                        "away": fora,

                        "home_score": int(placar_casa),

                        "away_score": int(placar_fora),

                        "time": horario

                    })



            except Exception as e:


                print(
                    "Erro Betano:",
                    e
                )



            finally:


                browser.close()



        return jogos