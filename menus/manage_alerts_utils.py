from constants import STATIONS
import database as db
import text as t
from utils import *


def get_alert_id(request_message, username, session_messages):
    """
    Solicita ao usuário um valor para o ID do alerta.
    Garante que o valor informado seja um número inteiro válido.
    """
    while True:
        display_cecilia_message(
            request_message,
            session_messages,
        )

        option = request_user_option(t.user_title.format(username), session_messages)
        if not option.isdigit():
            display_cecilia_message(t.invalid_value_message, session_messages)
            continue

        return option


def get_alert_title(request_message, username, session_messages, default=""):
    """
    Solicita ao usuário o título do alerta.
    Garante que o valor não seja vazio. Permite fornecer um valor padrão.
    """
    while True:
        display_cecilia_message(
            request_message,
            session_messages,
        )

        title = request_user_option(
            t.user_title.format(username), session_messages, default=default
        )
        if title == "":
            display_cecilia_message(t.invalid_value_message, session_messages)
            continue

        return title


def get_alert_description(request_message, username, session_messages, default=""):
    """
    Solicita ao usuário a descrição do alerta.
    Garante que o valor não seja vazio. Permite fornecer um valor padrão.
    """
    while True:
        display_cecilia_message(
            request_message,
            session_messages,
        )

        description = request_user_option(
            t.user_title.format(username), session_messages, default=default
        )
        if description == "":
            display_cecilia_message(t.invalid_value_message, session_messages)
            continue

        return description


def get_alert_start_time(request_message, username, session_messages, default=""):
    """
    Solicita ao usuário a data e hora de início do alerta.
    Se o usuário não fornecer uma data, usa a data e hora atual como padrão.
    """
    start_time = get_valid_datetime(
        request_message,
        username,
        session_messages,
        required=False,
        default=default,
    )

    if start_time == "":
        return start_time

    return start_time if start_time else datetime.now()


def get_alert_end_time(
    request_message, start_time, username, session_messages, default=""
):
    """
    Solicita ao usuário a data e hora de término do alerta.
    Valida se a data de término ocorre depois da data de início.
    """
    while True:
        end_time = get_valid_datetime(
            request_message,
            username,
            session_messages,
            required=False,
            default=default,
        )

        if end_time == "":
            return end_time

        if end_time < start_time:
            display_cecilia_message(t.invalid_end_time_message, session_messages)
            continue

        return end_time


def get_alert_station(request_message, username, session_messages, default=""):
    """
    Solicita ao usuário a estação do alerta com base em uma lista pré-definida.
    Valida se o índice fornecido é válido.
    """
    while True:
        display_cecilia_message(
            request_message,
            session_messages,
        )

        option = request_user_option(
            t.user_title.format(username), session_messages, default=default
        )
        if not valid_positive_index(option, len(STATIONS)):
            display_cecilia_message(t.invalid_value_message, session_messages)
            continue

        station = STATIONS[int(option) - 1]
        return station


def get_id_severity(request_message, username, session_messages, default=""):
    """
    Exibe os níveis de severidade disponíveis e solicita ao usuário que escolha um.
    Retorna o índice correspondente à severidade selecionada.
    """
    severities = db.get_all_severities()
    severities_options = "\n".join(list(map(severity_option_str, severities)))

    while True:
        display_cecilia_message(
            request_message.format(severities_options),
            session_messages,
        )

        option = request_user_option(
            t.user_title.format(username),
            session_messages,
            default=default,
        )
        if not valid_positive_index(option, len(severities)):
            display_cecilia_message(t.invalid_value_message, session_messages)
            continue

        return int(option)


def get_valid_alert_status(request_message, username, session_messages):
    """
    Solicita ao usuário que informe o status desejado para filtrar os alertas:
    - "1": alerta ativo (sem data de término).
    - "2": alerta encerrado (com data de término).
    """
    while True:
        display_cecilia_message(
            request_message,
            session_messages,
        )

        option = request_user_option(t.user_title.format(username), session_messages)
        match option:
            case "1":
                return "IS NULL"
            case "2":
                return "IS NOT NULL"
            case _:
                display_cecilia_message(t.invalid_option_message, session_messages)
                continue

        return option


