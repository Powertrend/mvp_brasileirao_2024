from sklearn.model_selection import train_test_split

class DadosService:
    def __init__(self, dataset):
        self.dataset = dataset

    def separar_dados(self, test_size=0.2):
        treino, teste = train_test_split(self.dataset, test_size=test_size)
        treino.to_csv('dataset/treino.csv', index=False)
        teste.to_csv('dataset/teste.csv', index=False)
        print("Dados separados e salvos em treino.csv e teste.csv.")
