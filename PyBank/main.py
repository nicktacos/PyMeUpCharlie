import os
import csv
csvpath = os.path.join("..", "Resources", "budget_data.csv")
prevrev = 0
revch = []
mos = []
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    totrev = 0
    row_count = 0
    for row in csvreader:
        currentrev = int(row[1])
        totrev += currentrev
        row_count += 1
        mos.append(row[0])
        if row_count > 1:
            revchange = currentrev - prevrev
            revch.append(revchange)
        prevrev = currentrev
sumrc = sum(revch)
avgc = sumrc / (row_count - 1)
maxc = max(revch)
minc = min(revch)
maxind = revch.index(maxc)
minind = revch.index(minc)
maxmos = mos[maxind + 1]
minmos = mos[minind + 1]


print("Financial Analysis")
print("--------------------------")
print(f"Total Months: {str(row_count)}")  
print(f"Total Profit/Losses: ${int(totrev)}")
print(f"Average Change: ${avgc}")
print(f"Greatest Increase in Profits: {maxmos} (${maxc})")
print(f"Greatest Decrease in Profits: {minmos} (${minc})")
   
filename = "OutputPyPoll.txt"
filepath = os.path.join(".", filename)
with open(filepath, 'w') as text:
    text.write("Financial Analysis" + "\n")
    text.write("--------------------------" + "\n")
    text.write(f"Total Months: {str(row_count)}" + "\n")
    text.write(f"Total Profit/Losses: ${int(totrev)}" + "\n")
    text.write(f"Average Change: ${avgc}" + "\n")
    text.write(f"Greatest Increase in Profits: {maxmos} (${maxc})" + "\n")
    text.write(f"Greatest Decrease in Profits: {minmos} (${minc})" + "\n")

        
