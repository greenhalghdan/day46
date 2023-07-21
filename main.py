from bs4 import BeautifulSoup
import requests


year = input("what your would you like to go back to(YYYY-MM-DD)")

response = requests.get("https://www.billboard.com/charts/hot-100/2000-08-12")

