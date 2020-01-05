#PyBank.py
# import the os and csv to be able to read the csv file
import os
import csv

#set the name of csv and define the path to attrive the csv file
budget_csv = os.path.join("..", "Resources", "budget_data.csv")

#Create dict for calculating the average monthly change

budget_dict ={}

#Create a list to keep track of instances of rows
months_count = []

#Set initial values that need to be calculated

total_profit = 0
monthly_change = 0
last_month =0

#Open csv file and skip the header, and set to iterate the rows
with open(budget_csv, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)
    
    for row in csvreader:
        #Iterate and sum to get total
        total_profit += int(row[1])

        #Insert rows into a list to keep track of total months
        if row[0] not in months_count:
            months_count.append(row[0])

            #Calculating the difference on a monthly basis
            budget_dict[row[0]] = int(row[1]) - last_month
            last_month = int(row[1])


for k, v in budget_dict.items():

    #Skipping the first month
    if k == months_count[0]:
        num = 0
    else:
        
        monthly_change = monthly_change + v

#Getting max and min and the associated keys tied to those values from the budget_dict{} with zip()
lowest_price = min(zip(budget_dict.values(), budget_dict.keys()))
highest_price = max(zip(budget_dict.values(), budget_dict.keys()))

#Converting instances of row in list to a count
number_months = len(months_count)

#Getting avgerage monthly change
average_change = (monthly_change/number_months - 1)

#Setting the Output for results
line = "-------------------------------"
results = (
    line + '\n' + "Financial Analysis" + '\n' + line + '\n'
    "Total Months: " + str(number_months) + '\n'
    "Total Revenue: " + str(total_profit) + '\n'
    "Average Revenue Change: " + str(int(average_change)) + '\n'
    "Greatest Increase in Revenue: " + str(highest_price) + '\n'
    "Greatest Decrease in Revenue: " + str(lowest_price) + '\n' + line + '\n'
)

#Displya the results
print(results)

#Write out to a text file
f = open("Financial_Analysis.txt", "w")
f.write(results)
f.close()

