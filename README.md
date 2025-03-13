# Estação Fácil

**Estação Fácil** é uma aplicação de assistente virtual desenvolvida em Python para ajudar passageiros do metrô de São Paulo. Cecília, nossa IA conversacional, fornece informações e orientações de maneira natural e descontraída, tornando sua experiência de viagem mais simples e agradável.

## Funcionalidades

- **Obter Informações:**

  - Alertas e notificações sobre a linha.
  - Horários de funcionamento.
  - Tarifas e formas de pagamento.
  - Lista de estações.
  - Informações sobre a equipe de desenvolvimento.

- **Traçar Rotas:**

  - Ajuda a definir a estação de partida e destino.
  - Informa o sentido e a quantidade de estações até o destino.

- **Localizar-se:**

  - Permite identificar a sua localização a partir de códigos encontrados próximos a QR Codes nas estações.

- **Histórico de Conversas:**
  - Visualização, exclusão e gerenciamento do histórico de interações com Cecília.

## Tecnologias Utilizadas

- **Python 3**  
  A aplicação foi construída utilizando apenas bibliotecas padrão do Python, como `os`, `json`, `datetime` e `time`.

## Estrutura do Projeto

```
├── main.py          # Arquivo principal que inicia o fluxo da aplicação.
├── utils.py         # Funções auxiliares para exibição de mensagens, entrada de dados e manipulação do histórico.
├── constants.py     # Definição de constantes (estações, localizações, latência, etc.).
└── text.py          # Textos e mensagens exibidos pela assistente Cecília.
```

## Como Executar

1. **Pré-requisitos:**

   - Certifique-se de ter o Python 3 instalado em sua máquina.
   - O projeto não utiliza dependências externas, usando apenas as bibliotecas padrão do Python.

2. **Clone o repositório:**

   ```bash
   git clone https://github.com/estacao-facil/estacao-facil-python.git
   cd estacao-facil-python
   ```

3. **Execute a aplicação:**

   ```bash
   python main.py
   ```

4. **Utilização:**  
   Siga as instruções exibidas na tela. Cecília irá guiá-lo(a) através das opções disponíveis para que você possa obter informações, traçar rotas, localizar-se e gerenciar seu histórico de conversas.

## Projeto Desenvolvido por:

- **Angelo Antonio Recke Ricieri**
- **Antonio de Luca Ribeiro Silva**
- **Paulo Sérgio França Barbosa**
