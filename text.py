# Cabeçalho
header = """--------------------------------------------------------------------------------
--------------------------------- ESTAÇÃO FÁCIL --------------------------------
--------------------------------------------------------------------------------
"""

welcome_message = """Olá, seja bem-vindo ao Estação Fácil!
Eu sou Cecília, sua assistente virtual, e estou aqui para te ajudar.

Para começarmos, por favor, informe o seu nome:
"""


# Títulos dos participantes
cecilia_title = "Cecília:"

undefined_title = "Usuário não identificado:"

user_title = "{}:"


#  MENU: Principal
welcome_menu = """Prazer em te conhecer, {}!
Agora que já sabemos quem você é, escolha uma das opções abaixo:

1. Obter Informações
2. Traçar Rotas entre Estações
3. Localizar-se
4. Gerenciar Alertas
5. Consultar Clima
6. Histórico de Conversas
0. Sair

Por favor, escolha uma das opções para continuar.
"""

main_menu = """Posso ajudar com mais alguma coisa?  

1. Obter Informações
2. Traçar Rotas entre Estações
3. Localizar-se
4. Gerenciar Alertas
5. Verificar Clima
6. Histórico de Conversas
0. Sair
"""


#  MENU: Obter Informações
information_menu = """Você escolheu "Obter Informações".
Aqui estão as opções de informações disponíveis:

1. Alertas e Notificações
2. Horário de Funcionamento
3. Tarifas e Formas de Pagamento
4. Listar Estações
5. Sobre a Equipe
0. Cancelar

Digite o número correspondente à sua escolha.
"""

alerts_notifications_message = """No momento, não há alertas de incidentes ou interrupções na linha amarela do metrô.
Recomendo que você verifique periodicamente para se manter atualizado.
"""

operating_hours_message = """A linha amarela do metrô de São Paulo opera nos seguintes horários:

- Segunda a sexta-feira: 04h40 às 00h00.
- Sábados: 04h40 às 01h00.
- Domingos e feriados: 04h40 às 00h00.

Lembre-se: esses horários podem ser alterados em feriados prolongados ou devido a manutenções programadas.
"""

fares_payment_message = """A tarifa padrão para utilizar a linha amarela do metrô é de R$ 5,0.

As formas de pagamento aceitas incluem:

- Cartão de débito/crédito com tecnologia NFC (sem contato).
- Cartão Bilhete Único (recarga online ou nos terminais das estações).
- Dinheiro (apenas nos guichês de atendimento).
"""

list_stations_message = """As estações atualmente em operação na linha amarela do metrô de São Paulo são:

- Butantã
- Pinheiros
- Faria Lima
- Fradique Coutinho
- Oscar Freire
- Paulista
- Higienópolis-Mackenzie
- República
- Luz
"""

about_team_message = """Este sistema foi desenvolvido pela equipe:

- Angelo Antonio Recke Ricieri – RM: 560299
- Antonio de Luca Ribeiro Silva – RM: 560169
- Paulo Sérgio França Barbosa – RM: 559914
"""

cancel_operation_message = """Operação cancelada. Retornando ao Menu Principal.
"""


#  MENU: Traçar Rotas
departure_station_options = """Certo! Vamos traçar a sua rota.

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
"""

departure_confirmation_message = """Perfeito! Você selecionou a estação {} como origem.
"""

destination_station_options = """Certo! Agora escolha uma estação de destino na lista abaixo:

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
"""

destination_confirmation_message = """Ótimo! Você selecionou a estação {} como destino.
"""

route_summary_message = """Rota traçada com sucesso!

- Estação de partida: {}
- Estação de destino: {}

Você precisará embarcar sentido {}, esperar por {} estações e descer na estação {}.

Agora é só seguir as indicações e embarcar no próximo trem!
Se precisar de mais alguma coisa, estarei por aqui para ajudar. Boa viagem!
"""

same_departure_destination_message = """Ué, parece que você está tentando ir para onde já está!
Se precisar realmente ir a algum lugar, é só me avisar.
Vou estar aqui prontinha para te ajudar!
"""


#  MENU: Obter Localização
location_menu = """Para que eu possa te ajudar a se localizar, por favor, insira o código que está
logo abaixo de um QR Code ao seu redor.
Cada estação da linha amarela tem códigos específicos espalhados por ela.

Veja alguns exemplos de códigos que você pode encontrar:
    BU-177, BU-810, PI-871, PI-614, FA-673, FA-346, FR-411, FR-762, OS-677, OS-620,
    PA-867, PA-967, HI-197, HI-213, RE-820, RE-618, LU-181, LU-143

Digite o código que você está vendo que eu te direi a sua localização!
"""

location_result_message = """Prontinho! Você está localizado em:
    {}.
"""


#  MENU: Histórico de Conversas
history_chat_menu = """Você escolheu "Histórico de Conversas".
Aqui estão as opções disponíveis:

1. Visualizar uma conversa anterior
2. Deletar uma conversa
3. Apagar todo o histórico de conversas
0. Cancelar

Digite o número correspondente à sua escolha.
"""

saved_chat_list_item = "{}. Salvo em: {}"

