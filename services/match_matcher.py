import unicodedata
import re



class MatchMatcher:



    def normalize(self, texto):


        texto = texto.lower()



        texto = unicodedata.normalize(
            "NFKD",
            texto
        ).encode(
            "ascii",
            "ignore"
        ).decode()



        substituicoes = {


            "club": "",

            "fc": "",

            "fbc": "",

            "sportivo": "",

            "sport": "",

            "de": "",

            "ii": "",

            "reserve": "",

            "reserves": "",

            "b": "",

        }



        for antigo, novo in substituicoes.items():

            texto = texto.replace(
                antigo,
                novo
            )



        texto = re.sub(
            r"[^a-z0-9]",
            "",
            texto
        )



        return texto




    def team_similarity(self, a, b):


        a = self.normalize(a)

        b = self.normalize(b)



        # um nome dentro do outro

        if a in b or b in a:

            return True



        # compara começo do nome

        tamanho = min(
            len(a),
            len(b)
        )


        if tamanho >= 5:


            if a[:5] == b[:5]:

                return True



        return False





    def compare(self, betano_game, sofa_game):


        sofa_match = sofa_game["match"]



        sofa_parts = sofa_match.split(
            " x "
        )


        if len(sofa_parts) != 2:

            return False



        sofa_home = sofa_parts[0]

        sofa_away = sofa_parts[1]



        home_ok = self.team_similarity(

            betano_game["home"],

            sofa_home

        )



        away_ok = self.team_similarity(

            betano_game["away"],

            sofa_away

        )



        return (
            home_ok
            and
            away_ok
        )





    def find_matches(self, betano_games, sofa_games):


        encontrados = []



        for bet in betano_games:


            for sofa in sofa_games:


                if self.compare(
                    bet,
                    sofa
                ):


                    encontrados.append({

                        "betano": bet,

                        "sofa": sofa

                    })



        return encontrados