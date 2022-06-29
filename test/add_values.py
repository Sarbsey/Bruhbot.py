import sqlite3


con = sqlite3.connect('../cogs/fight.db')
cur = con.cursor()


def options_list(list_name):
    list_name = []
    for row in cur.execute('SELECT * FROM debate'):
        r = row
        list_name.append(r[1])
    return list_name

# cur.execute('''CREATE TABLE debate (topic, name)''')


topic_add = 'animals'
name_add = 'chinchillas'

options = options_list(topic_add)

if options.count(name_add) > 0:
    print('already in list')
    pass
else:
    cur.execute(f"INSERT INTO debate VALUES ('{topic_add}','{name_add}')")
    print(f"{name_add} added")
    con.commit()
