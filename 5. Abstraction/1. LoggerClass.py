from abc import ABC, abstractmethod
from datetime import datetime

class Logger(ABC):
    def __init__(self, level:str):
        self.__level = level

    @abstractmethod
    def log(self, message:str) -> None:
        pass 

    def format_message(self, message:str) -> str:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"[{timestamp}] [{self.__level}] {message}"
    
class consolelogger(Logger):
    def __init__(self, level:str):
        super().__init__(level)
        
    def log(self, message:str) -> None:
        print(self.format_message(message))
    
class Filelogger(Logger):

    def __init__(self, level:str, file_path:str):
        super.__init__(level)
        self._file_path = file_path

    def log(self, message:str) -> None:
        print(f" Writing to {self._file_path} : {self.format_message(message)}")
