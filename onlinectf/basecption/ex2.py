#!/usr/bin/env python
from caesar import *
from collections import defaultdict
from itertools import izip, islice
import operator
# Psalm 1:1

# this is the list of bigrams, from most frequent to less frequent
bigrams = ["TH", "HE", 'IN', 'OR', 'HA', 'ET', 'AN', 'EA', 'IS', 'OU', 'HI', 'ER', 'ST', 'RE', 'ND']

# this is the list of monograms, from most frequent to less frequent
monograms = ['E', 'T', 'A', 'O', 'I', 'N', 'S', 'R', 'H', 'D', 'L', 'U', 'C', 'M', 'F', 'Y', 'W', 'G', 'P', 'B', 'V', 'K', 'X', 'Q', 'J', 'Z']

# this is the dictionary containing the substitution table (e.g. subst_table['A'] = 'B'}
# TODO fill it in the create_subst_table function
subst_table = {}

# these are the dictionaries containing the frequency of the mono/bigrams in the text
# TODO fill them in the analize function
freq_table_bi = {}
freq_table_mono = {}

# sorts a dictionary d by the value
def sort_dictionary(d):

    sorted_dict = list(reversed(sorted(d.items(), key=operator.itemgetter(1))))
    return sorted_dict

# computes the frequencies of the monograms and bigrams in the text
def analize(text):
    global freq_table_bi
    global freq_table_mono

    freq_table_mono = defaultdict(int)
    freq_table_bi   = defaultdict(int)

    print "[+] Compute freqencies from document."
  
    for mon in text :
        freq_table_mono[mon] +=1

    for i in range(len(text)-1):
        bi = text[i] + text[i+1]''
        freq_table_bi[bi] +=1
    

    print "[+] Sort frequencies."


    freq_table_mono = sort_dictionary(freq_table_mono) 
    freq_table_bi = sort_dictionary(freq_table_bi)  
    print "[+] Bigram frequencies:\n"  
    for key, value in freq_table_bi:
        print "%s: %s" % (key, value)
    print "[+] Mono frequencies:\n"  
    for key, value in freq_table_mono:
        print "%s: %s" % (key, value)


# creates a substitution table using the frequencies of the bigrams
def create_subst_table():
    global subst_table

    print "[+] Create substitution table"
    print "[+] Adding bigrams..."
    for mona in range(10000000):
        mona = mona

    freqs_bi_fromtext = [i[0] for i in freq_table_bi]

    for i, j in zip(bigrams,freqs_bi_fromtext) :
        subst_table[i] = j
    
def complete_subst_table():
    global subst_table
    
    print "[+] Adding monograms..."
   
    
    freqs_mono_fromtext = [i[0] for i in freq_table_mono]
    for i, j in zip(monograms,freqs_mono_fromtext) :
        subst_table[i] = j
    
    print '[+] First substitution table compiled: '    
    print subst_table
    
def adjust():

    global subst_table
    print "[+] Adding adjustments to substitution table..."
 
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

def decrypt_text(text):
    global subst_table
    print "[+] Initiating decrypting operation..."

    # TODO 4 decrypt and print the text using the substitution table
    # modifying touples

    print "[+] First decryption:"

    decrypted = [ (i+j)  for i ,j in zip(text[::2], text[1::2])]
    for index_bi in range(len(decrypted)):
        if decrypted[index_bi] in bigrams:
          decrypted[index_bi] = subst_table[decrypted[index_bi]]
   
    text_fin = ''
    for i in decrypted:
      text_fin += i    
    print text_fin    

    #modifing monograms
    print "[+] Second decryption:"

    decrypted = [ i  for i  in text]
    for index_mono in range(len(decrypted)):
        if decrypted[index_mono] in subst_table:
          decrypted[index_mono] = subst_table[decrypted[index_mono]]
    
    text_fin = ''
    for i in range(len(decrypted)-1):
            text_fin += decrypted[i]        
    print text_fin 


def main():
    with open('ciphertext.dat', 'r') as myfile:
        text = myfile.read()
    
    analize(text)
    create_subst_table()
    complete_subst_table()
    adjust()
    decrypt_text(text)
  

if __name__ == "__main__":
  main()

Candidate password : apYBg
Candidate password : chZwc
Candidate password : cOphi

Candidate password : dw4Yi
Candidate password : fGCqn
Candidate password : fPybq
Candidate password : jgd2D
Candidate password : kkZe5
Candidate password : mwq6A
Candidate password : oDsVQ
Candidate password : o1dg4
Candidate password : qhJgI
Candidate password : tr8je
Candidate password : vYJLa
Candidate password : zdED0
Candidate password : ztLpk
