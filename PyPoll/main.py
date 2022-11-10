# This function allows for printing to a console and text file with the same call
def logger(message):
    outputPath = os.path.join("Analysis", "analysis.txt")
    print(message)
    with open(outputPath, 'a') as output:
        output.write(message)
        output.write('\n')

# import the needed dependencies
import csv
import os

# set the path for the csv file being used
csvPath = os.path.join("Resources", "election_data.csv")
outputPath = os.path.join("Analysis", "analysis.txt")

with open(outputPath, 'w') as output:
    pass

# counting variables and winner variable
winner = ""
winnerVotes = 0
totalVotes = 0
candidates = {
    "Name":[],
    "Votes":[],
    "Percentage":[]}

# open the csv file and read its contents
with open(csvPath, encoding="utf") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)

    #count the votes
    for row in csvreader:
        totalVotes += 1
        votedFor = row[2]

        # if the candidate has already gotten votes add to their total
        if votedFor in candidates["Name"]:
            index = candidates["Name"].index(votedFor)
            candidates["Votes"][index] += 1
        # otherwise add the candidate and set their votes to 1
        else:
            candidates["Name"].append(votedFor)
            candidates["Votes"].append(1)

# log the results of the election
logger("Election Results")
logger("-------------------------")
logger(f"Total Votes: {totalVotes}")
logger("-------------------------")

# calculate the percentages of each candidate and select a winner
for candidate in candidates["Name"]:
    index = candidates["Name"].index(candidate)
    votes = candidates["Votes"][index]
    candidates["Percentage"].append((candidates["Votes"][index]/totalVotes)*100)
    percentage = candidates["Percentage"][index]
    logger(f"{candidate}: {percentage:.3f}% ({votes})")
    if(candidates["Votes"][index] > winnerVotes):
        winner = candidate
        winnerVotes = candidates["Votes"][index]


logger("-------------------------")
logger(f"Winner: {winner}")    
logger("-------------------------")