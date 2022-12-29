#there seems to be a tool for that task
#called moses. (smt)
import string
IFILE= './book_copy.txt'

CODE = {' ': '_', 
	"'": '.----.', 
	'(': '-.--.-', 
	')': '-.--.-', 
	',': '--..--', 
	'-': '-....-', 
	'.': '.-.-.-', 
	'/': '-..-.', 
	'0': '-----', 
	'1': '.----', 
	'2': '..---', 
	'3': '...--', 
	'4': '....-', 
	'5': '.....', 
	'6': '-....', 
	'7': '--...', 
	'8': '---..', 
	'9': '----.', 
	':': '---...', 
	';': '-.-.-.', 
	'?': '..--..', 
	'A': '.-', 
	'B': '-...', 
	'C': '-.-.', 
	'D': '-..', 
	'E': '.', 
	'F': '..-.', 
	'G': '--.', 
	'H': '....', 
	'I': '..', 
	'J': '.---', 
	'K': '-.-', 
	'L': '.-..', 
	'M': '--', 
	'N': '-.', 
	'O': '---', 
	'P': '.--.', 
	'Q': '--.-', 
	'R': '.-.', 
	'S': '...', 
	'T': '-', 
	'U': '..-', 
	'V': '...-', 
	'W': '.--', 
	'X': '-..-', 
	'Y': '-.--', 
	'Z': '--..', 
	'_': '..--.-'}
 
def convertToMorseCode(sentence):
	sentence = sentence.upper()
	encodedSentence = ""
	for character in sentence:
		if character in string.ascii_letters+string.digits:
			encodedSentence += CODE[character]
	return encodedSentence

SEQUENCE ='x.xx...x.xxx..-xx-.xxxx.-.-xxx.-.x..x.xxxx..x.xxx.-.-.xx-.-xxx..-.xx.x.x.--x.xxx'

def check(s1,seq):
	for i in range(len(seq)):
		if seq[i] != 'x':
			if SEQUENCE[i] != s1[i]:
				return False
	return True
		

with open(IFILE,'r') as f:
	book = f.read()
	book_splitted = book.split()
	book_stripped = ''.join(book.split())
morse_splitted = []
for w in book_splitted:
	morse_splitted.append(convertToMorseCode(w))


pos = 0
fixed_seq = ''
for i in range(len(morse_splitted)):
	morse_seq = ''.join(morse_splitted[i:i+10])[:len(SEQUENCE)]
	if check(morse_seq,SEQUENCE):
		print(f"found sequence at:{i}")
		print(morse_seq)
		fixed_seq = morse_seq
		pos = i
		break
				

if fixed_seq:
	n_words =0
	seq_len = len(fixed_seq)
	while seq_len:
		seq_len-= len(morse_splitted[pos+n_words])
		n_words+=1

	print('CSA{' +'_'.join(book_splitted[pos:pos+n_words]).strip(',')+'}')
