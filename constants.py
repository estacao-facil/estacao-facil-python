# Define o tempo de latência (delay) para as operações, em segundos.
LATENCY = 0.5  # Mantenha entre 0 e 1 (valores maiores podem tornar o sistema extremamente lento)

# Lista de estações disponíveis para o sistema.
STATIONS = [
    "Butantã",
    "Pinheiros",
    "Faria Lima",
    "Fradique Coutinho",
    "Oscar Freire",
    "Paulista",
    "Higienópolis-Mackenzie",
    "República",
    "Luz",
]

# Dicionário que relaciona códigos de localização com suas descrições.
LOCATIONS = {
    "BU-177": "Entrada principal - Estação Butantã, próximo às catracas",
    "BU-810": "Plataforma - Estação Butantã, lado sentido Luz",
    "PI-871": "Plataforma - Estação Pinheiros, lado sentido Butantã",
    "PI-614": "Entrada da estação - Estação Pinheiros, próximo à integração com a CPTM",
    "FA-673": "Escadaria - Estação Faria Lima, saída para Av. Faria Lima",
    "FA-346": "Plataforma - Estação Faria Lima, lado sentido Luz",
    "FR-411": "Elevador - Estação Fradique Coutinho, acesso ao nível superior",
    "FR-762": "Saída - Estação Fradique Coutinho, próximo à Rua dos Pinheiros",
    "OS-677": "Corredor - Estação Oscar Freire, direção ao Hospital das Clínicas",
    "OS-620": "Plataforma - Estação Oscar Freire, lado sentido Butantã",
    "PA-867": "Saída - Estação Paulista, conexão com a linha verde",
    "PA-967": "Plataforma - Estação Paulista, lado sentido Luz",
    "HI-197": "Plataforma - Estação Higienópolis-Mackenzie, lado sentido Butantã",
    "HI-213": "Bilheteria - Estação Higienópolis-Mackenzie, próximo ao guichê de informações",
    "RE-820": "Bilheteria - Estação República, próxima ao guichê de informações",
    "RE-618": "Plataforma - Estação República, lado sentido Luz",
    "LU-181": "Plataforma - Estação Luz, conexão com a CPTM",
    "LU-143": "Saída - Estação Luz, próximo ao Museu da Língua Portuguesa",
}

# Caminho do arquivo que armazena o histórico de conversas.
PATH_HISTORY = "chats.json"

# Database
DB_URL = ""
DB_USER = ""
DB_PASSWORD = ""

# Open Weather
OPEN_WEATHER_API_KEY = ""
