import re , shutil , os
import argparse

parse = argparse.ArgumentParser(description = 'Directories for destination and working directory')
parse.add_argument('-w' , action = 'store' , dest = 'Working_directory' , required = True)
parse.add_argument('-d' , action = 'store' , dest = 'Destination_directory' , required = True)

given_args = parse.parse_args()


def main(string):
	for i in os.listdir(string):
		Pattern = re.compile(r'([a-z+A-Z0-9]+)(.)(pdf|jpg|png|txt)$')
		Message = Pattern.findall(i)
		print(i)
		lists = []
		for j in range(len(Message)):
			X = ''.join(Message[j])
			lists.append(X)
	return lists
def copy(x,destination):
	for i in main(x):
		destination = os.makedirs(destination)
		shutil.copy(i , destination)
		print("Files moved")
print(main(given_args.Working_directory))
#copy(given_args.Working_directory,given_args.Destination_directory)