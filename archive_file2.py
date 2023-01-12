import zipfile , os , re

os.chdir("C:\\Users\\bilai\\Documents")
zips = zipfile.ZipFile('new.zip' , 'w')
for x , y , z in os.walk("C:\\Users\\bilai\\Documents\\Unisa files"):
	for files in z:
		pattern = re.compile(r'\w+(.)([^py]|[^txt])$')
		pattern = pattern.search(files)
		try:
			if pattern.group():
				zips.write("C:\\Users\\bilai\\Documents\\Unisa files\\" + files , compress_type = zipfile.ZIP_DEFLATED)
		except AttributeError:
			pass
zips.close()