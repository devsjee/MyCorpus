import string

CORPUS = ""
vocab = []

def load_vocab(fname):
	'''returns a list of unique words
	'''

	data = ""
	with open(fname,'r') as f:
		data = f.read()
	words = data.split('\n')

	return words

def add_sentence(sent):
	''' sent is a string with words separated by spaces
		returns true if more than 50 percent of the words are form
		the loaded vocab
	'''

	global vocab


	words = sent.split(' ')
	total = len(words)
	count = 0
	for word in words:
		
		if word in vocab:
			count+=1

	if count*1.0/total > 0.5:
		return True
	else:
		return False
	


def process_text(fname):
	'''fname is the string form of the file name to be opened and processed for corpus
	the text is processed to remove the punctuation present in string.punctuation
	also it is converted to lowercase
	'''

	global CORPUS

	data = ""
	with open(fname,'r') as f:
		data = f.readlines()

	if type(data) == list:
		data = str(data[0])

	assert(type(data) == str),"Data read from text is not in text format"

	for punc in string.punctuation:
		if punc != "." :
			data = data.replace(punc,' ')

	data = data.lower()

	sents = data.split('.')
	
	for sent in sents:
		if add_sentence(sent):
			CORPUS += " "+sent


def main():
	global vocab
	vocab = load_vocab('vocab')
	process_text('editorial.txt')
	print 'corpus is ' ,CORPUS
	print len(CORPUS)

	with open('check1.txt','w') as f:
		f.writelines(CORPUS)

if __name__ == '__main__':
	main()
