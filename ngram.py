from nltk.tokenize import word_tokenize
from nltk.util import ngrams
import csv
import nltk
from itertools import zip_longest

# Return n word grams according to the given text
def get_ngrams(text, n ):
    n_grams = ngrams(word_tokenize(text), n)
    return [ ' '.join(grams) for grams in n_grams]
  
# Extract rows from sheet_data and returns a matrix version containing
# list of lists
def extract_rows(sheet_data):
    lst = []
    for row in sheet_data:
        lst.append(row)
    return lst

#transposes a list of lists
def transposed(lists, defval=0):
   return list(zip_longest(*lists))

# writes data in a csv row by row with header head
def writecsv(head, data, wfile):
	wfile.writerow(head)
	for r in data:
		wfile.writerow(r)

# Main Function: reads data from giving csv and creates a new sheet
# containg 1 to max_ngrams 
def get_data(input_filename, max_ngram):
	read_file = open(input_filename + '.csv', 'r', encoding="latin1")
	csv_read = csv.reader(read_file)
	write_file = open(input_filename + '_ngarms' + '.csv', 'w', newline='', encoding="latin1")
	csv_write = csv.writer(write_file)
	sheet_data = extract_rows(csv_read)[1:]
	header = []
	new_data = []
	while (max_ngram > 0):
		header.append(str(max_ngram) + '_gram')
		temp = []
		for row in sheet_data:
			if (len(row[3].split(' ')) < max_ngram): continue
			temp += get_ngrams(row[3], max_ngram)
		new_data.append(temp)
		max_ngram -= 1
	writecsv(header, list(transposed(new_data)), csv_write)
	read_file.close()
	write_file.close()
    	

# caller command, contains the path to the source file and max ngram required
get_data("\\\\officescchome28.office.adroot.bmogc.net\scc28userdata$\\asaee01\home\Python Scripts\Text Analysis\\new", 7)






