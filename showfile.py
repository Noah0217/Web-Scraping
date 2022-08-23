from requests_html import HTMLSession

s = HTMLSession()
r = s.get('https://books.toscrape.com/')


sel = 'title'

print(r.html.find(sel))