from pymongo import MongoClient
from services.carga_dataset import DatasetService

class MongoDBService:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['brasileirao2024']
        self.dataset_service = DatasetService()

    def importar_dados(self):
        classificacao = self.dataset_service.get_classificacao()
        realizadas = self.dataset_service.get_realizadas()
        nao_realizadas = self.dataset_service.get_nao_realizadas()
        
        self.db.classificacao.drop()
        self.db.realizadas.drop()
        self.db.nao_realizadas.drop()

        self.db.classificacao.insert_many(classificacao)
        self.db.realizadas.insert_many(realizadas)
        self.db.nao_realizadas.insert_many(nao_realizadas)

        print("Dados importados para o MongoDB.")
