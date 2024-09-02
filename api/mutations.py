import strawberry
from services.importacao_mongodb import MongoDBService

@strawberry.type
class Mutation:
    @strawberry.mutation
    def importar_dados(self) -> str:
        service = MongoDBService()
        service.importar_dados()
        return "Dados importados para o MongoDB com sucesso!"
