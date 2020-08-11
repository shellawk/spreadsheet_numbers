num = int(input('Enter column number: '))

column_lst = []

def converter(number):
	number -= 1
	
	rem = number % 26
	
	letter = chr(rem + 65)
	
	return letter

while num != 0:
	column_lst.append(converter(num))
	
	num = int(num / 26)

column_lst = column_lst[::-1]
column = ''.join(column_lst)

print(column)