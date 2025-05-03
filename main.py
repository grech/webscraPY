from app.infrastructure.storage.json_storage import JsonFileStorage
from app.use_cases.scrape_and_store import ScrapeAndStore

if __name__ == "__main__":
     
     # scraper = PageScraper()
     # page = scraper.scrape("https://chavitosclub.netlify.app/")
     # print(f"URL: {page.url}")
     # print(f"Title: {page.title}")
     
    # Ruta del archivo JSON donde se guardarán los resultados
     output_path = "scraped_page.json"
     
     # instancia el almacenamiento JSON
     storage = JsonFileStorage(filepath=output_path)
     
     # Crea el caso de uso que combina el scraping y almacenamiento
     scraper_storage = ScrapeAndStore(storage=storage)
     
     
     urls=[
          "https://chavitosclub.netlify.app/",
          "https://www.google.com",
          "https://www.bing.com",
          "https://www.duckduckgo.com",
          "https://www.github.com",
          "https://www.stackoverflow.com",
          "https://www.reddit.com",
          "https://www.quora.com",
          "https://www.wikipedia.org"
     ]
     
     for url in urls:
          print(f"scraping y guardando : {url}")
          scraper_storage.execute(url)
     
     print(f"Resultados guardados en {output_path}")