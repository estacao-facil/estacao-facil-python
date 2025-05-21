import text as t
from utils import *

from menus.check_weather_menu import check_weather_menu
from menus.history_chat_menu import history_chat_menu
from menus.information_menu import information_menu
from menus.location_menu import location_menu
from menus.manage_alerts_menu import manage_alerts_menu
from menus.route_menu import route_menu


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
            case "1":
                information_menu(username, session_messages)
            case "2":
                route_menu(username, session_messages)
            case "3":
                location_menu(username, session_messages)
            case "4":
                manage_alerts_menu(username, session_messages)
            case "5":
                check_weather_menu(username, session_messages)
            case "6":
                history_chat_menu(username, session_messages)
            case "0":
                # Exibe mensagem de despedida e encerra o loop.
                display_cecilia_message(t.farewell_message, session_messages)
                break
            case _:
                display_cecilia_message(
                    t.invalid_option_message, session_messages
                )  # Caso a opção seja inválida, exibe mensagem de erro.

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
    return (
        username or "Usuário Anônimo"
    )  # Caso o usuário não informe um nome, utiliza "Usuário Anônimo".


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
