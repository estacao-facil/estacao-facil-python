import text as t
from utils import *

import database as db


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
            case "1":
                show_all_active_alerts(session_messages)
            case "2":
                display_cecilia_message(t.operating_hours_message, session_messages)
            case "3":
                display_cecilia_message(t.fares_payment_message, session_messages)
            case "4":
                display_cecilia_message(t.list_stations_message, session_messages)
            case "5":
                display_cecilia_message(t.about_team_message, session_messages)
            case "0":
                display_cecilia_message(t.cancel_operation_message, session_messages)
            case _:
                display_cecilia_message(t.invalid_option_message, session_messages)
                continue  # Se a opção for inválida, repete o loop.

        break  # Encerra o loop após uma opção válida ser processada.


# Exibe todos os alertas ativos (ou seja, que ainda não têm data de término registrada).
def show_all_active_alerts(session_messages):
    """
    Função responsável por buscar e exibir todos os alertas ativos.
    - Considera como "ativo" qualquer alerta cuja coluna 'end_time' esteja nula.
    - Utiliza a função 'get_filtered_alerts' do módulo database para realizar a consulta.
    - Exibe a lista formatada com todos os alertas encontrados.
    - Caso nenhum alerta esteja ativo, exibe uma mensagem padrão.
    """
    alerts = db.get_filtered_alerts(
        "a.end_time IS NULL"
    )  # Consulta alertas sem data de término (ativos).
    n_alerts = len(alerts)

    if alerts:
        # Formata a lista de alertas em uma única string para exibição.
        alerts_str = "\n".join(list(map(alert_str, alerts)))
        display_cecilia_message(
            t.list_filtered_alerts.format(n_alerts, alerts_str), session_messages
        )
    else:
        # Se nenhum alerta for encontrado, exibe mensagem informando ausência de alertas ativos.
        display_cecilia_message(t.alerts_not_found, session_messages)
