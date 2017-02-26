import bs4
from bs4 import BeautifulSoup as BS

def subNodes(node, strip_newline=True):
	ret = []
	for c in node.children:
		if type(c) is bs4.element.NavigableString:
			if strip_newline and not str(c).strip():
				continue
			else:
				ret.append(str(c).replace('\r', ''))
		else:
			ret.append(nodeToMarkdown(c))
	return ''.join(ret)

def nodeToMarkdown(node):
	if type(node) is bs4.element.NavigableString: return ''

	if 'class' in node.attrs and 'lang-en' in node.attrs['class']:
		return ''

	name = node.name

	if name[0] == 'h' and name[1] in '123456' and len(name)==2:
		return '#' * int(name[1]) + ' ' + node.string.strip() + '\n\n'

	if name == 'hr':
		return '----------\n\n'

	if name in ['p', 'span', 'div', 'section']:
		ret = subNodes(node)
		if name == 'p': ret = ret.strip() + '\n\n'
		return ret

	if name == 'var':
		return '$' + node.string + '$'

	if name == 'pre':
		if 'class' in node.attrs and 'prettyprint' in node.attrs['class']:
			return '```' + subNodes(node, False) + '```\n\n'
		else:
			return '>' + subNodes(node, False) + '\n\n'

	if name == 'ul':
		return subNodes(node) + '\n'
	if name == 'li':
		return '* ' + subNodes(node, True).strip() + '\n'

	if name == 'code':
		return '`' + subNodes(node, False) + '`'

	if name == 'img':
		if 'atcoder.jp' not in node['src']:
			node['src'] = 'http://abc001.contest.atcoder.jp/' + node['src']
		return str(node)

	if name == 'strong' or name == 'b':
		return '**' + subNodes(node) + '**\n\n'

	if name == 'ol':
		i = 0
		ret = []
		for c in node.children:
			if type(c) is bs4.element.NavigableString: continue
			ret.append('%d. '%(i) + nodeToMarkdown(c))
		return '\n'.join(ret)

	if name == 'br':
		return '\n'

	if name == 'center':
		return str(node)

	if name == 'font':
		return subNodes(node, True)

	raise Exception(name + ' is not implemented.')


def parse_atcoder_task(body):
	soup = BS(body, 'html.parser')
	p = soup.find('h2')

	ret = ''
	while True:
		ret += nodeToMarkdown(p)
		if p.name == 'div' and p.get('id') == 'task-statement': break
		p = p.next_sibling

	return ret