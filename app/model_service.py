import joblib
import numpy as np

class PredictionService:
    def __init__(self):
        # Carregar o modelo treinado e os objetos necessários
        self.model = joblib.load('app/models/modelo_treinado.pkl')
        self.label_encoder = joblib.load('app/models/label_encoder.pkl')
        self.scaler = joblib.load('app/models/scaler.pkl')
        # self.resultado_encoder = joblib.load('app/models/resultado_encoder.pkl')  # Se aplicável

    def predict(self, mandante: str, visitante: str) -> str:
        # Codificar os times
        time_mandante_cod = self.label_encoder.transform([mandante])
        time_visitante_cod = self.label_encoder.transform([visitante])

        # Criar o array de features
        features = np.array([[time_mandante_cod[0], time_visitante_cod[0]]])

        # Escalonar os dados
        features_scaled = self.scaler.transform(features)

        # Fazer a predição
        predicao = self.model.predict(features_scaled)

        # Inverter a codificação do resultado
        # resultado_previsto = self.resultado_encoder.inverse_transform(predicao)

        # return resultado_previsto[0]
        return predicao[0]
