#  Cabeçalho
header = (
"""--------------------------------------------------------------------------------
----------------------------------ESTAÇÃO FÁCIL---------------------------------
--------------------------------------------------------------------------------
""")

welcome_message = (
"""Olá! Bem-vindo ao Estação Fácil!
Eu sou Cecília, sua assistente virtual, e estou aqui para ajudar você.

Para começar, por favor, me diga o seu nome.
""")


#  Título dos participantes
cecilia_title = "Cecília:"

undefined_title = "Usuário não identificado:"

user_title = "{}:"


#  MENU: Principal
welcome_menu = (
"""Prazer em te conhecer, {}!
Agora que já sabemos quem você é, aqui estão as opções do Menu Principal:

1. Obter Informações
2. Traçar Rotas entre Estações
3. Localizar-se
0. Sair

Por favor, escolha uma das opções para continuar.
""")

main_menu = (
"""Posso ajudar com mais alguma coisa?  

1. Obter Informações
2. Traçar Rotas entre Estações
3. Localizar-se
0. Sair
""")


#  MENU: Obter Informações
information_menu = (
"""Você escolheu "Obter Informações".
Aqui estão as opções de informações disponíveis:

1. Alertas e Notificações
2. Horário de Funcionamento
3. Tarifas e Formas de Pagamento
4. Listar Estações
5. Sobre a Equipe
0. Cancelar

Digite o número correspondente à sua escolha.
""")

alerts_notifications_message = (
"""Atualmente, não há alertas de incidentes ou interrupções na linha amarela do metrô.

Continue verificando regularmente para atualizações em tempo real.
""")

operating_hours_message = (
"""A linha amarela do metrô de São Paulo opera nos seguintes horários:

- De segunda a sexta-feira: das 04h40 às 00h00.
- Sábados: das 04h40 à 01h00.
- Domingos e feriados: das 04h40 às 00h00.

Por favor, esteja ciente de que os horários podem ser alterados durante feriados
prolongados ou devido a manutenções programadas.
""")

fares_payment_message = (
"""A tarifa padrão para o uso da linha amarela do metrô é de R$ 5,00.

As formas de pagamento aceitas incluem:

- Cartão de débito/crédito com tecnologia NFC (sem contato).
- Cartão Bilhete Único (recarga online ou nos terminais das estações).
- Dinheiro (somente nos guichês de atendimento).
""")

list_stations_message = (
"""As estações atualmente em operação na linha amarela do metrô de São Paulo são:

- Butantã
- Pinheiros
- Faria Lima
- Fradique Coutinho
- Oscar Freire
- Paulista
- Higienópolis-Mackenzie
- República
- Luz
""")

about_team_message = (
"""O desenvolvimento deste sistema foi realizado pela seguinte equipe:

- Angelo Antonio Recke Ricieri. RM:560299
- Antonio de Luca Ribeiro Silva. RM:560169
- Paulo Sérgio França Barbosa. RM:559914
""")

cancel_operation_message = (
"""Operação cancelada. Voltando para o Menu Principal.
""")


#  MENU: Traçar Rotas
departure_station_options = (
"""Certo! Vamos traçar a sua rota.

Por favor, escolha uma estação de partida na lista abaixo:

1. Butantã
2. Pinheiros
3. Faria Lima
4. Fradique Coutinho
5. Oscar Freire
6. Paulista
7. Higienópolis-Mackenzie
8. República
9. Luz

Digite o número correspondente à sua estação de partida.
""")

departure_confirmation_message = (
"""Perfeito! Você selecionou a estação {} como origem.
""")

destination_station_options = (
"""Certo! Agora escolha uma estação de destino na lista abaixo:

1. Butantã
2. Pinheiros
3. Faria Lima
4. Fradique Coutinho
5. Oscar Freire
6. Paulista
7. Higienópolis-Mackenzie
8. República
9. Luz

Digite o número correspondente à sua estação de destino.
""")

destination_confirmation_message = (
"""Ótimo! Você selecionou a estação {} como destino.
""")

route_summary_message = (
"""Rota traçada com sucesso!

- Estação de partida: {}
- Estação de destino: {}

Você precisará embarcar sentido {}, esperar por {} estações e descer na estação {}.

Agora é só seguir as indicações e embarcar no próximo trem!
Se precisar de mais alguma coisa, estarei por aqui para ajudar. Boa viagem!
""")

same_departure_destination_message = (
"""Ué, parece que você está tentando ir para onde já está!
Se precisar realmente ir a algum lugar, é só me avisar.
Vou estar aqui prontinha para te ajudar!
""")


#  MENU: Obter Localização
location_menu = (
"""Para que eu possa te ajudar a se localizar, por favor, insira o código que está
logo abaixo de um QR Code ao seu redor.
Cada estação da linha amarela tem códigos específicos espalhados por ela.

Veja alguns exemplos de códigos que você pode encontrar:

    BU-177, BU-810, PI-871, PI-614, FA-673, FA-346, FR-411, FR-762, OS-677, OS-620,
    PA-867, PA-967, HI-197, HI-213, RE-820, RE-618, LU-181, LU-143

Digite o código que você está vendo e eu te direi a sua localização!
""")

location_result_message = (
"""Prontinho! Você está localizado em:

{}.
""")


#  Outros
invalid_input_message = (
"""Ops! Parece que você digitou uma opção inválida.

Por favor, escolha uma das opções do menu para que eu possa te ajudar corretamente.
""")

farewell_message = (
"""Ok! Se precisar de algo mais, estarei por aqui para ajudar.
Tenha um ótimo dia e até a próxima!
""")
