from sofascore_api import SofaScoreClient


sofa = SofaScoreClient()


event_id = 16326400


estatisticas = sofa.get_event_statistics(event_id)


print(estatisticas)