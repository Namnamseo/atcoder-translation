import requests
import atcoder_parser
import os, shutil

def work(contest, mondai):
	url = 'http://{0}.contest.atcoder.jp/tasks/{0}_{1}'.format(contest, mondai)
	r = requests.get(url, allow_redirects=False)
	if r.status_code != 200:
		return False
	try:
		with open('{}_{}.md'.format(contest, mondai), 'w', encoding='utf-8') as f:
			f.write('[link]({}).\n\n'.format(url))
			f.write(atcoder_parser.parse_atcoder_task(r.text))
	except:
		import webbrowser
		webbrowser.open(url)
		raise
	return True

try: shutil.rmtree('dump')
except: pass
os.mkdir('dump')
os.chdir('dump')

for i in range(20, 30):
	j = 1
	while work('arc{:03d}'.format(i), str(j)):
		j += 1