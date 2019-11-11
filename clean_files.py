import os
from pathlib import Path

def find_and_store_files(store, directory_in_str, file_type, total):
	pathlist = Path(directory_in_str).glob('**/*{}'.format(file_type))
	for path in pathlist:
		# because path is object not string
		path_in_str = str(path)

		file_name = clean_name(path_in_str)
		store.add(file_name)
		total = delete(path, file_name, store, total)
		return total


def clean_name(name):
	name = name.replace(' ', '')
	name = name.replace('/',' ')
	name = name[::-1]
	name = name.split()[0]
	return name[::-1]


def delete(path, name, store, total):
	if name in store:
		try:
			os.remove(path)
			print('Removed duplicate file: {}'.format(name))
			total += 1

		except:
			print("Couldn't delete {}".format(name))
	return total

def main():
	store = set()
	directory_in_str = '/Users/parthsareen/Documents/file_cleaner'
	#directory_in_str = os.getcwd()
	total = 0
	file_type = input("Enter file type ")

	total = find_and_store_files(store, directory_in_str, file_type, total)
	if total == None:
		total = 0
	print('File cleanup done! Deleted {} files'.format(total))

	yes = True
	while yes:
		total = 0
		user_input = input('Run for another file type? y/n ')
		if user_input == 'y':
			file_type = input("Enter file type ")
			total = find_and_store_files(store, directory_in_str, file_type, total)
			if total == None:
				total = 0
			print('File cleanup done! Deleted {} files'.format(total))
		elif user_input == 'n':
			yes = False

		else:
			print('Input not recognized, please try again')

if __name__ == '__main__':
	main()