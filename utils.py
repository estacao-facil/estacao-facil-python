from datetime import datetime
import json
from json.decoder import JSONDecodeError
from prompt_toolkit import prompt
import re
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


def request_user_option(user_title, session_messages, default=""):
    """
    Solicita uma entrada do usuário (opção) com base no título fornecido.
    Registra a entrada na lista de mensagens da sessão.
    """
    sleep(LATENCY)

    option = prompt(f"{user_title} ", default=str(default))
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
            case "S":
                return True
            case "N":
                return False
            case _:
                display_cecilia_message(t.invalid_option_message, session_messages)
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
    return "\n".join(
        [
            t.saved_chat_list_item.format(i, key)
            for i, key in enumerate(history_chat.keys(), 1)
        ]
    )


def extract_alert(raw_alert):
    """
    Converte uma tupla de dados de alerta (vinda do banco) em um dicionário estruturado.
    Facilita o uso e a exibição das informações no sistema.
    """
    return {
        "id": raw_alert[0],
        "title": raw_alert[1],
        "description": raw_alert[2],
        "start_time": raw_alert[3],
        "end_time": raw_alert[4],
        "station": raw_alert[5],
        "severity_id": raw_alert[6],
        "severity": raw_alert[7],
        "severity_level": raw_alert[8],
    }


def extract_severity(raw_severity):
    """
    Converte uma tupla de severidade em um dicionário.
    Utilizado principalmente para exibir as opções de severidade de forma clara.
    """
    return {
        "id": raw_severity[0],
        "description": raw_severity[1],
        "severity_level": raw_severity[2],
    }


def alert_str(alert):
    """
    Gera uma string formatada com os dados principais de um alerta.
    Utilizada para listagens simplificadas de alertas (ex: listagem de todos os alertas).
    """
    status = "Encerrado" if alert["end_time"] else "Ativo"

    return t.alert_short_str.format(
        alert["id"],
        alert["title"],
        alert["station"],
        alert["severity"],
        alert["start_time"].strftime("%d/%m/%Y %H:%M"),
        status,
    )


def severity_option_str(severity):
    """
    Gera uma string com o ID e a descrição da severidade, usada em menus de seleção.
    """
    return t.severity_option_str.format(severity["id"], severity["description"])


def get_valid_date(
    request_message, username, session_messages, required=True, default=""
):
    """
    Solicita ao usuário uma data no formato DD-MM-AAAA.
    - Valida o formato usando regex.
    - Converte a string para um objeto datetime.
    - Pode aceitar valor vazio se 'required' for False.
    """
    pattern = r"^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-\d{4}$"

    while True:
        display_cecilia_message(request_message, session_messages)

        option = request_user_option(
            t.user_title.format(username), session_messages, default=default
        )
        if not required and not option:
            return ""

        if not re.match(pattern, option):
            display_cecilia_message(t.invalid_value_message, session_messages)
            continue

        return datetime.strptime(option, "%d-%m-%Y")


def get_valid_datetime(
    request_message, username, session_messages, required=True, default=""
):
    """
    Solicita ao usuário uma data e hora no formato DD-MM-AAAA HH:MM.
    - Valida o formato com regex.
    - Converte a entrada em um objeto datetime.
    - Pode aceitar valor vazio se 'required' for False.
    """
    pattern = r"^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(\d{4}) ([01][0-9]|2[0-3]):[0-5][0-9]$"

    while True:
        display_cecilia_message(request_message, session_messages)

        option = request_user_option(
            t.user_title.format(username), session_messages, default=default
        )
        if not required and not option:
            return ""

        if not re.match(pattern, option):
            display_cecilia_message(t.invalid_value_message, session_messages)
            continue

        return datetime.strptime(option, "%d-%m-%Y %H:%M")
