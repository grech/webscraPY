from bs4 import BeautifulSoup
import requests
class PageParser:
     def get_html(self, url: str) -> str:
          headers = {
               "User-Agent": (
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/115.0.0.0 Safari/537.36"
               )
          }
          response = requests.get(url, headers=headers)
          response.raise_for_status()
          return response.text
     
     def parse_title(self, html: str) -> str:
          soup = BeautifulSoup(html, "lxml")
          return soup.title.string.strip()
     
     def parse_h1(self, html: str) -> str:
          soup = BeautifulSoup(html, "lxml")
          h1= "no tiene h1"
          h1 = soup.find("h1")
          print(h1)
          return h1.text.strip() if h1 else "no tiene h1"