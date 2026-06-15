from abc import ABC, abstractmethod

class Exportable(ABC):
    @abstractmethod
    def export(self) ->str:
        pass

class CSVExporter(Exportable):
    def export(self):
        return "name,email,age\nAlice,alice@gmail.com,30"
    
class JSONExporter(Exportable):
    def export(self) -> str:
        return '{"name":"Alice", "email":"alice@gmail.com"}'