view_old_chat_options = """Essas são as sessões de chat salvas:

{}

Por favor, selecione a conversa desejada digitando o número correspondente.
"""

no_chat_history_message = """Nenhum registro de conversa encontrado.

Para que um histórico de conversa seja salvo, é necessário ter concluído uma conversa anteriormente. 
Sempre que você finalizar uma interação, a conversa será armazenada automaticamente e poderá ser acessada futuramente nesta seção.

Se precisar de ajuda, estou aqui para auxiliar você!
"""


view_old_chat_message = """----------------------------- Conversa Restaurada ------------------------------

Chat de: {}

{}

--------------------------------------------------------------------------------
"""

view_old_chat_delete_options = """Essas são as sessões de chat salvas:

{}

Por favor, selecione a conversa que deseja excluir digitando o número correspondente.
"""

delete_chat_confirm_message = """Você tem certeza de que deseja excluir o registro de "{}" do histórico de conversas?
Essa ação não pode ser revertida.

Digite "S" para confirmar ou "N" para cancelar.
"""

chat_deleted_message = """A conversa "{}" foi excluída com sucesso do histórico.
"""

delete_all_chats_confirm_message = """Você tem certeza de que deseja excluir todo o histórico de conversas?
Essa ação não pode ser revertida.

Digite "S" para confirmar ou "N" para cancelar.
"""

all_chats_deleted_message = """Todo o histórico de conversas foi excluído com sucesso.
"""


#  MENU: Gerenciar Alertas
manage_alerts_menu = """Você escolheu "Gerenciar Alertas".
Aqui estão as opções disponíveis:

1. Listar Alertas
2. Detalhar um Alerta
3. Cadastrar um Novo Alerta
4. Atualizar um Alerta Existente
5. Excluir um Alerta
0. Cancelar

Por favor, escolha uma das opções para continuar.
"""

list_alerts_menu = """Você escolheu "Listar Alertas".
Como deseja visualizar os alertas?

1. Listar Todos os Alertas
2. Aplicar Filtros de Pesquisa
0. Cancelar

Digite o número correspondente à sua escolha.
"""

list_filtered_alerts_menu = """Você escolheu aplicar filtros na listagem de alertas.
Escolha uma das opções abaixo:

1. Filtrar por ID
2. Filtrar por Status (Ativo ou Encerrado)
3. Filtrar por Estação
4. Filtrar por Data
0. Cancelar

Digite o número correspondente à opção desejada.
"""

detail_alert_menu = """Você escolheu "Detalhar um Alerta".

Por favor, informe o ID do alerta que deseja consultar.
"""

new_alert = """Você escolheu "Cadastrar um Novo Alerta".

Vamos registrar as informações do alerta passo a passo.
"""

update_alert = """Você escolheu "Atualizar um Alerta".

Informe o ID do alerta que deseja modificar.
"""

remove_alert = """Você escolheu "Excluir um Alerta".

Para continuar, por favor, informe o ID do alerta que deseja remover.
"""

alert_short_str = "[#{}] {} em {} | Gravidade: {} | Início: {} | Status: {}"

detail_alert = """Aqui estão os detalhes do alerta solicitado:

-------------------------- Detalhes do Alerta [#{id}] --------------------------

Título: {title}
Estação: {station}
Início: {start_time}
Fim: {end_time}
Gravidade: {severity_level} - {severity}
Descrição: {description}

Status: {status}

------------------------------------------------------------------------------
"""

list_all_alerts = """Foram encontrados {} alertas registrados no sistema:

{}
"""

list_filtered_alerts = """Foram encontrados {} alertas com base nos filtros aplicados:

{}
"""

alert_not_found = """Ops! Não encontrei nenhum alerta com o ID informado.

Verifique se o número está correto e tente novamente.
"""

alerts_not_found = """Nenhum alerta foi encontrado com os critérios fornecidos.

Tente ajustar os filtros ou verificar se os dados estão corretos.
"""

export_alerts = """Deseja exportar o resultado em formato JSON?

Digite "S" para confirmar ou "N" para cancelar.
"""

request_export_alerts_path = """Por favor, informe o caminho e nome do arquivo onde deseja salvar os alertas.

Não é necessário incluir a extensão ".json". Ela será adicionada automaticamente.
"""

export_alerts_success = """Exportação concluída com sucesso!

O arquivo com os alertas foi salvo no local indicado.
"""

export_alerts_denied = """Tudo bem! A exportação foi cancelada e nenhum arquivo foi gerado.
"""

delete_alert_confirm_message = """Tem certeza de que deseja excluir o alerta [#{}]?

Essa ação é permanente e não poderá ser desfeita.

Digite "S" para confirmar ou "N" para cancelar.
"""

alert_deleted_message = """O alerta [#{}] foi excluído com sucesso do sistema.
"""

new_alert_success = """Alerta cadastrado com sucesso!

Agora ele já está disponível para visualização e gerenciamento.
"""

invalid_end_time_message = """Atenção: a data de encerramento deve ser posterior à data de início do alerta.
Por favor, tente novamente.
"""

severity_option_str = "{}. {}"

request_filter_alert_id = """Por favor, informe o ID do alerta para busca.
"""

