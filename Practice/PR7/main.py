with open(f'{'books.csv'}', 'r', encoding='utf-8') as file:
    books = file.read().splitlines()
    for i in range(0, len(books)):
        books[i] = books[i].split('|')

def get_books(name):
	exist = 0
	result = []
	for i in range(1, len(books)):
		if str(name).lower() in str(books[i]).lower():
			result.append(books[i])
			exist += 1
	if exist > 0:
		return result
	else:
		print('Такой книги нет в списке')

def get_totals(getBooks):
	result = []
	total = ()
	for i in range (0, len(getBooks)):
		if int(int(getBooks[i][3]) * float(getBooks[i][4])) < 500:
			total = (getBooks[i][0], float(int(getBooks[i][3]) * float(getBooks[i][4])) + 100)
		else:
			total = (getBooks[i][0], float(int(getBooks[i][3]) * float(getBooks[i][4])))
		result.append(total)
	return result

if __name__ == '__main__':
	bookInfo = get_books('python')
	print(bookInfo)
	print(get_totals(bookInfo))
