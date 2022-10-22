from copy import deepcopy
def solve(s):
	# print(s)
	n_s = deepcopy(s)
	# print(n_s)
	m_dicti = {">": "<", "/": "\\", ")": "(", "<": ">", "\\": "/", "(": ")"}
	# top 
	n_s[0],n_s[2] = s[2],s[0]
	n_s[4],n_s[6] = s[6],s[4]
	n_s[8],n_s[10] = s[10],s[8]
	for i,limb in enumerate(n_s):
		if limb in m_dicti.keys():
			n_s[i] = m_dicti[limb]
			

		# if s[4] == " ":
		# 	n_s[6] =" "
		# elif s[4] == "<":
		# 	n_s[6] = ">"
		# elif s[4] == "/":
		# 	n_s[6] == "\\"		 
	# print(''.join(n_s))
	# print(n_s)
	return n_s


def m_paser(t_line,p_hlias):
	# is it command?
	if t_line[0] == "say":
		print(' '.join(t_line[1:]))
	else:
		p_hlias  = action(t_line[-4:],p_hlias)
		print(''.join(p_hlias))
	return p_hlias

def action(command,p_hlias):
	# do i turn?
	if command[0] == "turn":
		p_hlias = solve(p_hlias)
		return p_hlias
		
	# leg or hand decision
	if command[1] == 'leg':
		# print("leg command")
		if command[0] == 'right':
			if command[2] == 'in':
				p_hlias[8] = "<"
			else:
				p_hlias[8] = "/"
		else:
			if command[2] == 'in':
				p_hlias[10] = ">"
			else:
				p_hlias[10] = "\\"
			pass


	else:
		if command[0] == "right":
			if command[3] == "head":
				p_hlias[4] = ' '
				p_hlias[0] = '('
			elif command[3] == "hip":
				p_hlias[4] = '<'
				p_hlias[0] = ' '
			else:
				p_hlias[4] = '/'
				p_hlias[0] = ' '

		else:
			if command[3] == "head":
				p_hlias[6] = ' '
				p_hlias[2] = ')'

			elif command[3] == "hip":
				p_hlias[6] = '>'
				p_hlias[2] = ' '

			else:
				p_hlias[6] = '\\'
				p_hlias[2] = ' '

		# print("hand command")
		# print(command)
	# print(''.join(p_hlias))
	return p_hlias

def main():
	f = open("in.txt", "r")
	test_cases = int(f.readline())
	hlias = " o \n/|\\\n/ \\"
	hlias = list(hlias)
	for _i in range(test_cases):
		querries = int(f.readline())
		for _j in range(querries):
			t_line = f.readline().split()
		
			hlias = m_paser(t_line,hlias)
			# print(''.join(hlias))
	# print(hlias)

if __name__ == '__main__':
	main()