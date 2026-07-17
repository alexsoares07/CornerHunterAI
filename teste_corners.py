from providers.sofascore_provider import SofaScoreProvider


provider = SofaScoreProvider()


resultado = provider.get_corners(16326400)


print(resultado)