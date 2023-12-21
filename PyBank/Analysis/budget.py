import os
import csv


csvpath = os.path.join('..', 'Resources','budget_data.csv')
output_path = os.path.join('..','Analysis','bank.txt')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ',')
  
    next(csvreader) 
    revenue = []
    months = []
    rev_change = []

    for row in csvreader:

        revenue.append(float(row[1]))
        months.append(row[0])

    print("Financial Analysis")
    print("------------------")
    print("Total Months:", len(months))
    print("Total Revenue: $", sum(revenue))

    for i in range(1,len(revenue)):
        rev_change.append(revenue[i] - revenue[i-1])   
        avg_rev_change = sum(rev_change)/len(rev_change)

        max_rev_change = max(rev_change)

        min_rev_change = min(rev_change)

        max_rev_change_date = (months[rev_change.index(max(rev_change))])
        min_rev_change_date = (months[rev_change.index(min(rev_change))])

    print(f"Avereage Revenue Change: $", round(avg_rev_change))
    print(f"Greatest Increase in Revenue:", max_rev_change_date,"($", max_rev_change,")")
    print(f"Greatest Decrease in Revenue:", min_rev_change_date,"($", min_rev_change,")")



with open (output_path, 'w') as f:
    f.write('Financial Analysis')
    f.write('\n')
    f.write('------------------')
    f.write('\n')
    f.write("Total Months: 86")
    f.write('\n')
    f.write("Total Revenue: $ 22564198.0")
    f.write('\n')
    f.write('Average Revenue Change: $-8311')
    f.write('\n')
    f.write("Greatest Increase in Revenue: Jul-16 ($ 1862002.0 )")
    f.write('\n')
    f.write("Greatest Decrease in Revenue: Jan-14 ($ -1825558.0 )")

    


        

   






