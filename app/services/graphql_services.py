# app/services/graphql_service.py
from app.services.model_service import ModelService
from models.input_data import InputData

class GraphQLService:
    def __init__(self):
        self.model_service = ModelService()

    def predict_match(self, mandante, visitante, posMandante, posVisitante):
        # Prepara os dados e faz a predição usando o model service
        input_data = InputData(
            Mandante=mandante,
            Visitante=visitante,
            Posicao_Mandante=posMandante,
            Posicao_Visitante=posVisitante
        )
        input_data_scaled = self.model_service.preprocess_input(input_data)
        return self.model_service.predict(input_data_scaled)
