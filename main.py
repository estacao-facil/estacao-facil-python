import os

import text as t
from utils import *
from constants import STATIONS, LOCATIONS, PATH_HISTORY


# MENU: Início
def home_menu(username, session_messages):
    """
    Exibe o menu principal (início) e direciona o usuário para outras funcionalidades
    com base na opção escolhida. O menu continua em loop até o usuário optar por sair.
    """
    first_iteration = True
    while True:
        if first_iteration:
            display_cecilia_message(t.welcome_menu.format(username), session_messages)
        else:
            display_cecilia_message(t.main_menu, session_messages)

        option = request_user_option(t.user_title.format(username), session_messages)
        match option:
            case "1": information_menu(username, session_messages)
            case "2": route_menu(username, session_messages)
            case "3": location_menu(username, session_messages)
            case "4": history_chat_menu(username, session_messages)
            case "0":
                # Exibe mensagem de despedida e encerra o loop.
                display_cecilia_message(t.farewell_message, session_messages)
                break
            case _: display_cecilia_message(t.invalid_input_message, session_messages)  # Caso a opção seja inválida, exibe mensagem de erro.

        first_iteration = False  # Após a primeira execução, o menu padrão é exibido.


def onboarding(session_messages):
    """
    Função responsável pelo onboarding do usuário:
    - Exibe o cabeçalho e mensagem de boas-vindas.
    - Solicita o nome do usuário e trata a entrada, retornando um nome válido.
    """
    print(t.header)
    display_cecilia_message(t.welcome_message, session_messages)

    username = request_user_option(t.undefined_title, session_messages).strip().title()
    return username or "Usuário Anônimo"  # Caso o usuário não informe um nome, utiliza "Usuário Anônimo".


# MENU: Obter Informações
def information_menu(username, session_messages):
    """
    Menu que exibe diferentes tipos de informações:
    - Alertas e notificações.
    - Horários de funcionamento.
    - Tarifas e formas de pagamento.
    - Lista de estações.
    - Informações sobre a equipe.
    - Opção de cancelar.
    """
    while True:
        display_cecilia_message(t.information_menu, session_messages)

        option = request_user_option(t.user_title.format(username), session_messages)
        match option:
            case "1": display_cecilia_message(t.alerts_notifications_message, session_messages)
            case "2": display_cecilia_message(t.operating_hours_message, session_messages)
            case "3": display_cecilia_message(t.fares_payment_message, session_messages)
            case "4": display_cecilia_message(t.list_stations_message, session_messages)
            case "5": display_cecilia_message(t.about_team_message, session_messages)
            case "0": display_cecilia_message(t.cancel_operation_message, session_messages)
            case _:
                display_cecilia_message(t.invalid_input_message, session_messages)
                continue  # Se a opção for inválida, repete o loop.
        
        break  # Encerra o loop após uma opção válida ser processada.


# MENU: Traçar Rotas entre Estações
def route_menu(username, session_messages):
    """
    Função para o menu de traçar rotas entre estações.
    Solicita ao usuário a estação de partida e de destino, valida a escolha e exibe um resumo da rota.
    """
    # Solicita e valida o índice da estação de partida.
    departure_index = request_station_index(username, t.departure_station_options, session_messages)
    departure_station = STATIONS[departure_index]
    display_cecilia_message(t.departure_confirmation_message.format(departure_station), session_messages)

    # Solicita e valida o índice da estação de destino.
    destination_index = request_station_index(username, t.destination_station_options, session_messages)
    destination_station = STATIONS[destination_index]
    display_cecilia_message(t.destination_confirmation_message.format(destination_station), session_messages)

    # Se a estação de partida for igual à de destino, exibe mensagem de erro e retorna.
    if departure_station == destination_station:
        display_cecilia_message(t.same_departure_destination_message, session_messages)
        return
    
    # Determina a direção com base na posição das estações na lista.
    direction = "Butantã" if departure_index > destination_index else "Luz"
    stations_until_destination = abs(departure_index - destination_index)

    # Exibe o resumo da rota com os detalhes da viagem.
    display_cecilia_message(t.route_summary_message.format(
        departure_station,
        destination_station,
        direction,
        stations_until_destination,
        destination_station,
    ), session_messages)


def request_station_index(username, message, session_messages):
    """
    Função que solicita ao usuário um índice correspondente à estação desejada.
    Verifica se a entrada é um número válido e retorna o índice (ajustado para zero-based).
    """
    while True:
        display_cecilia_message(message, session_messages)
        
        option = request_user_option(t.user_title.format(username), session_messages)
        if not valid_positive_index(option, len(STATIONS)):
            display_cecilia_message(t.invalid_input_message, session_messages)
            continue
        
        return int(option) - 1  # Converte para inteiro e ajusta o índice.


# MENU: Localizar-se
def location_menu(username, session_messages):
    """
    Menu que solicita ao usuário a opção de localização e exibe a descrição da localização selecionada.
    """
    while True:
        display_cecilia_message(t.location_menu, session_messages)

        option = request_user_option(t.user_title.format(username), session_messages)
        if not option in LOCATIONS.keys():
            display_cecilia_message(t.invalid_input_message, session_messages)
            continue
        
        break

    location = LOCATIONS[option]
    display_cecilia_message(t.location_result_message.format(location), session_messages)


