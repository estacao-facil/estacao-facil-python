from datetime import datetime
import json
from json.decoder import JSONDecodeError
from time import sleep

from constants import LATENCY, PATH_HISTORY
import text as t


def display_cecilia_message(message, session_messages):
    """
    Exibe uma mensagem formatada com o título "Cecília" e registra a mensagem na lista de sessão.
    Adiciona um delay (latência) para simular processamento.
    """
    sleep(LATENCY)

    # Concatena o título e a mensagem, separando por uma quebra de linha.
    content = "\n".join((t.cecilia_title, message))
    print(content)

    session_messages.append(content)


def request_user_option(user_title, session_messages):
    """
    Solicita uma entrada do usuário (opção) com base no título fornecido.
    Registra a entrada na lista de mensagens da sessão.
    """
    sleep(LATENCY)

    option = input(f"{user_title} ")
    print()

    # Registra a opção informada pelo usuário.
    content = "\n".join((f"{user_title} {option}", ""))
    session_messages.append(content)

    return option


def request_user_confirmation(user_title, message, session_messages):
    """
    Solicita uma confirmação do usuário (S/N).
    Repete a solicitação até que o usuário informe uma resposta válida.
    Retorna True para "S" e False para "N".
    """
    while True:
        display_cecilia_message(message, session_messages)

        option = request_user_option(user_title, session_messages)
        match option.upper():
            case "S": return True
            case "N": return False
            case _:
                display_cecilia_message(t.invalid_input_message, session_messages)
                continue


def valid_positive_index(input, elements_amount):
    """
    Verifica se a entrada é um número válido (dígito) e se está no intervalo permitido (1 até a quantidade de elementos).
    Retorna True se for válida, caso contrário, False.
    """
    if not input.isdigit():
        return False
    if not 0 < int(input) <= elements_amount:
        return False

    return True


def save_chat(session_messages):
    """
    Salva o histórico da sessão (todas as mensagens) em um arquivo JSON.
    - Gera um ID de sessão baseado na data e hora atual.
    - Adiciona a sessão ao histórico e escreve no arquivo.
    """
    session_id = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    session_messages = "\n".join(map(str, session_messages))

    # Obtém o histórico de chats já salvos.
    history_chat = get_history_chat()
    history_chat[session_id] = session_messages
    with open(PATH_HISTORY, "w") as file:
        json_data = json.dumps(history_chat)
        file.write(json_data)


def get_history_chat():
    """
    Lê o arquivo de histórico de chats e retorna um dicionário com as sessões salvas.
    Se o arquivo não existir ou estiver corrompido, retorna um dicionário vazio.
    """
    try:
        with open(PATH_HISTORY, "r") as file:
            json_data = file.read()
            return json.loads(json_data or "{}")
    except (FileNotFoundError, JSONDecodeError):
        return {}


def get_list_history_chat(history_chat):
    """
    Formata o dicionário de histórico de chats em uma lista numerada de sessões para exibição.
    """
    return "\n".join([
        t.saved_chat_list_item.format(i, key)
        for i, key in enumerate(history_chat.keys(), 1)
    ])
