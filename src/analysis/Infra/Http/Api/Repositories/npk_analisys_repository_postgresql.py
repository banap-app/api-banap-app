from uuid import UUID
from typing import List
from .....Domain.entities import Analysis
from .....Application.adapters import NpkAnalisysRepository
from ....Database.postgresql_connection import PostgresqlConnection

class NpkAnalisysRepositoryPostgresql(NpkAnalisysRepository):
    """
    PostgreSQL implementation of NpkAnalisysRepository.
    """
    def __init__(self, connection: PostgresqlConnection):
        """
        Inicializa a instância com a conexão do PostgreSQL.
        """
        self.connection = connection
        self.cursor = self.connection.cursor  # Usando o cursor da conexão

    def add(self, analysis: Analysis):
        """
        Adiciona uma nova análise NPK ao banco de dados.
        """
        try:
            query = """
            INSERT INTO npk_analysis (id, id_field, result, created_at)
            VALUES (%s, %s, %s, %s)
            """
            self.cursor.execute(query, (
                str(analysis.id),
                str(analysis.idField),
                analysis.result,
                analysis.created_at
            ))
            self.connection.commit()  # Realiza o commit da transação
        except Exception as e:
            self.connection.rollback()  # Reverte a transação em caso de erro
            print(f"Failed to add analysis: {e}")
            raise e

    def listAnalisys(self, idField: UUID) -> List[Analysis]:
        """
        Retorna todas as análises NPK com base no idField fornecido.
        """
        try:
            query = """
            SELECT id, id_field, result, created_at
            FROM npk_analysis
            WHERE id_field = %s
            """
            self.cursor.execute(query, (str(idField),))
            rows = self.cursor.fetchall()

            analyses = []
            for row in rows:
                analysis = Analysis(
                    id=UUID(row[0]),
                    id_field=UUID(row[1]),
                    result=row[2],
                    created_at=row[3]
                )
                analyses.append(analysis)

            return analyses
        except Exception as e:
            print(f"Failed to list analyses: {e}")
            raise e

    def __del__(self):
        """
        Garante que o cursor e a conexão sejam fechados ao destruir o objeto.
        """
        if hasattr(self, 'cursor') and self.cursor:
            self.cursor.close()
        if hasattr(self, 'connection') and self.connection:
            self.connection.close()
