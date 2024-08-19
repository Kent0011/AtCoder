import os
import subprocess

print('contest name') 
contest_name = input()

current = os.path.dirname(__file__)

subprocess.call(['acc', 'new', contest_name, '-c', 'all'],cwd=rf'{current}/..')

template = open(f'{current}/template.py','r')
t = template.read()

Contests = filenames = [f.name for f in os.scandir(f'{current}/../{contest_name}') if f.is_dir()]


for contest in Contests:

    f = open(f'{current}/../{contest_name}/{contest}/main.py','w')

    f.write(t)

    f.close()

template.close()