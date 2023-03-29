# Import modules
import os
import csv

# Set the input/output path 
input_path=os.path.join(r"C:\Users\Chloe\OneDrive\Desktop\Bootcamp\Challenge_3\PyBank\budget_data.csv")
output_path = os.path.join(r"C:\Users\Chloe\OneDrive\Desktop\Bootcamp\Challenge_3\PyBank\Financial Analysis.txt")

# Set variables
total_months = []
total_profit = []
monthly_profit_change = []

# Open csv file
with open(input_path) as csvfile:  
     
     csvreader = csv.reader(csvfile, delimiter=',')

     csv_header = next(csvreader)

# Count the total of months and total of profits
     for row in csvreader: 

        total_months.append(row[0])
        total_profit.append(int(row[1]))
        
# Calculate the profit change
     for i in range(len(total_profit)-1):
        
        monthly_profit_change.append(total_profit[i+1]-total_profit[i])
        
max_increase_value = max(monthly_profit_change)
max_decrease_value = min(monthly_profit_change)

max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1 

print(f"Financial Analysis")
print(f"----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")

with open (output_path,"w") as file:
    file.write(f"Financial Analysis\n")
    file.write(f"----------------------------\n")
    file.write(f"Total Months: {len(total_months)}\n")
    file.write(f"Total: ${sum(total_profit)}\n")
    file.write(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}\n")
    file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})\n")
    file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")
