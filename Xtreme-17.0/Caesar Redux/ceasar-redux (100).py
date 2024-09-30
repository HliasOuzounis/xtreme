def solution(num , message):
	# if there is the word "the" in the message its decoded
	# encrypted message is shifted by num
	encrypt_num = 26 - num
	decrypt_num = num
	# if the output is the word the then it is decoded


	if (("the " == message[:4])  or (" the" in message[-4:]) or (" the " in message) or ("the" == message)):
			return_message = ''
			for letter in message:
				if letter.isalpha():
					return_message += chr(((ord(letter) - 97 + encrypt_num) % 26) + 97)
				else:
					return_message += letter
			return return_message
	else:
		return_message = ''

		for letter in message:
				if letter.isalpha():
					return_message += chr(((ord(letter) - 97 + decrypt_num) % 26) + 97)
				else:
					# if its not a letter just add it
					return_message += letter
		return return_message
	

# a simple parser for python. use get_number() and get_word() to read
def parser():
	while 1:
		data = list(input().split(' '))
		for number in data:
			if len(number) > 0:
				yield(number)   



def get_word():
	global input_parser
	return next(input_parser)

def get_number():
	data = get_word()
	try:
		return int(data)
	except ValueError:
		return float(data)

def parser_input():
		
	testcases = int(input())
	for testcase in range(testcases):
		shiftnum = int(input())
		message = input()
		print(solution(shiftnum, message))
	pass
input_parser = parser()
parser_input()

def tester_input():
	inp1 = 19
	mess1 = "we accept the ieeextreme challenge"
	print(solution(inp1, mess1))
	inp2 = 19
	mess2 = "qbspbz jhlzhy olsk aol vmmpjl vm wvuapmle theptbz wypvy av iljvtpun kpjahavy" 
	print(solution(inp2, mess2))
		
