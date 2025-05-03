from bs4 import BeautifulSoup
import requests
class PageParser:
     def get_html(self, url: str) -> str:
          r = requests.get(url)
          r.raise_for_status()
          return r.text
     
     def parse_title(self, html: str) -> str:
          soup = BeautifulSoup(html, "lxml")
          return soup.title.string.strip()