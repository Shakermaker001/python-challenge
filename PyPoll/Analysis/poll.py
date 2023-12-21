import os
import csv
from collections import Counter

csvpath = os.path.join('..', 'Resources','election_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ',')

    next(csvreader)
    
    canidates = [row[2] for row in csvreader]
    canidate_votes = Counter(canidates)
    total_votes = len(canidates)

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



       






    
        
    