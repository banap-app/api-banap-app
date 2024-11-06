import psycopg2
from psycopg2 import sql
from uuid import UUID
from typing import List
from ...Domain.entities import Analysis
from ...Application.adapters import NpkAnalisysRepository

class NpkAnalisysRepositoryPostgresql(NpkAnalisysRepository):
    """
    PostgreSQL implementation of NpkAnalisysRepository.
    """
    def __init__(self, connection_string: str):
        # Inicializa a conexão com o banco de dados PostgreSQL
        self.connection = psycopg2.connect(connection_string)
        self.cursor = self.connection.cursor()

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
                str(analysis.id_field),
                analysis.result,
                analysis.created_at
            ))
            self.connection.commit()
        except Exception as e:
            self.connection.rollback()
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
        # Fecha a conexão quando o objeto for destruído
        self.cursor.close()
        self.connection.close()
