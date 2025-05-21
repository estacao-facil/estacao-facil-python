from constants import STATIONS
import text as t
from utils import *


# MENU: Traçar Rotas entre Estações
def route_menu(username, session_messages):
    """
    Função para o menu de traçar rotas entre estações.
    Solicita ao usuário a estação de partida e de destino, valida a escolha e exibe um resumo da rota.
    """
    # Solicita e valida o índice da estação de partida.
    departure_index = request_station_index(
        username, t.departure_station_options, session_messages
    )
    departure_station = STATIONS[departure_index]
    display_cecilia_message(
        t.departure_confirmation_message.format(departure_station), session_messages
    )

    # Solicita e valida o índice da estação de destino.
    destination_index = request_station_index(
        username, t.destination_station_options, session_messages
    )
    destination_station = STATIONS[destination_index]
    display_cecilia_message(
        t.destination_confirmation_message.format(destination_station), session_messages
    )

    # Se a estação de partida for igual à de destino, exibe mensagem de erro e retorna.
    if departure_station == destination_station:
        display_cecilia_message(t.same_departure_destination_message, session_messages)
        return

    # Determina a direção com base na posição das estações na lista.
    direction = "Butantã" if departure_index > destination_index else "Luz"
    stations_until_destination = abs(departure_index - destination_index)

    # Exibe o resumo da rota com os detalhes da viagem.
    display_cecilia_message(
        t.route_summary_message.format(
            departure_station,
            destination_station,
            direction,
            stations_until_destination,
            destination_station,
        ),
        session_messages,
    )


def request_station_index(username, message, session_messages):
    """
    Função que solicita ao usuário um índice correspondente à estação desejada.
    Verifica se a entrada é um número válido e retorna o índice (ajustado para zero-based).
    """
    while True:
        display_cecilia_message(message, session_messages)

        option = request_user_option(t.user_title.format(username), session_messages)
        if not valid_positive_index(option, len(STATIONS)):
            display_cecilia_message(t.invalid_value_message, session_messages)
            continue

        return int(option) - 1  # Converte para inteiro e ajusta o índice.
