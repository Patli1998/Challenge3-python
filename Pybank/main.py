## Import Lib ##
import os
import csv

## path ##
budget_data = "./Pybank/Resources/budget_data.csv"

with open(budget_data) as csvfile:
    reader = csv.DictReader(csvfile)

## loop stored in Dict ##

for row in reader:
    budget_data.append({"month": row["date"], "amount": int(row["Profit/Losses"]),"change": 0})

## total ##

months_total=len(budget_data)

## Change in Months ##

Old_Amount=budget_data[0]["amount"]
for i in range(months_total):
    budget_data[i]["change"]=budget_data[i]["amount"] - Old_Amount
    Old_Amount = budget_data[i]["amount"]

## Finding total Amount ##
total_amount=sum(row['amount']for row in budget_data)

## total change and avg of changes ##

total_change=sum(row['change']for row in budget_data)
Average=round(total_change / (months_total-1),2)

## greatest increase and decrease ##
greatest_increase = {"month": "", "change": 0}
greatest_decrease = {"month": "", "change": 0}

if row["change"] > greatest_increase["change"]:
                    greatest_increase["month"] = row["month"]
                    greatest_increase["change"] = row["change"]
elif row["change"] < greatest_decrease["change"]:
                    greatest_decrease["month"] = row["month"]
                    greatest_decrease["change"] = row["change"]

## print all ##

print("Financial_Analysis")
print("---------------------------------")
print(f"Total Months: {months_total}")
print(f"Total: ${total_amount}")
print(f"Average Change: ${round(Average,2)}")
print(f"Greatest Increase in Profits: {greatest_increase['month']} (${greatest_increase['change']})")
print(f"Greatest Decrease in Profits: {greatest_decrease['month']} (${greatest_decrease['change']})")