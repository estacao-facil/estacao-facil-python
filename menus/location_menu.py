from constants import LOCATIONS
import text as t
from utils import *


# MENU: Localizar-se
def location_menu(username, session_messages):
    """
    Menu que solicita ao usuário a opção de localização e exibe a descrição da localização selecionada.
    """
    while True:
        display_cecilia_message(t.location_menu, session_messages)

        option = request_user_option(t.user_title.format(username), session_messages)
        if not option in LOCATIONS.keys():
            display_cecilia_message(t.invalid_value_message, session_messages)
            continue

        break

    location = LOCATIONS[option]
    display_cecilia_message(
        t.location_result_message.format(location), session_messages
    )
