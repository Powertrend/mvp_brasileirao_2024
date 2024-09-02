# Possíveis Problemas de Classificação com o Dataset

## 1. Previsão do Resultado da Partida (Vitória Mandante, Empate, Vitória Visitante)

**Objetivo:**  
Classificar o resultado de uma partida em três categorias: vitória do time mandante, empate ou vitória do time visitante.

**Classes:**  
- Vitória_Mandante
- Empate
- Vitória_Visitante

**Features:**
- Posição atual dos times na tabela
- Pontos
- Vitórias, Empates, Derrotas
- Saldo de Gols (SG)
- Gols Pró (GP) e Gols Contra (GC)
- Desempenho recente (últimos N jogos)
- Histórico de confrontos diretos
- Local do jogo (estádio, se há vantagem de jogar em casa)
- Data e Hora (dia da semana, horário)

## 2. Previsão de Rebaixamento ou Permanência na Série

**Objetivo:**  
Classificar se um time será rebaixado ou não até o final do campeonato.

**Classes:**  
- Rebaixado
- Não_Rebaixado

**Features:**
- Posição atual na tabela
- Pontos acumulados
- Jogos restantes
- Desempenho dos adversários diretos
- Saldo de Gols
- Histórico de rebaixamentos
- Desempenho em casa e fora

## 3. Previsão da Probabilidade de Título

**Objetivo:**  
Classificar se um time tem alta probabilidade de conquistar o título até o final do campeonato.

**Classes:**  
- Alta_Probabilidade
- Baixa_Probabilidade

**Features:**
- Posição atual
- Pontos acumulados
- Jogos restantes
- Desempenho recente
- Desempenho dos concorrentes diretos
- Histórico de conquistas de título

## 4. Classificação de Goleadores (Quem será o artilheiro)

**Objetivo:**  
Classificar quais jogadores têm maior probabilidade de se tornar artilheiros do campeonato.

**Classes:**  
- Artilheiro
- Não_Artilheiro

**Features:**
- Número de jogos disputados
- Gols marcados até o momento
- Média de gols por jogo
- Histórico de gols por temporada
- Participação nos jogos (minutos jogados)
- Lesões e suspensões

## Estrutura de Dados para Classificação

Para cada problema de classificação, é necessário definir claramente as features (variáveis independentes) e o target (variável dependente).

### Exemplo: Previsão do Resultado da Partida

#### 1. Coleta e Preparação dos Dados

- **Classificacao.csv:** Dados atuais das equipes.
- **Rodadas_Realizadas.csv:** Dados históricos de partidas realizadas.
- **Rodadas_Nao_Realizadas.csv:** Dados das partidas futuras a serem previstas.

#### 2. Engenharia de Features

**Combinação de Dados:**  
Unir os dados de classificação com os dados das partidas realizadas para obter informações completas sobre cada partida.

**Criação de Features:**
- Diferença de Pontos entre os times
- Diferença de Saldo de Gols
- Desempenho Recente: Média de pontos nas últimas 5 rodadas
- Histórico de Confrontos Diretos
- Local da Partida: Vantagem de jogar em casa
- Dia da Semana e Hora: Pode influenciar o desempenho

#### 3. Definição do Target

**Resultado da Partida:**  
Converter os placares em categorias (Vitória_Mandante, Empate, Vitória_Visitante).

#### 4. Tratamento de Dados Faltantes (NaN)

- **Estadio, Data, Dia e Hora:** Preencher valores faltantes com a moda ou usando técnicas de imputação apropriadas.
- **Placar_Mandante e Placar_Visitante:** Tratar entradas com 'X' (jogos adiados) removendo ou marcando de forma adequada.

#### 5. Divisão dos Dados

**Treino e Teste:**  
Utilizar `separacao_dados.py` para dividir os dados em conjuntos de treino e teste, mantendo a proporção adequada de classes.

## Implementação Orientada a Objetos com FastAPI e GraphQL

Vamos adaptar o código base para suportar a abordagem orientada a objetos e integrar a API com FastAPI e GraphQL.
