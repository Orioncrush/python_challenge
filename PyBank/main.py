# Import OS and CSV modules
import os
import csv

# Set the path for the csv file and output
filePath = os.path.join('Resources','budget_data.csv')
outputPath = os.path.join('Analysis', 'analysis.txt')

# Tracking Variables
months = 0
netTotal = 0.0
change = 0.0
averageChange = 0.0
greatestProft = 0.0
greatestPDate = "Nev-00"
greatestLoss = 0.0
greatestLDate = "Nev-00"
lastProfit = 0.0

with open(filePath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)

    for row in csvreader:
        porl = float(row[1]) 
        months += 1
        netTotal += porl
        change += (porl - lastProfit)
        lastProfit = porl
        
        if(porl > greatestProft):
            greatestProft = porl
            greatestPDate = row[0]
        
        if(porl < greatestLoss):
            greatestLoss = porl
            greatestLDate = row[0]

averageChange = change / months

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {months}")
print(f"Total: ${netTotal:.2f}")
print(f"Average Change: ${averageChange:.2f}")
print(f"Greatest Increase in Profits: {greatestPDate} (${greatestProft:.2f})")
print(f"Greatest Decrease in Profits: {greatestLDate} (${greatestLoss:.2f})")

with open(outputPath, 'w') as output:
    output.write("Financial Analysis")
    output.write('\n')
    output.write("----------------------------")
    output.write('\n')
    output.write(f"Total Months: {months}")
    output.write('\n')
    output.write(f"Total: ${netTotal:.2f}")
    output.write('\n')
    output.write(f"Average Change: ${averageChange:.2f}")
    output.write('\n')
    output.write(f"Greatest Increase in Profits: {greatestPDate} (${greatestProft:.2f})")
    output.write('\n')
    output.write(f"Greatest Decrease in Profits: {greatestLDate} (${greatestLoss:.2f})")
