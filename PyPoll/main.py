import os
import csv
csvpath = os.path.join("..", "Resources", "election_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    rowcnt = 0
    cand = ""
    cvotes = {}
    cper = {}
    winvotes = 0
    win = ""
    for row in csvreader:
        rowcnt += 1
        cand = row[2]
        if cand in cvotes:
            cvotes[cand] = cvotes[cand] + 1
        else:
            cvotes[cand] = 1
for candi, vtcnt in cvotes.items():
    cper[candi] = "{0: .0%}".format(vtcnt / rowcnt)
    if vtcnt > winvotes:
        winvotes = vtcnt
        win = candi


print("Election Results")
print("--------------------")
print(f"Total Votes: {rowcnt}")
print("--------------------")
for candi, vtcnt in cvotes.items():
    print(f"{candi}: {cper[candi]} ({vtcnt})")
print("--------------------")
print(f"Winner: {win}")
print("--------------------")

filename = "OutputPy.txt"
filepath = os.path.join(".", filename)
with open(filepath, 'w') as text:
    text.write("Election Results" + "\n")   
    text.write("--------------------" + "\n")
    text.write(f"Total Votes: {rowcnt}" + "\n")
    text.write("--------------------" + "\n")
    for candi, vtcnt in cvotes.items():
        text.write(f"{candi}: {cper[candi]} ({vtcnt})" + "\n")
    text.write("--------------------" + "\n")
    text.write(f"Winner: {win}" + "\n")
    text.write("--------------------" + "\n")
    

    




