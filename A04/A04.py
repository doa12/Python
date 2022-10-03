playing = True

while playing:
	a = int(input("Choose a number:\n"))
	b = int(input("Choose another one:\n"))
	operation = input(
		"Choose an operation:\n    Options are: + , - , * or /.\n    Write 'exit' to   finish.\n"
	)

	# add your code here!
	if operation == '+':
			print('Result:\n', a + b, '\n=========================================')
	elif operation == '-':
			print('Result:\n', a - b, '\n=========================================')
	elif operation == '*':
			print('Result:\n', a * b, '\n=========================================')
	elif operation == '/':
			print('Result:\n', a / b, '\n=========================================')
	elif operation == 'exit':
			print('=========================================\n', 'Bye~')
			playing = False