from nltk.tokenize import word_tokenize
from nltk.util import ngrams
import csv
import nltk



# Visualizing the dictionaries! (For Testing Purposes)
#####################################################################
import uuid
import tkinter as tk
from tkinter import ttk


def j_tree(tree, parent, dic):
    for key in sorted(dic.keys()):
        uid = uuid.uuid4()
        if isinstance(dic[key], dict):
            tree.insert(parent, 'end', uid, text=key)
            j_tree(tree, uid, dic[key])
        elif isinstance(dic[key], tuple):
            tree.insert(parent, 'end', uid, text=str(key) + '()')
            j_tree(tree, uid,
                   dict([(i, x) for i, x in enumerate(dic[key])]))
        elif isinstance(dic[key], list):
            tree.insert(parent, 'end', uid, text=str(key) + '[]')
            j_tree(tree, uid,
                   dict([(i, x) for i, x in enumerate(dic[key])]))
        else:
            value = dic[key]
            if isinstance(value, str):
                value = value.replace(' ', '_')
            tree.insert(parent, 'end', uid, text=key, value=value)


def tk_tree_view(data):
    # Setup the root UI
    root = tk.Tk()
    root.title("tk_tree_view")
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # Setup the Frames
    tree_frame = ttk.Frame(root, padding="3")
    tree_frame.grid(row=0, column=0, sticky=tk.NSEW)

    # Setup the Tree
    tree = ttk.Treeview(tree_frame, columns=('Values'))
    tree.column('Values', width=100, anchor='center')
    tree.heading('Values', text='Values')
    j_tree(tree, '', data)
    tree.pack(fill=tk.BOTH, expand=1)

    # Limit windows minimum dimensions
    root.update_idletasks()
    root.minsize(root.winfo_reqwidth(), root.winfo_reqheight())
    root.mainloop()

# Caller: 
# tk_tree_view(data)
#####################################################################



# Implementation
#####################################################################

# Header for the csv
head = ['Incident Ticket Number','Incident Service Type','Original Summary','Stemmed Summary','1-Gram','2-Gram','3-Gram','4-Gram','5-Gram','6-Gram','7-Gram',]


# Returns a list of n word grams according to the given text
def get_ngramlist(text, n):
	NgLst = []
	x = 1
	while (x <= n):
		n_grams = ngrams(word_tokenize(text), x)
		NgLst.append(list([ ' '.join(grams) for grams in n_grams]))
		x += 1
	return NgLst


# Extract rows from sheet_data and returns a matrix version containing
# list of lists
def extract_rows(sheet_data):
    lst = []
    for row in sheet_data:
    	print("Extracting Data....")
    	lst.append(row)
    return lst


# writes data in a csv row by row with header head
def writecsv(head, data, wfile):
	wfile.writerow(head)
	for r in data:
		print('Almost Done....')
		print('----------------')
		wfile.writerow(r)


# Searches through a list of n-Grams and returns a list of
# n-grams containing the Key
def FindGram(key, lst):
	match = []
	for l in lst:
		if len(list(key.split(' '))) == 1:
			if key in list(l.split(' ')):
				match.append(l)
		else:
			if key in l:
				match.append(l)
	return match


# Creates a dictionary tree of all the n-grams. You can view the dictionary using the
# "Visualizing the Dictionary" code above
def MakeGram(pre, NGL, q):
	if len(NGL) <= q+1:
		return {}
	for NthGram in  pre:
		print("Finding Relations Between Grams....")
		log = FindGram(str(NthGram), NGL[q+1])
		temp = MakeGram(dict.fromkeys(log, None), NGL, q+1)
		pre[NthGram] = temp
	return pre


# Converts the dictionary into a list of list to be written onto the csv
def d2l(d, cur=()):
    if not d:
        yield list(cur)
    else:
        for n, s in d.items():
            for log in d2l(s, cur+(n,)):
            	yield list(log)


# Adds then Incident Number 
def AddINC(INC,LoL):
	r = []
	for L in LoL:
		print('Making Sure data is accurate...')
		r.append(INC + L)
	return r


# Main Function: reads data from giving csv and creates a new sheet
# containg 1 to max_ngrams 
def Start_Process(input_filename, max_ngram):
	read_file = open(input_filename + '.csv', 'r', encoding="latin1")
	csv_read = csv.reader(read_file)
	write_file = open(input_filename + '_ngarms' + '.csv', 'w', newline='', encoding="latin1")
	csv_write = csv.writer(write_file)
	sheet_data = extract_rows(csv_read)[1:]
	new_data = []
	for row in sheet_data:
		temp = []
		temp += row[1:5]
		NgramList = get_ngramlist(row[4],max_ngram)
		MainKeys = dict.fromkeys(NgramList[0], None)
		NestedDict = MakeGram(MainKeys, NgramList, 0)
		lol = d2l(NestedDict)
		new_data += AddINC(temp,lol)
	writecsv(head, new_data, csv_write)
	print('Your New File is Ready!')
	read_file.close()
	write_file.close()
    	

# caller command; contains the path to the source file and max ngram required
Start_Process("\\\\officescchome28.office.adroot.bmogc.net\scc28userdata$\\asaee01\home\Text Analysis for top 3 Products\\new\\Windows 7", 7)



# Testing! (Please Ignore)
###################################################################
# abcd = get_ngramlist("I have something to say", 7)
# x = dict.fromkeys(abcd[0], None)
# g = MakeGram(x, abcd, 0)
# print('AAAAAANNNNNNNSSSSSS')
# print(g)
# tk_tree_view(g)
# print("$$$$$$$$$$$$$$$$$$$$$$$$$$")
# lolod = list(d2l(g))
# print(lolod)
# p = "\\\\officescchome28.office.adroot.bmogc.net\scc28userdata$\\asaee01\home\Text Analysis for top 3 Products\\new\\checking.csv"
# wrte = open(p,'w',newline='',encoding='latin1')
# w = csv.writer(wrte)
# writecsv(head, lolod, w)
# print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
# for a in loe:
# 	print(str(a))
###################################################################

# Contact Ali if you need help regarding this script!
