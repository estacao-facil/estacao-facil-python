from datetime import datetime, time

import database as db
from .manage_alerts_utils import *
from utils import *
import text as t


# MENU: Gerenciar Alertas
def manage_alerts_menu(username, session_messages):
    """
    Menu principal de gerenciamento de alertas.
    Permite listar, detalhar, criar, editar e remover alertas.
    O loop é interrompido após uma operação válida ou ao cancelar.
    """
    while True:
        display_cecilia_message(
            t.manage_alerts_menu,
            session_messages,
        )

        option = request_user_option(t.user_title.format(username), session_messages)
        match option:
            case "1":
                list_alerts(username, session_messages)
            case "2":
                detail_alert(username, session_messages)
            case "3":
                new_alert(username, session_messages)
            case "4":
                update_alert(username, session_messages)
            case "5":
                remove_alert(username, session_messages)
            case "0":
                display_cecilia_message(t.cancel_operation_message, session_messages)
                break
            case _:
                display_cecilia_message(t.invalid_option_message, session_messages)
                continue

        break  # Sai do menu após executar uma operação válida


def list_alerts(username, session_messages):
    """
    Menu de listagem de alertas.
    Permite ao usuário escolher entre listar todos os alertas ou aplicar filtros.
    """
    while True:
        display_cecilia_message(
            t.list_alerts_menu,
            session_messages,
        )

        option = request_user_option(t.user_title.format(username), session_messages)
        match option:
            case "1":
                show_all_alerts(username, session_messages)
            case "2":
                show_filtered_alerts(username, session_messages)
            case "0":
                display_cecilia_message(t.cancel_operation_message, session_messages)
                break
            case _:
                display_cecilia_message(t.invalid_option_message, session_messages)
                continue

        break


def show_all_alerts(username, session_messages):
    """
    Busca e exibe todos os alertas registrados no sistema.
    Após exibição, oferece a opção de exportar os dados.
    """
    alerts = db.get_all_alerts()

    if not alerts:
        display_cecilia_message(t.alerts_not_found, session_messages)

    n_alerts = len(alerts)
    alerts_str = "\n".join(list(map(alert_str, alerts)))
    display_cecilia_message(
        t.list_all_alerts.format(n_alerts, alerts_str), session_messages
    )

    export_alerts_question(alerts, username, session_messages)


def show_filtered_alerts(username, session_messages):
    """
    Permite ao usuário filtrar alertas por:
    - ID
    - Status (ativo ou encerrado)
    - Estação
    - Data de início
    Após a exibição, oferece a opção de exportar os dados.
    """
    while True:
        display_cecilia_message(
            t.list_filtered_alerts_menu,
            session_messages,
        )

        option = request_user_option(t.user_title.format(username), session_messages)
        match option:
            case "1":
                id = get_alert_id(t.request_filter_alert_id, username, session_messages)
                where_clause = "a.id = :id"
                params = {"id": id}
            case "2":
                status = get_valid_alert_status(
                    t.request_filter_alert_status, username, session_messages
                )
                where_clause = f"a.end_time {status}"
                params = {}
            case "3":
                station = get_alert_station(
                    t.request_filter_alert_station, username, session_messages
                )
                where_clause = f"a.station = :station"
                params = {"station": station}
            case "4":
                date = get_valid_date(
                    t.request_filter_alert_date,
                    username,
                    session_messages,
                )
                where_clause = "a.start_time BETWEEN :start_time AND :end_time"
                params = {
                    "start_time": datetime.combine(date, time(hour=0, minute=0)),
                    "end_time": datetime.combine(date, time(hour=23, minute=59)),
                }
            case "0":
                display_cecilia_message(t.cancel_operation_message, session_messages)
                break
            case _:
                display_cecilia_message(t.invalid_option_message, session_messages)
                continue

        alerts = db.get_filtered_alerts(where_clause, params)

        if not alerts:
            display_cecilia_message(t.alerts_not_found, session_messages)

        n_alerts = len(alerts)
        alerts_str = "\n".join(list(map(alert_str, alerts)))
        display_cecilia_message(
            t.list_filtered_alerts.format(n_alerts, alerts_str), session_messages
        )

        export_alerts_question(alerts, username, session_messages)

        break


def detail_alert(username, session_messages):
    """
    Exibe os detalhes completos de um alerta selecionado pelo ID.
    Mostra status (Ativo/Encerrado), data formatada e informações relevantes.
    """
    display_cecilia_message(t.detail_alert_menu, session_messages)

    id = get_alert_id(t.request_detail_alert_id, username, session_messages)

    alert = db.get_alert_by_id(id)
    if alert:
        alert["status"] = "Encerrado" if alert["end_time"] else "Ativo"
        alert["start_time"] = alert["start_time"].strftime("%d/%m/%Y %H:%M")
        alert["end_time"] = (
            alert["end_time"].strftime("%d/%m/%Y %H:%M")
            if alert["end_time"]
            else "Não Encerrado"
        )

        display_cecilia_message(
            t.detail_alert.format(**alert),
            session_messages,
        )
    else:
        display_cecilia_message(t.alerts_not_found, session_messages)


def new_alert(username, session_messages):
    """
    Inicia o processo de criação de um novo alerta:
    - Solicita todos os dados necessários.
    - Insere o alerta no banco de dados.
    """
    display_cecilia_message(t.new_alert, session_messages)
    new_alert = request_new_alert_values(username, session_messages)
    db.insert_alert(new_alert)

    display_cecilia_message(
        t.new_alert_success,
        session_messages,
    )


def update_alert(username, session_messages):
    """
    Permite ao usuário atualizar os dados de um alerta existente.
    - Verifica se o ID informado existe.
    - Se existir, solicita os novos dados e atualiza o registro no banco.
    """
    display_cecilia_message(t.update_alert, session_messages)

    while True:
        id = get_alert_id(t.request_update_alert_id, username, session_messages)

        if id == "0":
            display_cecilia_message(
                t.cancel_operation_message,
                session_messages,
            )
            return

        alert = db.get_alert_by_id(id)
        if not alert:
            display_cecilia_message(
                t.alert_not_found,
                session_messages,
            )
            continue
        break

    updated_alert = get_updated_alert_values(username, session_messages, alert)
    db.update_alert(id, updated_alert)

    display_cecilia_message(
        t.update_alert_success,
        session_messages,
    )


def remove_alert(username, session_messages):
    """
    Permite remover um alerta do sistema.
    - Solicita o ID do alerta.
    - Verifica se ele existe.
    - Pede confirmação antes de excluir.
    """
    display_cecilia_message(t.remove_alert, session_messages)

    while True:
        id = get_alert_id(t.request_delete_alert_id, username, session_messages)

        if id == "0":
            display_cecilia_message(
                t.cancel_operation_message,
                session_messages,
            )
            return

        alert = db.get_alert_by_id(id)
        if not alert:
            display_cecilia_message(
                t.alert_not_found,
                session_messages,
            )
            continue
        break

    user_confirmation = request_user_confirmation(
        t.user_title.format(username),
        t.delete_alert_confirm_message.format(id),
        session_messages,
    )
    if not user_confirmation:
        display_cecilia_message(t.operation_cancelled_message, session_messages)
        return

    db.delete_alert(id)
    display_cecilia_message(t.alert_deleted_message.format(id), session_messages)
