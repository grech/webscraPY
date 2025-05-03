# app/use_cases/scrape_page.py
from app.infrastructure.web.bs_parser import PageParser
from app.domain.page import Page;

class PageScraper:
     def __init__(self):
          self.parser = PageParser()

     def scrape(self, url: str) -> Page:
          html = self.parser.get_html(url)
          title = self.parser.parse_title(html)
          return Page(url = url, title = title)