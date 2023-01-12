# Program to delete unneeded files

import os , argparse

parse = argparse.ArgumentParser(description = "Directory to scan")
parse.add_argument('-d' ,action = 'store' , required = True , dest = 'directory')

args = parse.parse_args()
os.chdir(args.directory)

for x in os.listdir(args.directory):
	if os.path.isfile(x) and os.path.getsize(x)  > 104857600:
		print(x)
		#os.unlink(x)

