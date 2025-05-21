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

- **Verificar Clima:**

  - Consulta o clima atual de qualquer bairro da cidade de São Paulo.
  - Ideal para planejar a saída de casa ou o deslocamento até a estação de destino.

- **Gerenciar Alertas:**

  - Visualizar todos os alertas registrados no sistema.
  - Aplicar filtros para exibir alertas por ID, status, estação ou data.
  - Criar novos alertas.
  - Atualizar alertas existentes.
  - Remover alertas com confirmação.
  - Exportar alertas em formato `.json`.

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

3. **Instale as dependências:**

   Apesar de grande parte do projeto utilizar apenas bibliotecas nativas do Python, algumas funcionalidades específicas dependem de bibliotecas externas.
   Para garantir o funcionamento completo da aplicação, instale as bibliotecas a seguir:

   ```bash
   pip install requests oracledb
   ```

   - `requests`: utilizada para realizar chamadas à API do OpenWeather.
   - `oracledb`: necessária para conectar ao banco de dados Oracle.

   > 💡 Dica: você pode usar o arquivo `requirements.txt` com as bibliotecas utilizadas e instalar tudo de uma vez:

   ```bash
   pip install -r requirements.txt
   ```

4. **Execute a aplicação:**

   ```bash
   python main.py
   ```

5. **Utilização:**  
   Siga as instruções exibidas na tela. Cecília irá guiá-lo(a) através das opções disponíveis para que você possa obter informações, traçar rotas, localizar-se e gerenciar seu histórico de conversas.

⚠️ **Importante:**
Antes de executar a aplicação, é necessário preencher as credenciais no arquivo `constants.py`, localizado na raiz do projeto.
Esse arquivo contém campos reservados para dados sensíveis como conexão com o banco de dados Oracle e a chave da API do OpenWeather.

### Exemplo de configuração:

```python
# constants.py

# Database
DB_URL = ""       # Exemplo: "localhost/orclpdb1"
DB_USER = ""      # Exemplo: "admin"
DB_PASSWORD = ""  # Exemplo: "123456"

# Open Weather
OPEN_WEATHER_API_KEY = ""  # Exemplo: "abc123def456ghi789"
```

## Projeto Desenvolvido por:

- **Angelo Antonio Recke Ricieri**
- **Antonio de Luca Ribeiro Silva**
- **Paulo Sérgio França Barbosa**
