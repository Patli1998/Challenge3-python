## Import Lib ##
import os
import csv

## path ##
budget_file = "./PyBank/Resources/budget_data.csv"

## calculating total months
total_number_of_months = 0
total = 0
previous_amount = 0
changes_in_profit_losses = 0
max_profit = float('-inf')
max_profit_months = "NA"
min_profit = float('inf')
min_profit_months = "NA"
with open(budget_file, newline='') as csvfile:
    spamreader = csv.DictReader(csvfile, delimiter=',')
    ## next(csvfile) ##
    for row in spamreader:
       
        total_number_of_months+=1

        # calculating totals
        total+=int(row["Profit/Losses"]) 

        change_in_profit_losses = int(row["Profit/Losses"]) - previous_amount
        changes_in_profit_losses += change_in_profit_losses
        print(f"Current Profit Losses {previous_amount} - {row['Profit/Losses']} = {change_in_profit_losses}")
        # print(f"Change In Profit Losses {change_in_profit_losses}")
        # print(f"changes in profit losses{changes_in_profit_losses}")

        # Calculting greatest increase in profits
        previous_amount = int(row["Profit/Losses"])
        if change_in_profit_losses > max_profit:
            max_profit = change_in_profit_losses
            max_profit_months = row["Date"]

        # Calculating greatest decrease in profits
        if change_in_profit_losses < min_profit:
            min_profit = change_in_profit_losses
            min_profit_months = row["Date"]




changes_in_profit_losses_total = change_in_profit_losses / (total_number_of_months - 1)







print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_number_of_months}")
print(f"Total: ${total}")
print(f"Average Change: ${changes_in_profit_losses_total}")
print(f"Greatest Increase in Profits: {max_profit_months} ${max_profit}")
print(f"Greatest Decrease in Profits: {min_profit_months} ${min_profit}")


with open('./PyBank/Analysis/output.txt', 'w') as f:
    f.write("Financial Analysis\n")
    f.write("----------------------------\n")
    f.write(f"Total Months: {total_number_of_months}\n")
    f.write(f"Total: ${total}\n")
    f.write(f"Average Change: ${changes_in_profit_losses_total}\n")
    f.write(f"Greatest Increase in Profits: {max_profit_months} ${max_profit}\n")
    f.write(f"Greatest Decrease in Profits: {min_profit_months} ${min_profit}\n")