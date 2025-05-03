# from app.use_cases.scrape_page import ScrapePage
from app.use_cases.scrape_page import PageScraper
from app.domain.storage_repository import StorageRepository

class ScrapeAndStore:
     """Cada uso que combina el scraping de una url y el almacenamiento de su entidad page"""
     
     def __init__(self, storage: StorageRepository):
          self.scraper = PageScraper()
          self.storage = storage
          
     def execute(self, url: str):
          """ ejecuta el scraping de la url priporcionada y  guarda el resultado en el almacenamiento """
          
          page = self.scraper.scrape(url)
          self.storage.save(page)