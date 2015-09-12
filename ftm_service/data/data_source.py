from pg4nosql.PostgresNoSQLClient import PostgresNoSQLClient
import config
import uuid


class FTMDataSource(object):
    def __init__(self):
        self.__pg = PostgresNoSQLClient(host=config.POSTGRES_HOST,
                                        port=config.POSTGRES_PORT,
                                        user=config.POSTGRES_USER,
                                        password=config.POSTGRES_PASSWORD)

        self.__db = self.__pg[config.FTM_DATABASE]

    # --- public ---

    # workflow
    def commit(self):
        self.__db.commit()

    def close(self):
        self.__db.close()

    # add
