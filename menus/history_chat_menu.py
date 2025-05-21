import os

from constants import PATH_HISTORY
import text as t
from utils import *


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
            case "1":
                restore_chat(username, session_messages)
            case "2":
                delete_chat(username, session_messages)
            case "3":
                delete_all_chats(username, session_messages)
            case "0":
                display_cecilia_message(t.cancel_operation_message, session_messages)
                break
            case _:
                display_cecilia_message(t.invalid_option_message, session_messages)
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
        display_cecilia_message(
            t.view_old_chat_options.format(list_history_chat), session_messages
        )

        option = request_user_option(t.user_title.format(username), session_messages)
        if not valid_positive_index(option, len(history_chat.keys())):
            display_cecilia_message(t.invalid_value_message, session_messages)
            continue

        break

    chat_index = int(option) - 1  # Converte para inteiro e ajusta o índice.
    chat_date, chat = list(history_chat.items())[chat_index]

    display_cecilia_message(
        t.view_old_chat_message.format(chat_date, chat), session_messages
    )


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
        display_cecilia_message(
            t.view_old_chat_delete_options.format(list_history_chat), session_messages
        )

        option = request_user_option(t.user_title.format(username), session_messages)
        if not valid_positive_index(option, len(history_chat.keys())):
            display_cecilia_message(t.invalid_value_message, session_messages)
            continue

        break

    chat_index = int(option) - 1  # Converte para inteiro e ajusta o índice.
    key = list(history_chat.keys())[chat_index]

    # Solicita confirmação do usuário para exclusão.
    user_confirmation = request_user_confirmation(
        t.user_title.format(username),
        t.delete_chat_confirm_message.format(key),
        session_messages,
    )
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
    user_confirmation = request_user_confirmation(
        t.user_title.format(username),
        t.delete_all_chats_confirm_message,
        session_messages,
    )
    if not user_confirmation:
        display_cecilia_message(t.operation_cancelled_message, session_messages)
        return

    if os.path.exists(PATH_HISTORY):
        os.remove(PATH_HISTORY)
    display_cecilia_message(t.all_chats_deleted_message, session_messages)
