from providers.sofascore_provider import SofaScoreProvider

provider = SofaScoreProvider()

event_id = 16326400

stats = provider.get_statistics_map(event_id)

print("\nTOTAL DE ESTATÍSTICAS:", len(stats))

print("\nCHAVES DISPONÍVEIS:\n")

for key in stats.keys():
    print(key)