class Parenthesis:
	def __init__(self,my_string):
		self.my_string=my_string
	def is_valid(self):
		open= ["[", "{", "("]
		close = ["]", "}", ")"]
		stk=[]
		for i in self.my_string:
			if i in open:
				stk.append(i)
			elif i in close:
				pos = close.index(i)
				if ((len(stk) > 0) and
					(open[pos] == stk[len(stk)-1])):
					stk.pop()
				else:
					return "Invalid"
		if len(stk) == 0:
			return "Valid"
		else:
			return "Invalid"

p1=Parenthesis("(){}[]")
print(p1.is_valid())

p2=Parenthesis("({}[]")
print(p2.is_valid())