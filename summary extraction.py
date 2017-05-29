import csv
import pandas as pd

n = 1

def addindex():
    global n
    n = n + 1

def extract_summary(product_name):
    w = open("FILEPATH", "w", encoding="utf8", newline = "")
    writer = csv.writer(w)
    f = open(file, encoding="utf8")
    reader = csv.reader(f)
    writer.writerows([["Index", "Incident Ticket Number", "Original Summary", "Stemmed Summary"]])
    Ticketnumbers = set()
    filelist = ["FILEPATH",
                "FILEPATH",
                "FILEPATH",
                "FILEPATH",
                "FILEPATH",
                "FILEPATH",
                "FILEPATH",
                "FILEPATH",
                "FILEPATH",
                "FILEPATH",
                "FILEPATH",
                "FILEPATH"]
    for file in filelist:
        for row in reader:
            if (row[28] == product_name and row[1] not in Ticketnumbers):
                row[0] = n
                row[3:50] = ""
                writer.writerows([row])
                addindex()
                Ticketnumbers.add(row[1])
    f.close()
    w.close()
                        
 
def remove_duplicate_tickets():
    df = pd.read_csv("FILEPATH")
    df = df.drop_duplicates(subset=df.columns[1], keep = "last")
    df.to_csv("FILEPATH")
    
                        
                
def main():
    extract_summary()
             
             