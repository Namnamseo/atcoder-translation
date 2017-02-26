from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
	def __init__(self):
		super(MyHTMLParser, self).__init__()
		self.md = ''
		self.convert_charrefs = True
		self.started = False
		self.ended = False
		self.lvl = 0
		self.ignore = False

	def add(self, s):
		self.md += s

	def handle_starttag(self, tag, attrs):
		if tag == 'h2':
			self.started = True

		if not self.started or self.ended or self.ignore: return
		self.lvl += 1

		if len(tag)==2 and tag[0]=='h' and tag[1] in '123456':
			self.add('#' * int(tag[1]))

		if tag == 'span':
			if 'lang-en' in attrs:
				self.ignore = True

	def handle_endtag(self, tag):
		if not self.started or self.ended: return
		if tag == 'span':
			self.ignore = False
		

		self.lvl -= 1
		if self.lvl == 0 and tag == 'div':
			self.ended = True
			return

		if len(tag)==2 and tag[0]=='h' and tag[1] in '123456':
			self.add('\n\n')

	def handle_data(self, data):
		if not self.started or self.ended: return
		self.add(data)

def parse_atcoder_task(body):
	parser = MyHTMLParser()
	parser.feed(body)
	return parser.md