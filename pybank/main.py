# Import
import os
import csv

# __________PYBANK__________
# Import resources
budget_csv = os.path.join(".", "resources", "budget_data.csv")
# Name some variables and trackers
total_profit = 0
date_count = 0
net_change = 0
total_change = 0
greatest_inc = ["", 0]
greatest_dec = ["", 0]

# Open and read csv
with open(budget_csv) as budget_file:
    budget_reader = csv.reader(budget_file, delimiter=",")
    # Read the header row first
    budget_header = next(budget_reader)
    # Set the rest of the data to a list
    budget_list = list(budget_reader)
    # Find date total
    date_count = sum(1 for row in budget_list)
    print("Financial Analysis")
    print("----------------------------------------")
    print("Total Months:", date_count)

    # Find profit total
    for row in budget_list:
        total_profit += int(row[1])
    print("Total: $", total_profit)

# Reopen the csv to restart the reader
with open(budget_csv) as budget_file:
    budget_reader = csv.reader(budget_file, delimiter=",")
    # Read the header row
    budget_header = next(budget_reader)
    # Pull first row of actual numbers
    first_row = next(budget_reader)
    prev_net = int(first_row[1])
    # Track the net change
    for row in budget_reader:
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        total_change = total_change + net_change
        # Calculate the greatest increase
        if net_change > greatest_inc[1]:
            greatest_inc[0] = row[0]
            greatest_inc[1] = net_change
        # Calculate the greatest decrease
        if net_change < greatest_dec[1]:
            greatest_dec[0] = row[0]
            greatest_dec[1] = net_change
        avg_change = round(total_change/(date_count-1), 2)
    print("Average Change: $", avg_change)
    print("Greatest Increase in Profits:", greatest_inc)
    print("Greatest Decrease in Profits:", greatest_dec)

    # Export to .txt
    output_path = os.path.join(".", "analysis", "results.txt")
    with open(output_path, 'a') as csvfile:
        # Initialize csv.writer
        csvwriter = csv.writer(csvfile, delimiter=" ")
        # Export the results
        csvwriter.writerow(["Financial Analysis"])
        csvwriter.writerow(["----------------------------------------"])
        csvwriter.writerow(["Total Months:", date_count])
        csvwriter.writerow(["Total Profit: $", total_profit])
        csvwriter.writerow(["Average Change: $", avg_change])
        csvwriter.writerow(["Greatest Increase in Profits:", greatest_inc])
        csvwriter.writerow(["Greatest Decrease in Profits:", greatest_dec])
