# A program that finds files with extension .py and .txt and puts them in a zip file
import zipfile , os , re

os.chdir("C:\\Users\\bilai\\Videos\\Python Practices\\Networking")
zips = zipfile.ZipFile('new.zip' , 'w')
for i , y , z in os.walk(r'C:\\Users\\bilai\\Videos\\Python Practices\\Networking'):
	for files in z:
		pattern = re.compile(r'\w+(.)(py|txt)$')
		pattern = pattern.search(files)
		try:
			zips.write(pattern.group() , compress_type = zipfile.ZIP_DEFLATED)
		except AttributeError:
			pass
zips.close()

