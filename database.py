import oracledb

from constants import DB_USER, DB_PASSWORD, DB_URL
from utils import extract_alert, extract_severity


def get_connection():
    """
    Cria e retorna uma conexão com o banco de dados Oracle usando as credenciais
    definidas nos arquivos de configuração (constants.py).
    """
    return oracledb.connect(user=DB_USER, password=DB_PASSWORD, dsn=DB_URL)


def get_all_alerts():
    """
    Recupera todos os alertas da tabela 't_alert' com seus respectivos dados de severidade
    (por meio de um LEFT JOIN com a tabela 't_severity').
    Os resultados são ordenados pela data de término, início e nível de severidade.
    """
    stmt = """
    SELECT
        a.id,
        a.title,
        a.description,
        a.start_time,
        a.end_time,
        a.station,
        s.id,
        s.description,
        s.severity_level
    FROM
        t_alert a
        LEFT JOIN t_severity s ON ( a.id_severity = s.id )
    ORDER BY
        a.end_time DESC,
        a.start_time DESC,
        s.severity_level
    """

    with get_connection() as con:
        with con.cursor() as cur:
            cur.execute(stmt)
            alerts = cur.fetchall()

    # Transforma os resultados em dicionários utilizando a função utilitária extract_alert.
    return list(map(extract_alert, alerts)) if alerts else []


def get_filtered_alerts(where_clause, params={}):
    """
    Recupera alertas com base em uma cláusula WHERE customizada, útil para filtros dinâmicos.
    A cláusula e os parâmetros são passados externamente para montagem da query.
    """
    stmt = f"""
    SELECT
        a.id,
        a.title,
        a.description,
        a.start_time,
        a.end_time,
        a.station,
        s.id,
        s.description,
        s.severity_level
    FROM
        t_alert a
        LEFT JOIN t_severity s ON ( a.id_severity = s.id )
    WHERE
        {where_clause}
    ORDER BY
        a.end_time DESC,
        a.start_time DESC,
        s.severity_level
    """

    with get_connection() as con:
        with con.cursor() as cur:
            cur.execute(stmt, params)
            alerts = cur.fetchall()

    return list(map(extract_alert, alerts)) if alerts else []


def get_alert_by_id(id):
    """
    Recupera um único alerta com base em seu ID, incluindo os dados de severidade associados.
    Caso o alerta não seja encontrado, retorna um dicionário vazio.
    """
    stmt = f"""
    SELECT
        a.id,
        a.title,
        a.description,
        a.start_time,
        a.end_time,
        a.station,
        s.id,
        s.description,
        s.severity_level
    FROM
        t_alert a
        LEFT JOIN t_severity s ON ( a.id_severity = s.id )
    WHERE
        a.id = :id
    ORDER BY
        a.end_time DESC,
        a.start_time DESC,
        s.severity_level
    """

    with get_connection() as con:
        with con.cursor() as cur:
            cur.execute(stmt, {"id": id})
            alert = cur.fetchone()

    # Converte o resultado para dicionário ou retorna vazio se nenhum resultado for encontrado.
    return extract_alert(alert) if alert else {}


def insert_alert(alert):
    """
    Insere um novo alerta na tabela 't_alert' com os dados fornecidos em formato de dicionário.
    Realiza commit da transação após a inserção.
    """
    stmt = """
    INSERT INTO t_alert (
        title,
        description,
        start_time,
        end_time,
        station,
        id_severity
    ) VALUES (
        :title,
        :description,
        :start_time,
        :end_time,
        :station,
        :id_severity
    )
    """

    with get_connection() as con:
        with con.cursor() as cur:
            cur.execute(stmt, alert)

        con.commit()


def update_alert(id, alert):
    """
    Atualiza os dados de um alerta existente com base no ID informado.
    Recebe os novos dados em formato de dicionário e executa o commit ao final.
    """
    stmt = """
    UPDATE
        t_alert
    SET
        title = :title,
        description = :description,
        start_time = :start_time,
        end_time = :end_time,
        station = :station,
        id_severity = :id_severity
    WHERE
        id = :id
    """

    with get_connection() as con:
        with con.cursor() as cur:
            cur.execute(stmt, {"id": id, **alert})

        con.commit()


def delete_alert(id):
    """
    Exclui um alerta do banco de dados com base no ID fornecido.
    Executa commit após a remoção.
    """
    stmt = "DELETE FROM t_alert WHERE id = :id"

    with get_connection() as con:
        with con.cursor() as cur:
            cur.execute(stmt, {"id": id})

        con.commit()


def get_all_severities():
    """
    Recupera todas as severidades da tabela 't_severity', ordenadas por ID.
    Retorna uma lista de dicionários contendo ID, descrição e nível de severidade.
    """
    stmt = """
    SELECT
        id,
        description,
        severity_level
    FROM
        t_severity
    ORDER BY
        id
    """

    with get_connection() as con:
        with con.cursor() as cur:
            cur.execute(stmt)
            severities = cur.fetchall()

    return (
        list(
            map(
                extract_severity,
                severities,
            )
        )
        if severities
        else []
    )
