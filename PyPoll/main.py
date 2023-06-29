import os
import csv

csvpath = os.path.join("..","PyPoll","Resources","election_data.csv")

votes = []
count_CCS = 0
count_DD = 0
count_RAD = 0
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    header = next(csvreader)
    for row in csvreader:
        votes.append(row)
    for vote in votes:
        if vote[2] == 'Charles Casper Stockham':
            count_CCS += 1
        elif vote[2] =='Diana DeGette':
            count_DD += 1
        elif vote[2] == 'Raymon Anthony Doane':
            count_RAD += 1
    perc_CCS = count_CCS/sum([count_CCS,count_DD,count_RAD])*100
    perc_DD = count_DD/sum([count_CCS,count_DD,count_RAD])*100
    perc_RAD = count_RAD/sum([count_CCS,count_DD,count_RAD])*100
    winner_votes = max([count_CCS,count_DD,count_RAD])
    if winner_votes == count_RAD:
        winner = "Raymon Anthony Doane"
    elif winner_votes == count_CCS:
        winner = "Charles Casper Stockham"
    elif winner_votes == count_DD:
        winner = "Diana DeGette"
print('Election Results')
print('-------------------------')
print(f'Total Votes: {len(votes)}')
print('-------------------------')
print(f'Charles Casper Stockham: {round(perc_CCS,3)}% ({count_CCS})')
print(f'Diana DeGette: {round(perc_DD,3)}% ({count_DD})')
print(f'Raymon Anthony Doane: {round(perc_RAD,3)}% ({count_RAD})')
print('-------------------------')
print(f'Winner: {winner}')
print('-------------------------')

filename = "output.txt"
content = 'Election Results\n-------------------------\nTotal Votes: 369711\n-------------------------\nCharles Casper Stockham: 23.049% (85213)\nDiana DeGette: 73.812% (272892)\nRaymon Anthony Doane: 3.139% (11606)\n-------------------------\nWinner: Diana DeGette\n-------------------------'


file = open(filename, "w")
file.write(content )
file.close()

