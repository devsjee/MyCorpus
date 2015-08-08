import string
import pylab
import matplotlib

#vocab is the global dict containing the words and their frequency of occurence in the corpus
VOCAB ={}

#fnames is the the total list of files from which input is processed
fnames =['f1.txt']
N = 4

#corpus is the string form of all text files processed so far
CORPUS =""

#input is the current corpus but with spaces removed
INPUT = ""

def process_text(fname):
	'''fname is the string form of the file name to be opened and processed for corpus
	the text is processed to remove the punctuation present in string.punctuation
	also it is converted to lowercase
	'''
	data = ""
	with open(fname,'r') as f:
		data = f.readlines()

	if type(data) == list:
		data = str(data[0])

	assert(type(data) == str),"Data read from text is not in text format"

	for punc in string.punctuation:
		data = data.replace(punc,' ')

	data = data.lower()

	return data

def update_vocab(text):
	'''input : text in string format
	takes the words from text and updates the frequency in global variable VOCAB
	'''
	global VOCAB

	words = text.split(' ')
	for word in words:
		if word != ' ' and word != '':
			count = VOCAB.get(word,0)
			VOCAB[word] = count+1

	
def add_to_corpus(fname):
	''' fname: file name in string format
	modifies the global variable CORPUS and also updates the VOCAB
	'''
	global CORPUS
	temp= process_text(fname)

	CORPUS+= " "+temp

	update_vocab(temp)


def plot_vocab_hist(fname):
	'''plots the histogram of the frequencies of current vocabulary 
	'''
	global VOCAB

	vocab_list =[]
	for key in VOCAB:
		vocab_list.append((VOCAB[key],key))
		print key+ " "+ str(VOCAB[key])

	vocab_list.sort()
	norm = vocab_list[-1][0]

	freq = [x[0] for x in vocab_list]

	pylab.figure()

	#bins =[1,50,100,150,200,250,300,400,500,1000,1500,2000]
	#n,bins,patches = pylab.hist(freq,bins,normed=0,histtype='bar')

	pylab.hist(freq)
	pylab.xlabel('frequency')
	pylab.ylabel('frequency of frequency')
	pylab.title('Corpus frequency distribution after adding '+fname)

	pylab.show()

def main():
	for i in range(1,N+1):
		fname = "f"+str(i)+".txt"
		process_text(fname)
		add_to_corpus(fname)
		plot_vocab_hist(fname)		

if __name__ == '__main__':
	main()
