## Import Lib ##
import os
import csv

## path ##
budget_file = "./Challenge3-python/PyBank/Resources/budget_data.csv"
print('Get current working directory : ', os.getcwd())


total_number_of_months = 0
total = 0
with open(budget_file, newline='') as csvfile:
    spamreader = csv.DictReader(csvfile, delimiter=',')
    ## next(csvfile) ##
    for row in spamreader:
       
        total_number_of_months+=1
        total+=int(row["Profit/Losses"]) 

average = total / total_number_of_months

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_number_of_months}")
print(f"Total: ${total}")
print(f"Average Change: ${average}")