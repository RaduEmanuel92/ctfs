#!/usr/bin/env python
import sys
ct  = 	"KRSWE4TJNNWGK4RBEBAW2YJAMJ2SA23BMRQXEIDLN5WGC6JAN5WG2YLZMFRWC2ZAHIUSACQKKZDVM2LDNVWHEYSHKZ4USRDPOBEUKSRRMJXFKZ3BI5DHESKHKYYGIR3MOVEUGMBLKBVDIZ2SNN4EEURTORFFQMKJPJJDCSL2KZDDSR2VNJBE4WBQJJBFKMCVGJHEQMB"

bigrams = ["TH", "HE", 'IN', 'OR', 'HA', 'ET', 'AN', 'EA', 'IS', 'OU', 'HI', 'ER', 'ST', 'RE', 'ND']

# this is the list of monograms, from most frequent to less frequent
monograms = ['E', 'T', 'A', 'O', 'I', 'N', 'S', 'R', 'H', 'D', 'L', 'U', 'C', 'M', 'F', 'Y', 'W', 'G', 'P', 'B', 'V', 'K', 'X', 'Q', 'J', 'Z']
print ct 

ct2 = ct
bigrams = {}
global subst_table


def create_bigrams():
	for index in range(0,len(ct2)):
		bigram = ct2[index]
		#print bigram
		if bigram in bigrams:
			bigrams[bigram] +=1
		else:
			bigrams.update({bigram : 1})

	print "Dictionary with values created"
	for key, value in sorted(bigrams.iteritems(), key=lambda (k,v): (v,k)):
		print "%s: %s" % (key, value)

	print "-------------------------"

def adjust():
	index = 0
	subst_table = {}

	subst_table['A'] = 'K'
	subst_table['B'] = 'N'
	subst_table['C'] = 'S'
	subst_table['D'] = 'W'
	subst_table['F'] = 'C'
	subst_table['G'] = 'V'
	subst_table['J'] = 'G'
	subst_table['I'] = 'Y'
	subst_table['K'] = 'T'
	subst_table['M'] = 'D'
	subst_table['N'] = 'I'
	subst_table['P'] = 'W'
	subst_table['Q'] = 'E'
	subst_table['R'] = 'H'
	subst_table['S'] = 'U'
	subst_table['T'] = 'A'
	subst_table['U'] = 'G'
	subst_table['W'] = 'R'
	subst_table['X'] = 'F'
	subst_table['Y'] = 'B'
	subst_table['E'] = 'L'

	print subst_table
	ct3 = ['0' for x in range(len(ct2)+1)]
	index2=0
	for index in range(0,len(ct2)):
		bigram = ct2[index]
		if  bigram in subst_table:
			ct3[index2] = subst_table[bigram]
			index2 +=1
	
	print ct3
	print "Decrypt attempt:"
	for char in ct3:	
		sys.stdout.write(char+ ' ')

	print "\n"

if __name__ == '__main__':
	create_bigrams()
	adjust()