# MENU: Histórico de Conversas
def history_chat_menu(username, session_messages):
    """
    Menu para gerenciar o histórico de conversas, permitindo:
    - Restaurar uma conversa.
    - Excluir uma conversa específica.
    - Excluir todas as conversas.
    - Cancelar a operação.
    """
    while True:
        display_cecilia_message(t.history_chat_menu, session_messages)

        option = request_user_option(t.user_title.format(username), session_messages)
        match option:
            case "1": restore_chat(username, session_messages)
            case "2": delete_chat(username, session_messages)
            case "3": delete_all_chats(username, session_messages)
            case "0":
                display_cecilia_message(t.cancel_operation_message, session_messages)
                break
            case _:
                display_cecilia_message(t.invalid_input_message, session_messages)
                continue

        break  # Sai do loop após uma operação válida.


def restore_chat(username, session_messages):
    """
    Restaura uma conversa antiga:
    - Obtém o histórico salvo.
    - Exibe uma lista numerada das sessões salvas.
    - Solicita ao usuário que escolha uma sessão para visualização.
    - Exibe a conversa escolhida.
    """
    history_chat = get_history_chat()
    list_history_chat = get_list_history_chat(history_chat)

    if not history_chat:
        display_cecilia_message(t.no_chat_history_message, session_messages)
        return
    
    while True:
        display_cecilia_message(t.view_old_chat_options.format(list_history_chat), session_messages)

        option = request_user_option(t.user_title.format(username), session_messages)
        if not valid_positive_index(option, len(history_chat.keys())):
            display_cecilia_message(t.invalid_input_message, session_messages)
            continue

        break

    chat_index = int(option) - 1  # Converte para inteiro e ajusta o índice.
    chat_date, chat = list(history_chat.items())[chat_index]

    display_cecilia_message(t.view_old_chat_message.format(chat_date, chat), session_messages)
        

def delete_chat(username, session_messages):
    """
    Exclui uma conversa específica:
    - Exibe a lista de conversas salvas.
    - Solicita a escolha da conversa a ser deletada.
    - Pede confirmação do usuário.
    - Remove a conversa selecionada e atualiza o arquivo de histórico.
    """
    history_chat = get_history_chat()
    list_history_chat = get_list_history_chat(history_chat)

    if not history_chat:
        display_cecilia_message(t.no_chat_history_message, session_messages)
        return

    while True:
        display_cecilia_message(t.view_old_chat_delete_options.format(list_history_chat), session_messages)

        option = request_user_option(t.user_title.format(username), session_messages)
        if not valid_positive_index(option, len(history_chat.keys())):
            display_cecilia_message(t.invalid_input_message, session_messages)
            continue

        break

    chat_index = int(option) - 1  # Converte para inteiro e ajusta o índice.
    key = list(history_chat.keys())[chat_index]

    # Solicita confirmação do usuário para exclusão.
    user_confirmation = request_user_confirmation(t.user_title.format(username), t.delete_chat_confirm_message.format(key), session_messages)
    if not user_confirmation:
        display_cecilia_message(t.operation_cancelled_message, session_messages)
        return
        
    # Remove o chat do histórico e atualiza o arquivo JSON.
    history_chat.pop(key)
    with open(PATH_HISTORY, "w") as file:
        file.write(json.dumps(history_chat))

    display_cecilia_message(t.chat_deleted_message.format(key), session_messages)


def delete_all_chats(username, session_messages):
    """
    Exclui todas as conversas salvas:
    - Solicita confirmação do usuário.
    - Caso confirmado, remove o arquivo de histórico.
    """
    user_confirmation = request_user_confirmation(t.user_title.format(username), t.delete_all_chats_confirm_message, session_messages)
    if not user_confirmation:
        display_cecilia_message(t.operation_cancelled_message, session_messages)
        return
    
    if os.path.exists(PATH_HISTORY): os.remove(PATH_HISTORY)
    display_cecilia_message(t.all_chats_deleted_message, session_messages)


# Início do Fluxo da Aplicação
def start():
    """
    Função principal que inicia o fluxo da aplicação.
    - Realiza o onboarding do usuário.
    - Exibe o menu principal.
    - Salva o histórico de mensagens da sessão.
    - Trata interrupções (como Ctrl+C) e exceções inesperadas.
    """
    try:
        messages = []  # Lista para armazenar todas as mensagens e interações da sessão.
        username = onboarding(messages)

        home_menu(username, messages)
        save_chat(messages)
    except KeyboardInterrupt:
        # Caso o usuário interrompa a execução (Ctrl+C), exibe mensagem de despedida e salva o chat.
        display_cecilia_message(t.farewell_message, messages)
        save_chat(messages)
    except:
        # Em caso de exceção inesperada, salva o chat e relança a exceção.
        save_chat(messages)
        raise


if __name__ == "__main__":
    start()
    