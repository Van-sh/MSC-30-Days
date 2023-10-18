from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(selg, tag, attrs):
        print(tag)
        for attr in attrs:
            print(f'-> {attr[0]} > {attr[1]}')


N = int(input())
html = '\n'.join([input() for _ in range(N)])
parser = MyHTMLParser()
parser.feed(html)
parser.close()