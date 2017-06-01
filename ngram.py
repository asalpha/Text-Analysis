from nltk.tokenize import word_tokenize
from nltk.util import ngrams
import csv
import nltk
from itertools import zip_longest


head = ['Incident Ticket Number','Incident Service Type','Original Summary','Stemmed Summary','1-Gram','2-Gram','3-Gram','4-Gram','5-Gram','6-Gram','7-Gram',]


# Returns a list of n word grams according to the given text
def get_ngramlist(text, n ):
	NgLst = []
	x = 1
	while (x <= n):
		n_grams = ngrams(word_tokenize(text), x)
		NgLst.append(list([ ' '.join(grams) for grams in n_grams]))
		x += 1
	# print(NgLst)
	return NgLst
   
# Extract rows from sheet_data and returns a matrix version containing
# list of lists
def extract_rows(sheet_data):
    lst = []
    for row in sheet_data:
        lst.append(row)
    return lst

#transposes a list of lists
def transposed(lists, defval=0):
	new =[]
	x = list(zip_longest(*lists))
	for tup in x:
		new.append(list(tup))
	return new

# writes data in a csv row by row with header head
def writecsv(head, data, wfile):
	wfile.writerow(head)
	for r in data:
		wfile.writerow(r)


def FindGram(p, key, list):
	match = []
	for l in list:
		match.append([s for s in l if key in s])
	return match



# def MakeRow(key, prefix, lookup):
	



def MakeGram(pre, NGL):
	all = []
	# print(NGL[0][0])
	for OneGram in  NGL[0]:
		MatchingGrams = FindGram(pre, OneGram, NGL)
		MakeRow = transposed(MatchingGrams)
		track = 0
		for i in MakeRow:
			if i[0] == None:
				i[0] = OneGram
			all.append(pre + i)
			track += 1
			# print(i)
		# print(MakeRow)
		# all += MakeRow
	print('----------------')
	# print(all)
	return all




# Main Function: reads data from giving csv and creates a new sheet
# containg 1 to max_ngrams 
def get_data(input_filename, max_ngram):
	read_file = open(input_filename + '.csv', 'r', encoding="latin1")
	csv_read = csv.reader(read_file)
	write_file = open(input_filename + '_ngarms' + '.csv', 'w', newline='', encoding="latin1")
	csv_write = csv.writer(write_file)
	sheet_data = extract_rows(csv_read)[1:]
	# print(sheet_data)
	new_data = []
	for row in sheet_data:
		temp = []
		#temp.append(str(count))
		temp += row[1:5]
		NgramList = get_ngramlist(row[4],max_ngram)
		new_data += MakeGram(temp, NgramList)
	writecsv(head, new_data, csv_write)
	read_file.close()
	write_file.close()
    	

# caller command, contains the path to the source file and max ngram required
get_data("\\\\officescchome28.office.adroot.bmogc.net\scc28userdata$\\asaee01\home\Python Scripts\Text Analysis\\Total", 7)






