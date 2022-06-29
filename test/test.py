import sqlite3
#import random

# TODO: Make function for collection of options from one topic
# TODO: Make addition of option for some topic

con = sqlite3.connect('../cogs/fight.db')
cur = con.cursor()

def options_list(list_name):
    list_name = []
    for row in cur.execute('SELECT * FROM debate'):
        r = row
        list_name.append(r[1])
    return list_name


#cur.execute('''CREATE TABLE debate (topic, name)''')
topic_add = 'stuation'
name_add = 'at dancing'

options = options_list(topic_add)

if options.count(name_add) > 0:
    print('already in list')
    pass
else:
    cur.execute(f"INSERT INTO debate VALUES ('{topic_add}','{name_add}')")
    print(f"{name_add} added")
    con.commit()

'''
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