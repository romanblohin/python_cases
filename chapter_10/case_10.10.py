
def count_words(filename, word):
	'''Функция получает имя файла, подсчитывает сколько раз 
	указанное слово встречается в тексте '''

	with open(filename) as file_object:
		contents = file_object.read()

	print(f"В файле {filename} слово {word} встречается {contents.lower().count(word)}")

files = ['alice.txt', 'little_women.txt', 'moby_dick.txt', 'siddhartha.txt']
directory = 'txt/'

for file in files:
	count_words( directory + file, 'the')
print("")
for file in files:
	count_words( directory + file, 'the ')