def request_new_alert_values(username, session_messages):
    """
    Solicita ao usuário todos os campos necessários para criar um novo alerta.
    Retorna um dicionário com os dados coletados.
    """
    title = get_alert_title(t.request_new_alert_title, username, session_messages)
    description = get_alert_description(
        t.request_new_alert_description, username, session_messages
    )
    start_time = get_alert_start_time(
        t.request_new_alert_start_time, username, session_messages
    )
    end_time = get_alert_end_time(
        t.request_new_alert_end_time, start_time, username, session_messages
    )
    station = get_alert_station(t.request_new_alert_station, username, session_messages)
    id_severity = get_id_severity(
        t.request_new_alert_id_severity, username, session_messages
    )

    return {
        "title": title,
        "description": description,
        "start_time": start_time,
        "end_time": end_time,
        "station": station,
        "id_severity": id_severity,
    }


def get_updated_alert_values(username, session_messages, alert):
    """
    Solicita ao usuário os novos valores para atualizar um alerta existente.
    Os campos já vêm preenchidos com os valores atuais como padrão.
    """
    alert_station_option = (
        STATIONS.index(alert["station"]) + 1 if alert["station"] in STATIONS else ""
    )

    title = get_alert_title(
        t.request_update_alert_title, username, session_messages, default=alert["title"]
    )
    description = get_alert_description(
        t.request_update_alert_description,
        username,
        session_messages,
        default=alert["description"],
    )
    start_time = get_alert_start_time(
        t.request_update_alert_start_time,
        username,
        session_messages,
        default=alert["start_time"].strftime("%d-%m-%Y %H:%M"),
    )
    end_time = get_alert_end_time(
        t.request_update_alert_end_time,
        start_time,
        username,
        session_messages,
        default=(
            alert["end_time"].strftime("%d-%m-%Y %H:%M") if alert["end_time"] else ""
        ),
    )
    station = get_alert_station(
        t.request_update_alert_station,
        username,
        session_messages,
        default=alert_station_option,
    )
    id_severity = get_id_severity(
        t.request_update_alert_id_severity,
        username,
        session_messages,
        default=alert["severity_id"],
    )

    return {
        "title": title,
        "description": description,
        "start_time": start_time,
        "end_time": end_time,
        "station": station,
        "id_severity": id_severity,
    }


def export_alerts_question(alerts, username, session_messages):
    """
    Pergunta ao usuário se ele deseja exportar os alertas para um arquivo.
    Se sim, chama a função de exportação.
    """
    while True:
        display_cecilia_message(
            t.export_alerts,
            session_messages,
        )

        option = request_user_option(t.user_title.format(username), session_messages)
        match option:
            case "S":
                export_alerts(alerts, username, session_messages)
            case "N":
                display_cecilia_message(
                    t.export_alerts_denied,
                    session_messages,
                )
                break
            case _:
                display_cecilia_message(t.invalid_option_message, session_messages)
                continue

        break


def export_alerts(alerts, username, session_messages):
    """
    Exporta os alertas em formato JSON para o caminho definido pelo usuário.
    Realiza a formatação adequada das datas antes de salvar o arquivo.
    """
    while True:
        display_cecilia_message(
            t.request_export_alerts_path,
            session_messages,
        )

        path = request_user_option(t.user_title.format(username), session_messages)
        if not path:
            display_cecilia_message(t.invalid_value_message, session_messages)
            continue

        alerts = list(map(format_alert_for_export, alerts))

        path += ".json"
        with open(path, "w", encoding="utf-8") as file:
            json.dump(alerts, file, indent=4, ensure_ascii=False)

        display_cecilia_message(
            t.export_alerts_success,
            session_messages,
        )
        break


def format_alert_for_export(alert):
    """
    Formata os campos de data de um alerta para o padrão 'dd-mm-aaaa HH:MM',
    garantindo legibilidade no arquivo exportado.
    """
    return {
        **alert,
        "start_time": alert["start_time"].strftime("%d-%m-%Y %H:%M"),
        "end_time": (
            alert["end_time"].strftime("%d-%m-%Y %H:%M") if alert["end_time"] else None
        ),
    }
