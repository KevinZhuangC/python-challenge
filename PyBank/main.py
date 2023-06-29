import os
import csv

csvpath = os.path.join("..","PyBank","Resources","budget_data.csv")

Dates = []
pro_los = []
lists_years = []
years = []
changes =[]
with open(csvpath, encoding="utf8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    header = next(csvreader)
    for row in csvreader:
        Dates.append(row[0])
        pro_los.append(int(row[1]))
    for i in range(len(pro_los)-1):
        change = pro_los[i+1]-pro_los[i]
        changes.append(change)
    max_change = max(changes)
    min_change = min(changes)
    max_change__date = Dates[changes.index(max_change)+1]
    min_change__date = Dates[changes.index(min_change)+1]


def avg(numbers:list):
    avg = sum(numbers)/len(numbers)
    return avg

print('Financial Analysis')
print('----------------------------')
print(f"Total Months: {len(Dates)}")
print(f"Total: ${sum(pro_los)}")
print(f"Average Change: ${round(avg(changes),2)}")
print(f"Greatest Increase in Profits: {max_change__date} (${max_change})")
print(f"Greatest Decrease in Profits: {min_change__date} (${min_change})")

filename = "output.txt"
content = "Financial Analysis\n----------------------------\nTotal Months: 86\nTotal: $22564198\nAverage Change: $-8311.11\nGreatest Increase in Profits: Aug-16 ($1862002)\nGreatest Decrease in Profits: Feb-14 ($-1825558)"

file = open(filename, "w")
file.write(content )
file.close()
