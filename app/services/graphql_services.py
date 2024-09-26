"""Serviço preparação dos Dados Para o modelo treinado

    Returns:
        _type_: Service
    """
from app.services.model_service import ModelService
from models.input_data import InputData


class GraphQLService:
    """Classe principal
    """

    def __init__(self):
        self.model_service = ModelService()

    def predict_match(self, mandante, visitante, pos_mandante, pos_visitante):
        """Prepara os dados e faz a predição usando o model service

        Args:
            mandante (_type_): Um Clube
            visitante (_type_): Um Clube
            pos_mandante (_type_): Classificação do Clube
            pos_visitante (_type_):Classificação do Clube

        Returns:
            _type_: Resultado previsto
        """
        input_data = InputData(
            Mandante=mandante,
            Visitante=visitante,
            Posicao_Mandante=pos_mandante,
            Posicao_Visitante=pos_visitante
        )
        input_data_scaled = self.model_service.preprocess_input(input_data)
        return self.model_service.predict(input_data_scaled)
