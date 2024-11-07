import os
from dataclasses import dataclass
from ...Application.adapters import NpkAnalisysRepository
from ...Application.usecases import CreateNpkAnalisys, ListNpkAnalysis
from ...Infra.Database.postgresql_connection import PostgresqlConnection
from ...Infra.Http.Api.Repositories.npk_analisys_repository_postgresql import NpkAnalisysRepositoryPostgresql
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

@dataclass(slots=True)
class NpkAnalysisUseCaseFactory:
    def _get_connection_string(self) -> str:
        """
        Retorna a string de conexão ao banco de dados, carregada do arquivo .env.
        """
        db_name = os.getenv('DB_NAME')
        db_user = os.getenv('DB_USER')
        db_host = os.getenv('DB_HOST')
        db_password = os.getenv('DB_PASSWORD')

        return f"dbname='{db_name}' user='{db_user}' host='{db_host}' password='{db_password}'"

    def _get_repository(self) -> NpkAnalisysRepository:
        """
        Retorna uma instância de NpkAnalisysRepositoryPostgresql.
        """
        connection_string = self._get_connection_string()
        #connection_string = "dbname='a' user='postgres' host='localhost' password='my'"

        
        
        # Crie uma instância de PostgresqlConnection com a connection_string
        postgres_connection = PostgresqlConnection(connection_string=connection_string)
        
        
        # Passa o postgres_connection para o NpkAnalisysRepositoryPostgresql
        return NpkAnalisysRepositoryPostgresql(connection=postgres_connection)

    def create_npk_analisys_usecase(self) -> CreateNpkAnalisys:
        """
        Retorna uma instância de CreateNpkAnalisys.
        """
        npk_analisys_repository = self._get_repository()
        return CreateNpkAnalisys(npk_analisys_repository=npk_analisys_repository)

    def list_npk_analisys_usecase(self) -> ListNpkAnalysis:
        """
        Retorna uma instância de ListNpkAnalysis.
        """
        npk_analisys_repository = self._get_repository()
        return ListNpkAnalysis(npk_analisys_repository=npk_analisys_repository)
