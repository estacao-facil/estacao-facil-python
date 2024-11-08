from time import sleep
import text as t


# Constante global que define o tempo de espera (latência) para simular o tempo de resposta
LATENCY = 0.5  # Mantenha entre 0 e 1 (valores maiores podem tornar o sistema mais lento)


# Lista de estações disponíveis na linha de transporte
stations = [
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


# Dicionário que mapeia códigos de localização para descrições detalhadas de locais específicos nas estações
locations = {
    'BU-177': 'Entrada principal - Estação Butantã, próximo às catracas',
    'BU-810': 'Plataforma - Estação Butantã, lado sentido Luz',

    'PI-871': 'Plataforma - Estação Pinheiros, lado sentido Butantã',
    'PI-614': 'Entrada da estação - Estação Pinheiros, próximo à integração com a CPTM',

    'FA-673': 'Escadaria - Estação Faria Lima, saída para Av. Faria Lima',
    'FA-346': 'Plataforma - Estação Faria Lima, lado sentido Luz',

    'FR-411': 'Elevador - Estação Fradique Coutinho, acesso ao nível superior',
    'FR-762': 'Saída - Estação Fradique Coutinho, próximo à Rua dos Pinheiros',

    'OS-677': 'Corredor - Estação Oscar Freire, direção ao Hospital das Clínicas',
    'OS-620': 'Plataforma - Estação Oscar Freire, lado sentido Butantã',

    'PA-867': 'Saída - Estação Paulista, conexão com a linha verde',
    'PA-967': 'Plataforma - Estação Paulista, lado sentido Luz',

    'HI-197': 'Plataforma - Estação Higienópolis-Mackenzie, lado sentido Butantã',
    'HI-213': 'Bilheteria - Estação Higienópolis-Mackenzie, próximo ao guichê de informações',

    'RE-820': 'Bilheteria - Estação República, próxima ao guichê de informações',
    'RE-618': 'Plataforma - Estação República, lado sentido Luz',

    'LU-181': 'Plataforma - Estação Luz, conexão com a CPTM',
    'LU-143': 'Saída - Estação Luz, próximo ao Museu da Língua Portuguesa'
}


# Função para exibir uma mensagem com uma breve pausa para simular tempo de resposta
def display_cecilia_message(message):
    sleep(LATENCY)  # Aguarda o tempo especificado para simular latência

    print(t.cecilia_title)
    print(message)


# Função para solicitar uma opção do usuário, exibindo um título de solicitação
def request_user_option(user_title):
    sleep(LATENCY)  # Simula latência antes de solicitar a entrada

    option = input(user_title + " ")
    print()

    return option


# Função de onboarding para capturar o nome do usuário; se o campo estiver vazio, define como "Anônimo"
def onboarding():
    print(t.header)
    display_cecilia_message(t.welcome_message)

    username = request_user_option(t.undefined_title).strip().title()

    return username if username !="" else "Anônimo"


# Função que exibe o menu de informações e mantém o loop até que o usuário escolha uma opção válida
def information_menu(username):
    while True:
        display_cecilia_message(t.information_menu)
        option = request_user_option(t.user_title.format(username))
        
        match option:
            case "1": display_cecilia_message(t.alerts_notifications_message)  # Exibe alertas e notificações
            case "2": display_cecilia_message(t.operating_hours_message)  # Exibe horários de operação
            case "3": display_cecilia_message(t.fares_payment_message)  # Exibe tarifas e informações de pagamento
            case "4": display_cecilia_message(t.list_stations_message)  # Exibe lista de estações
            case "5": display_cecilia_message(t.about_team_message)  # Exibe informações sobre a equipe
            case "0": display_cecilia_message(t.cancel_operation_message)  # Cancela a operação
            case _:
                display_cecilia_message(t.invalid_input_message)  # Exibe mensagem de entrada inválida
                continue

        break


# Função para solicitar um índice de estação válido do usuário, garantindo que a entrada seja numérica e esteja dentro do intervalo permitido
def request_valid_station_index(message, username):
    while True:
        display_cecilia_message(message)
        station_index = request_user_option(t.user_title.format(username))

        if not station_index.isdigit() or int(station_index) <= 0 or int(station_index) > len(stations):
            display_cecilia_message(t.invalid_input_message)  # Exibe mensagem de entrada inválida se a entrada não for válida
            continue

        station_index = int(station_index) - 1
        return station_index


# Função que solicita as estações de partida e destino, e exibe um resumo da rota com a direção e quantidade de estações
def route_menu_option(username):
    departure_index = request_valid_station_index(t.departure_station_options, username)
    departure_station = stations[departure_index]
    display_cecilia_message(t.departure_confirmation_message.format(departure_station))

    destination_index = request_valid_station_index(t.destination_station_options, username)
    destination_station = stations[destination_index]
    display_cecilia_message(t.destination_confirmation_message.format(destination_station))

    # Verifica se a estação de partida é a mesma que a de destino e exibe uma mensagem se for o caso
    if departure_station == destination_station:
        display_cecilia_message(t.same_departure_destination_message)
        return
    
    # Determina a direção da rota e calcula o número de estações até o destino
    direction = "Butantã" if departure_index > destination_index else "Luz"
    stations_until_destination = abs(departure_index - destination_index)

    # Exibe o resumo da rota com as informações calculadas
    display_cecilia_message(t.route_summary_message.format(
        departure_station,
        destination_station,
        direction,
        stations_until_destination,
        destination_station
    ))


# Função para localizar uma posição específica em uma estação com base no código de localização fornecido pelo usuário
def location_menu_option(username):
    while True:
        display_cecilia_message(t.location_menu)
        option = request_user_option(t.user_title.format(username))
        location = locations.get(option)

        if location is None:
            display_cecilia_message(t.invalid_input_message)  # Exibe mensagem de entrada inválida se o código não for encontrado
            continue
        break

    # Exibe a descrição do local para o código de localização válido
    display_cecilia_message(t.location_result_message.format(location))


# Função principal que inicia o programa, realiza o onboarding e controla a navegação entre as opções do menu
def start():
    username = onboarding()  # Captura o nome do usuário

    first_iteration = True
    while True:
        # Exibe o menu de boas-vindas na primeira iteração, e o menu principal nas demais
        if first_iteration: 
            display_cecilia_message(t.welcome_menu.format(username))
        else: 
            display_cecilia_message(t.main_menu)

        option = request_user_option(t.user_title.format(username))
        match option:
            case "1": information_menu(username)  # Acessa o menu de informações
            case "2": route_menu_option(username)  # Calcula e exibe rota entre estações
            case "3": location_menu_option(username)  # Localiza posição específica dentro da estação
            case "0": 
                display_cecilia_message(t.farewell_message)  # Exibe mensagem de despedida
                break
            case _: 
                display_cecilia_message(t.invalid_input_message)  # Exibe mensagem para entrada inválida
                continue
            
        first_iteration = False


# Início do programa
if __name__ == "__main__":
    start()
