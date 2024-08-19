import os

print('name:') 
dirname = input()

current = os.path.dirname(__file__)

os.mkdir(f"{current}/../{dirname}")

template = open(f'{current}/template.py','r')
t = template.read()

File = ['a.py','b.py','c.py','d.py','e.py','f.py','g.py']

for file in File:

    f = open(f"{current}/../{dirname}/{file}",'w')

    f.write(t)

    f.close()

template.close()