import sqlite3
import requests
from bs4 import BeautifulSoup


def getdata(url):
    r = requests.get(url)
    return r.text


con = sqlite3.connect('../cogs/fight.db')
cur = con.cursor()


def options_list(list_name):
    list_name = []
    for row in cur.execute('SELECT * FROM debate'):
        r = row
        list_name.append(r[1])
    return list_name

cur.execute('''CREATE TABLE debate (topic, name)''')


topic_add = 'animals'


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
            name_add = image_link
            options = options_list(topic_add)

            if options.count(name_add) > 0:
                print('already in list')
                pass
            else:
                cur.execute(f"INSERT INTO debate VALUES ('{topic_add}','{name_add}')")
                print(f"{name_add} added")
                #con.commit()
    else:
        pass



