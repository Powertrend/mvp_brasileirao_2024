"""Modelo Treinado, encoder, scaler, resultado_encoder

    Returns:
        _type_: Embarca o modelo e executa a predição
    """

import os
import joblib

import numpy as np

from models.input_data import InputData


class ModelService:
    """Classe responsável por carregar o modelo embarcar ele no código
    """

    def __init__(self):
        """Carregar o modelo e objetos relacionados
        """
        self.model_path = os.path.join(
            os.path.dirname(__file__), '../../models')
        print("Caminho do model", self.model_path)
        self.model = joblib.load(os.path.join(
            self.model_path, 'modelo_treinado.pkl'))
        self.label_encoder = joblib.load(
            os.path.join(self.model_path, 'label_encoder.pkl'))
        self.scaler = joblib.load(os.path.join(self.model_path, 'scaler.pkl'))
        self.resultado_encoder = joblib.load(
            os.path.join(self.model_path, 'resultado_encoder.pkl'))

    def preprocess_input(self, data: InputData):
        """Codificando os times

        Args:
            data (InputData): Times

        Returns:
            _type_: Calculos e pradonização de dados
        """
        time_mandante_cod = self.label_encoder.transform([data.Mandante])[0]
        time_visitante_cod = self.label_encoder.transform([data.Visitante])[0]

        # Calculando a diferença de posição
        diferenca_posicao = data.Posicao_Mandante - data.Posicao_Visitante

        # Criando o array de entrada
        input_data = np.array([[time_mandante_cod, time_visitante_cod,
                                data.Posicao_Mandante, data.Posicao_Visitante,
                                diferenca_posicao]])

        # Escalonando os dados
        input_data_scaled = self.scaler.transform(input_data)

        return input_data_scaled

    def predict(self, input_data_scaled):
        """Fazer a predição

        Args:
            input_data_scaled (_type_): _description_

        Returns:
            _type_: _description_
        """
        predicao = self.model.predict(input_data_scaled)
        return self.resultado_encoder.inverse_transform(predicao)[0]
