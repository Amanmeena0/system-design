class Databaseclient:
    def __init__(self, max_connections:int, retry_attempts:int):
        self.__max_connections = max_connections
        self.__retry_attempts = retry_attempts

    def connect(self, host:str, port:int) -> None:
        self.__open_socket(host, port)
        self.__authenticate()
        self.__initialize_connection_pool()

    def query(self, sql:str) ->str:
        parsed_query = self.__parse_query(sql)
        return self.__execute_with_retry(parsed_query)
    
    def __open_socket(self, host:str, port:str) -> None: pass
    def __authenticate(self) -> None: pass
    def __initialize_connection_pool(self) -> None: pass
    def __parse_query(self, sql:str) -> str: return sql.strip()
    def __execute_with_retry(self, query:str) -> str:

        for i in range(self.__retry_attempts):

            try:
                return self.__execute_query()
            
            except Exception:
                if i == self.__retry_attempts - 1:
                    raise

        return ""
    def __execute_query(self, query:str) ->str: return "result"
