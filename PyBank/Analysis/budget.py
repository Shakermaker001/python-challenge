import os
import csv

csvpath = os.path.join('../Resources/budget_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    months = sum(1 for row in csvreader)
    total_profit = sum(int(r[2]) for r in csvreader)
    
  
        
        


print(total_profit)

   

   
 
    
  
        
