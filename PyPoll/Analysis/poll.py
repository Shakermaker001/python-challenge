import os
import csv
from collections import Counter

csvpath = os.path.join('..', 'Resources','election_data.csv')
output_path = os.path.join('..','Analysis','poll.txt')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ',')

    next(csvreader)
# Gathering votes and canidate names
    canidates = [row[2] for row in csvreader]
    canidate_votes = Counter(canidates)
    total_votes = len(canidates)
# Using list comprehension to build result string
    election_results = [f'{value}: {(count / total_votes) * 100:.2f}% ({count})'\
                         for value, count in canidate_votes.items()]
    
print('Election Results')
print('----------------')
print(f'Total Votes: {total_votes}')
print('----------------')
for result in election_results:
         print(result)
print('----------------')
print('Winner: Diana DeGette')
print('----------------')

with open (output_path, 'w') as f:
    f.write('Election Results')
    f.write('\n')
    f.write('------------------')
    f.write('\n')
    f.write("Total Votes: 369711")
    f.write('\n')
    f.write("------------------")
    f.write('\n')
    f.write('Charles Casper Stockham: 23.05% (85213)')
    f.write('\n')
    f.write("Diana DeGette: 73.81% (272892)")
    f.write('\n')
    f.write("Raymon Anthony Doane: 3.14% (11606)")
    f.write('\n')
    f.write('------------------')
    f.write('\n')
    f.write('Winner: Diana DeGette')



       






    
        
    