import strawberry
from app.model_service import PredictionService

# Crie uma instância do serviço de predição
prediction_service = PredictionService()

@strawberry.type
class Query:
    @strawberry.field
    def predict(self, mandante: str, visitante: str) -> str:
        """
        Recebe dois times como entrada e retorna a predição do resultado.
        """
        return prediction_service.predict(mandante, visitante)

# Cria o schema com a consulta
schema = strawberry.Schema(query=Query)
