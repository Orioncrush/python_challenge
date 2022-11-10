# this function allows for printing to the console and a file with a single function call
def logger(message):
    outputPath = os.path.join("Analysis", "analysis.txt")
    print(message)
    with open(outputPath, 'a') as output:
        output.write(message)
        output.write('\n')

# Import OS and CSV modules
import os
import csv

# Set the path for the csv file and output
filePath = os.path.join('Resources','budget_data.csv')
outputPath = os.path.join('Analysis', 'analysis.txt')

# Ensure the Analysis file is clean
with open(outputPath, 'w') as output:
    pass

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

# open and work through the csv file
with open(filePath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)

    for row in csvreader:
        porl = float(row[1]) 
        months += 1
        netTotal += porl
        change += (porl - lastProfit)
        lastProfit = porl
        
        #if this is the highest profit
        if(porl > greatestProft):
            greatestProft = porl
            greatestPDate = row[0]
        #if this is the worst loss
        if(porl < greatestLoss):
            greatestLoss = porl
            greatestLDate = row[0]

# calculate the average change
averageChange = change / months

#log the output
logger("Financial Analysis")
logger("----------------------------")
logger(f"Total Months: {months}")
logger(f"Total: ${netTotal:.2f}")
logger(f"Average Change: ${averageChange:.2f}")
logger(f"Greatest Increase in Profits: {greatestPDate} (${greatestProft:.2f})")
logger(f"Greatest Decrease in Profits: {greatestLDate} (${greatestLoss:.2f})")