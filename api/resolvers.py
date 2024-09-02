import strawberry
from typing import List
from services.carga_dataset import DatasetService
from services.previsao_resultados import PrevisaoResultados

@strawberry.type
class Query:
    @strawberry.field
    def get_classificacao(self) -> List[dict]:
        service = DatasetService()
        return service.get_classificacao()

    @strawberry.field
    def previsao_resultados(self, rodada: int) -> List[dict]:
        service = PrevisaoResultados()
        return service.prever_resultados(rodada)
