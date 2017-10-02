#!/usr/bin/env python
import sys
ct  = 	'52112515_4535_331534'\
		'442315_321144422453_2443_114234453314_543445'\
		'213431313452_442315_421112122444'\
		'543445_2134453314_2444_331534'\
		'442315_21311122_2443_2433_4423244214_31243315'\

bigrams = {}
global subst_table
print ct.replace("_", " ")
ct2 = ct.replace("_", "")
print ct2
def create_bigrams():
	for index in range(0,len(ct2),2):
		bigram = ct2[index:index+2]
		#print bigram
		if bigram in bigrams:
			bigrams[bigram] +=1
		else:
			bigrams.update({bigram : 1})

	print "DIctionary with values created"
	for key, value in sorted(bigrams.iteritems(), key=lambda (k,v): (v,k)):
		print "%s: %s" % (key, value)

	print "-------------------------"

def adjust():
	index = 0
	subst_table = {}
	for item in bigrams:
		subst_table[item] = chr(97+ index)
		index +=1
	subst_table['11']='a' #found
	subst_table['25']='k' #found
	subst_table['12']='b' #found
	subst_table['15']='e' #found
	subst_table['14']='d' #found
	subst_table['22']='g' #found
	subst_table['23']='h' #found.
	subst_table['33']='n' #found
	subst_table['32']='m' #found
	subst_table['44']='t' #found
	subst_table['45']='u' #found
	subst_table['42']='r' #found
	subst_table['43']='s' #found
	subst_table['35']='p' #found
	subst_table['34']='o' #found
	subst_table['53']='x' #found
	subst_table['24']='i' #found
	subst_table['54']='y' #found
	subst_table['52']='w' #found
	subst_table['31']='l' #found
	subst_table['21']='f' #found

	'''
	ct  = '52112515_4535_331534'\
		'442315_321144422453_2443_114234453314_543445'\
		'213431313452_442315_421112122444'\
		'543445_2134453314_2444_331534'\
		'442315_21311122_2443_2433_4423244214_31243315'\
		wake_up_neo_
		the_matrix_is_around_you
		follow_the_rabbit
		you_found_it_neo_
		the_flag_is_in_third_line

	'''
	print subst_table
	ct3 = ['0' for x in range(len(ct2)/2 +1)]
	index2=0
	for index in range(0,len(ct2),2):
		bigram = ct2[index:index+2]
		if  bigram in subst_table:
			ct3[index2] = subst_table[bigram]
			index2 +=1
	
	print ct3
	print "Decrypt attempt:"
	for char in ct3:	
		sys.stdout.write(char)

	print "\n"

if __name__ == '__main__':
	create_bigrams()
	adjust()