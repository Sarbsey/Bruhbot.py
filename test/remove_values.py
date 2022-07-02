import sqlite3
import requests
from bs4 import BeautifulSoup


con = sqlite3.connect('../cogs/fight.db')
cur = con.cursor()
cur.execute(f"DELETE FROM debate WHERE name = 'weimardoodle '")
