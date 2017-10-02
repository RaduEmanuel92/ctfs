# Code for solving Much Ado About Hacking

def adoHack(s):
	ben = s
	bea = 0
	john = 0
	pedro = 0
	ach = 32
	cleo = 128 - 32 #96
	string = ""
	for i in range(len(ben)):
		b = ord(ben[len(ben)-1-i])
		b = b - ach
		john = b
		b = b + pedro
		b = b % cleo
		pedro = john
		b = b + ach
		string += chr(b)
	return string

def reverseHack(s):
	rev = s
	bea = 0
	john = 0
	pedro = 0
	ach = 32
	cleo = 128 - 32
	string = ""
	for i in range(len(rev)):
		b = ord(rev[i])
		b = b - ach
		b = b - pedro
		john = b
		pedro = john
		b = b + ach
		while ( b < 40 ):
		#	nu ma intreba de ce merge
		#	but it works
		#	@intuition.gut
			b = b + cleo
		while ( b > 122 ):
    # hacker_life
			b = b - cleo
		string += chr(b)
	return string[::-1]

ben = ""
#ben = raw_input("read string> ")
#ben = ben.split(" ")[0]

#print ben

#test = adoHack(ben)
#print test
#print reverseHack(test)

#print reverseHack(ben)

end = "tu1|\h+&g\OP7@% :BH7M6m3g="
print reverseHack(end)
