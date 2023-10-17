from html.parser import HTMLParser

class Parser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f'Start : {tag}')
        if attrs != []:
            for attr in attrs:
                print(f'-> {attr[0]} > {attr[1]}')

    def handle_endtag(self, tag):
        print(f'End   : {tag}')

    def handle_startendtag(self, tag, attrs):
        print(f'Empty : {tag}')
        if attrs != []:
            for attr in attrs:
                print(f'-> {attr[0]} > {attr[1]}')

N = int(input())
html = '\n'.join([input() for _ in range(N)])
parser = Parser()
parser.feed(html)