request_filter_alert_status = """Qual o status do alerta?

1. Ativo
2. Encerrado

Digite o número correspondente.
"""

request_filter_alert_station = """Escolha a estação onde o alerta está localizado:

1. Butantã
2. Pinheiros
3. Faria Lima
4. Fradique Coutinho
5. Oscar Freire
6. Paulista
7. Higienópolis-Mackenzie
8. República
9. Luz

Digite o número correspondente à estação.
"""

request_filter_alert_date = """Para buscar por data, insira uma no formato:

DD-MM-AAAA
Exemplo: 07-05-2025
"""

request_detail_alert_id = """Informe o ID do alerta que deseja visualizar.
"""

request_new_alert_title = """Dê um título para o novo alerta.
"""

request_new_alert_description = """Descreva brevemente o que está acontecendo.
"""

request_new_alert_start_time = """Insira a data e o horário de início do alerta.

Formato esperado: DD-MM-AAAA HH:MM  
Exemplo: 07-05-2025 14:30

Dica: Deixe em branco para usar a data e hora atual.
"""

request_new_alert_end_time = """Insira a data e o horário de encerramento do alerta.

Formato esperado: DD-MM-AAAA HH:MM  
Exemplo: 07-05-2025 18:00

Dica: Deixe em branco se o alerta ainda estiver em andamento (não resolvido).
"""

request_new_alert_station = """Escolha a estação onde o alerta está localizado:

1. Butantã
2. Pinheiros
3. Faria Lima
4. Fradique Coutinho
5. Oscar Freire
6. Paulista
7. Higienópolis-Mackenzie
8. República
9. Luz

Digite o número correspondente.
"""

request_new_alert_id_severity = """Escolha o grau de gravidade do alerta:

{}
"""

request_update_alert_id = """Informe o ID do alerta que deseja atualizar.

Digite 0 para cancelar.
"""

request_update_alert_title = """Atualize o título do alerta (ou mantenha o atual).
"""

request_update_alert_description = """Atualize a descrição do alerta (ou mantenha a atual).
"""

request_update_alert_start_time = """Insira a nova data e horário de início (ou mantenha a atual).

Formato: DD-MM-AAAA HH:MM
Exemplo: 07-05-2025 10:00

Dica: Deixe em branco para usar a data e hora atual.
"""

request_update_alert_end_time = """Insira a nova data e horário de fim (ou mantenha a atual).

Formato: DD-MM-AAAA HH:MM
Exemplo: 07-05-2025 12:00

Dica: Deixe em branco se o alerta ainda estiver em andamento (não resolvido).
"""

request_update_alert_station = """Escolha a nova estação (ou mantenha a atual):

1. Butantã
2. Pinheiros
3. Faria Lima
4. Fradique Coutinho
5. Oscar Freire
6. Paulista
7. Higienópolis-Mackenzie
8. República
9. Luz

Digite o número correspondente.
"""

request_update_alert_id_severity = """Escolha o novo grau de gravidade (ou mantenha o atual):

{}
"""

request_delete_alert_id = """Informe o ID do alerta que deseja excluir.

Digite 0 para cancelar.
"""


#  MENU: Checar Clima
check_weather_menu = """Você escolheu "Verificar Clima".

Antes de sair de casa ou ao planejar sua chegada a uma estação, é sempre bom conferir o clima da região.

Por favor, digite o nome do bairro de São Paulo onde deseja verificar a previsão do tempo.
Você pode consultar tanto o bairro onde está quanto o da sua estação de destino.
"""

check_weather_district_not_found = """Não consegui encontrar esse bairro.

Verifique se o nome foi digitado corretamente. Dica: evite abreviações ou termos muito genéricos.
"""

check_weather_weather_fail = """Houve um problema ao consultar a previsão do tempo para a região escolhida.

Por favor, tente novamente mais tarde.
"""

weather_info = """Aqui está o clima atual em "{}":

Temperatura: {}°C  
Sensação térmica: {}°C  
Condição do tempo: {}  
Umidade relativa do ar: {}%

Essas informações ajudam você a se preparar melhor antes de sair!
"""

check_weather_connection_error = """Não consegui me conectar ao serviço de clima no momento.

Pode ser um problema com sua internet ou com o serviço externo que usamos para essa consulta.

Verifique sua conexão e tente novamente mais tarde.
"""


#  Outros
invalid_option_message = """Ops! Parece que você digitou uma opção inválida.

Por favor, escolha uma das opções para prosseguir.
"""

invalid_value_message = """Ops! Parece que você digitou um valor inválido.

Por favor, insira um valor válido.
"""

farewell_message = """Ok! Se precisar de algo mais, estarei por aqui para ajudar.
Tenha um ótimo dia e até a próxima!"""

update_alert = """Você escolheu "Atualizar um Alerta".

Informe o ID do alerta que deseja modificar e em seguida, atualize as informações desejadas.
"""

update_alert_success = """Alerta atualizado com sucesso!

As informações foram salvas e já estão disponíveis para visualização.
"""

operation_cancelled_message = """Operação cancelada. Nenhuma alteração foi feita.
"""
