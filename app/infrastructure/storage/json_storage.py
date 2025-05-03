import json
import os
from app.domain.storage_repository import StorageRepository
from app.domain.page import Page

class JsonFileStorage(StorageRepository):
     """Implementacion de sStorageRepository que persiste paginas en un archivo JSON
     Cada llamada a save agrega un nuevo objeto url con su titulo al array JSON"""

     def __init__(self, filepath: str):
          self.filepath = filepath
          # ASegura que el archivo exista
          if not os.path.exists(filepath):
               with open(self.filepath, 'w', encoding='utf-8') as f:
                    json.dump([],f,ensure_ascii=False, indent=2)


     def save(self, page: Page):
          # lee el contenido existente 
          with open(self.filepath, 'r+', encoding='utf-8') as f:
               try:
                    data = json.load(f)
               except json.JSONDecodeError:
                    data= []
               # Agrega la nueva pagina
               data.append({
                    "url": page.url,
                    "title": page.title,
                    "h1": page.h1
               })
               # escribe de nuevo en el archivo
               f.seek(0)
               json.dump(data, f, ensure_ascii=False, indent=2)
               f.truncate()
