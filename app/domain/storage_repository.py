from abc import ABC , abstractmethod
from  app.domain.page import Page 


class StorageRepository(ABC):
     """
     Interfaz para repositorios de almacenamiento de entidades page
     """

     @abstractmethod
     def save(self, page: Page) -> None:
          """
          Persiste una instacia page.
          
          : Praram page: Entidad page con los datos a almacernar
          """