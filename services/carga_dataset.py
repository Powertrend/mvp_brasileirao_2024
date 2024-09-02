import pandas as pd

class DatasetService:
    def __init__(self):
        self.classificacao = pd.read_csv('dataset/Classificacao.csv')
        self.realizadas = pd.read_csv('dataset/Rodadas_Realizadas.csv')
        self.nao_realizadas = pd.read_csv('dataset/Rodadas_Nao_Realizadas.csv')

    def get_classificacao(self):
        return self.classificacao.to_dict('records')
    
    def get_realizadas(self):
        return self.realizadas.to_dict('records')
    
    def get_nao_realizadas(self):
        return self.nao_realizadas.to_dict('records')
