#Store variables
ListCandidates = []
CandidateVotes = []
VotePercentage = []
TotalVotes = 0
#Reads in the CSVs for PyPoll
import os
import csv
election_data = os.path.join('Resources', 'election_data.csv')
with open(election_data, newline = "")as csvfile:
    csvReader = csv.reader(csvfile, delimiter = ",")
#Successfully stores the header row
    csvHeader = next(csvReader)
#Reads through all rows of data using for loop
    for row in csvReader:
#Total Votes (5 points)
        TotalVotes += 1
        if row[2] not in ListCandidates:
            ListCandidates.append(row[2])
            Index = ListCandidates.index(row[2])
            CandidateVotes.append(1)
        else:
            Index = ListCandidates.index(row[2])
            CandidateVotes[Index] += 1
#Each candidate’s total votes and percent of votes (5 points)
    for votes in CandidateVotes:
        CandidatePercentage = (votes/TotalVotes) * 100
        CandidatePercentage = "%.3f%%" % CandidatePercentage
        VotePercentage.append(CandidatePercentage)
#Winner (5 points)
    Winner = max(CandidateVotes)
    WinnerIndex = CandidateVotes.index(Winner)
    ElectionWinner = ListCandidates[Index]
#Format as below
    #Your analysis should align with the following results:
#Election Results
#-------------------------
#The total number of votes cast
    #Total Votes: 369711
#-------------------------
#A complete list of candidates who received votes
#The percentage of votes each candidate won
    #Charles Casper Stockham: 23.049% (85213)
    #Diana DeGette: 73.812% (272892)
    #Raymon Anthony Doane: 3.139% (11606)
#-------------------------
#The winner of the election based on popular vote
    #Winner: Diana DeGette
#-------------------------
print("Election Results")
print("-------------------------")
print(f"Total Votes: {TotalVotes}")
print("-------------------------")
for i in range(len(ListCandidates)):
    print(f"{ListCandidates[i]}: {VotePercentage[i]} ({CandidateVotes[i]})")
print("-------------------------")
print(f"Winner: {ElectionWinner}")
print("-------------------------")
# Exporting to .txt file
output = open("output.txt", "w")
Row1 = "Election Results"
Row2 = "--------------------------"
Row3 = str(f"Total Votes: {TotalVotes}")
Row4 = str("--------------------------")
#In addition, your final script should both print the analysis to the terminal and export a text file with the results.
output.write('{}\n{}\n{}\n{}\n'.format(Row1, Row2, Row3, Row4))
for i in range(len(ListCandidates)):
    row = str(f"{ListCandidates[i]}: {VotePercentage[i]} ({CandidateVotes[i]})")
    output.write('{}\n'.format(row))
Row5 = "--------------------------"
Row6 = str(f"Winner: {ElectionWinner}")
Row7 = "--------------------------"
#You define a string with curly braces {} as placeholders for where you want to insert values.
#You call the .format() method on the string and pass the values you want to insert into the placeholders as arguments to the method.
output.write('{}\n{}\n{}\n'.format(Row5, Row6, Row7))