<p align="center">
  <img src="/assets/images/brasileiro-serie-a.png" alt="Logo Brasileirão 2024">
</p>

# Predict - Predição de Jogos Brasileirão 2024 ⚽

O Predict é uma aplicação backend que embarca um modelo de machine learning treinado em um notebook google colab.

O front-end da aplicação pode ser encontrado no seguinte repositório: [https://github.com/Powertrend/front_end_mvp_brasileirao_2024](https://github.com/Powertrend/front_end_mvp_brasileirao_2024)

## Funcionalidades 🤖

-   Disponibilizar uma rota API GRaphQl para executar a predição.



## Instalação 📦

Requer o [Python 3](https://www.python.org/downloads/) instalado para rodar.

Para usar o Predict, siga estes passos:

1. Clone o repositório para a sua máquina.
2. Crie um ambiente virtual executando `python3 -m venv .venv` no terminal.
3. Ative o ambiente virtual executando `source .venv/bin/activate`.
4. Instale as dependências necessárias executando `pip install -r requirements.txt`.
5. Inicie o servidor back-end executando `uvicorn main:app --reload` no terminal. Isso iniciará o servidor Flask em `http://localhost:8000`.

## Uso

Inicie back-end e pronto sua API com o modelo treinado estará rodando, se quiser testar a API, acesse `http://localhost:8000/graphql` e execute a query : 

query {
    predictMatch(mandante: "Cruzeiro", visitante: "Flamengo", posMandante: 15, posVisitante: 8)
}

## Contribuindo

Se você gostaria de contribuir com o Predict, abra um pull request ou uma issue no repositório do GitHub.