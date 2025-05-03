import pytest
from app.use_cases.scrape_page import PageScraper
from app.domain.page import Page

# definimos un parse falso 
class DummyParser:
     def __init__(self):
          self.html_return = "<html><head><title>Dummy Title</title></head></html>"

     # valida url
     def get_html(self, url: str) -> str:
          assert url == "https://chavitosclub.netlify.app/"
          return self.html_return


     def parse_title(self, html: str) -> str:
          assert html == self.html_return
          return "Mi titulo de Prueba"
     
# fixture para parchear pahepoarser dentro de paggescraper
@pytest.fixture(autouse=True)
def patch_page_parser(monkeypatch):
     # cuando pageScraper haga pageparser() en vez de la real, usara DummyParser
     monkeypatch.setattr(
               "app.use_cases.scrape_page.PageParser",
               lambda: DummyParser()
          )
     
def test_scrape_returns_correct_page():
     scraper = PageScraper()
     page: Page = scraper.scrape("https://chavitosclub.netlify.app/")

     assert isinstance(page, Page)
     assert page.url == "https://chavitosclub.netlify.app/"
     assert page.title == "Mi titulo de Prueba"

     