import psycopg2

class PostgresqlConnection:
    """
    Classe responsável por gerenciar a conexão com o banco de dados PostgreSQL.
    """

    def __init__(self, connection_string: str):
        """
        Inicializa a instância com a string de conexão ao banco de dados.
        """
        self.connection_string = connection_string
        self.connection_postgres = None
        self.cursor = None
        self.connect()

    def connect(self):
        """
        Abre uma conexão com o banco de dados e inicializa o cursor.
        Além disso, configura a codificação para UTF-8.
        """
        try:
            # Conecta-se ao banco de dados
            print(self.connection_string)
            self.connection_postgres = psycopg2.connect(self.connection_string)
            self.cursor = self.connection_postgres.cursor()

            # Configura a codificação para UTF-8
            self.connection_postgres.set_client_encoding('UTF8')
        except Exception as e:
            print(f"Failed to connect to the database: {e}")
            raise e

    def close(self):
        """
        Fecha a conexão com o banco de dados e o cursor.
        """
        if self.cursor:
            self.cursor.close()
        if self.connection_postgres:
            self.connection_postgres.close()

    def commit(self):
        """
        Commit a transação atual.
        """
        if self.connection_postgres:
            self.connection_postgres.commit()

    def rollback(self):
        """
        Reverte a transação atual.
        """
        if self.connection_postgres:
            self.connection_postgres.rollback()

    def __enter__(self):
        """
        Método para suportar o uso de 'with' (context manager).
        """
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Fecha a conexão automaticamente quando usado com 'with'.
        """
        if exc_type is not None:
            self.rollback()
        self.close()
