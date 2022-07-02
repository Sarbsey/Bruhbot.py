import sqlite3
# import random
import discord
import requests
from bs4 import BeautifulSoup



def getdata(url):
    r = requests.get(url)
    return r.text

# TODO: Make function for collection of options from one topic
# TODO: Make addition of option for some topic


htmldata = getdata("https://a-z-animals.com/animals/")
soup = BeautifulSoup(htmldata, 'html.parser')
link_dict = []
for link in soup.find_all('a'):
    image_link = link.get('href')
    image_link = str(image_link)
    if image_link.startswith('https://a-z-animals.com/animals/'):
        #link_dict.append(image_link)
        image_link = image_link.split('/')[-2]
        if image_link.find('-') == -1:
            print(image_link)
    else:
        pass





'''
con = sqlite3.connect('../cogs/fight.db')
cur = con.cursor()

def options_list(list_name):
    list_name = []
    for row in cur.execute('SELECT * FROM debate'):
        r = row
        list_name.append(r[1])
    return list_name





try:
    cur.execute('''#CREATE TABLE debate (topic, name)''')
'''add = 'chicken'

    cur.execute("INSERT INTO debate VALUES ('animal','dog')")
    cur.execute("INSERT INTO debate VALUES ('animal','cat')")
    cur.execute(f"INSERT INTO debate VALUES ('animal','{add}')")

    con.commit()
    print("table created")
except sqlite3.OperationalError:
    print("table already exists")
    pass

options = []

for row in cur.execute('SELECT * FROM debate'):
    r = row
    options.append(r[1])

option_a = "d"
option_b = "d"
while option_a == option_b:
    option_a = random.choice(options)
    option_b = random.choice(options)

print(option_a, option_b)

for entry in options:
    if entry == "dog":
        print("dog found")
        break
'''