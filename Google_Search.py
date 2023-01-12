import sys , requests , webbrowser ,  bs4 , math

x = sys.argv

print("Welcome to Tijani's Search Engine".center(70))
print()
print("Searching.......")
print()

res = requests.get('www.google.com/search?= ' + ''.join(x[1:]))
res.raise_status_code()

bs = bs4.BeautifulSoup(res.text)
soup = bs.select('a')

links = min(5 , len(soup))

for i in range(links):
	webbrowser.open('www.google.com' + soup[i].get('href'))
