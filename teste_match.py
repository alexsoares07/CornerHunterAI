from providers.betano_provider import BetanoProvider
from services.match_matcher import MatchMatcher


betano = BetanoProvider()

matcher = MatchMatcher()


# pega jogos da Betano

jogos_betano = betano.get_live_matches()


print("\nJOGOS BETANO:")
for jogo in jogos_betano[:5]:
    print(jogo)



# teste simulando jogos do SofaScore
# depois vamos ligar direto no scanner

jogos_sofa = [

    {
        "match": "Torque II x Nacional Montevideo II"
    },

    {
        "match": "CS Limpeno x Club Silvio Pettirossi"
    }

]



resultado = matcher.find_matches(
    jogos_betano,
    jogos_sofa
)



print("\n====================")
print("MATCHES ENCONTRADOS")
print("====================")


for item in resultado:

    print("----------------")

    print("BETANO:")
    print(item["betano"])

    print("SOFASCORE:")
    print(item["sofa"])