#Store variables
TotalMonths = 0
ProfitLoss = 0
TotalValue = 0
TotalChange = 0
TotalProfit = []
Dates = []
#Reads in the CSVs for PyBank
import os
import csv
budget_data = os.path.join('Resources', 'budget_data.csv')
with open(budget_data, newline = "")as csvfile:
    csvReader = csv.reader(csvfile, delimiter = ",")
#Successfully stores the header row
    csvHeader = next(csvReader)
#Reads next row of actual data after header 
    FirstRow = next(csvReader)
    TotalMonths += 1
    ProfitLoss += int(FirstRow[1])
    TotalValue = int(FirstRow[1])
#Repeat through next rows
    for row in csvReader:
        Dates.append(row[0])
#Find total change and add it to 'TotalChange' list
        TotalChange = int(row[1])-TotalValue
        TotalProfit.append(TotalChange)
        TotalValue = int(row[1])
#Total Months (5 points) 
        TotalMonths += 1
#Total (5 points)
        ProfitLoss = ProfitLoss + int(row[1])
#Average Change (5 points)
    AverageChange = sum(TotalProfit)/len(TotalProfit)
#Greatest Increase (5 points)
    GreatestProfit = max(TotalProfit)
    ProfitIndex = TotalProfit.index(GreatestProfit)
    ProfitDate = Dates[ProfitIndex]
#Greatest Decrease (5 points)
    GreatestLoss = min(TotalProfit)
    LossIndex = TotalProfit.index(GreatestLoss)
    LossDate = Dates[LossIndex]
#Format as below
    #Your analysis should align with the following results:
#Financial Analysis
#----------------------------
#The total number of months included in the dataset
    #Total Months: 86
#The net total amount of "Profit/Losses" over the entire period
    #Total: $22564198
#The changes in "Profit/Losses" over the entire period, and then the average of those changes
    #Average Change: $-8311.11
#The greatest increase in profits (date and amount) over the entire period
    #Greatest Increase in Profits: Aug-16 ($1862002)
#The greatest decrease in profits (date and amount) over the entire period
    #Greatest Decrease in Profits: Feb-14 ($-1825558)
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {TotalMonths}")
print(f"Total: ${ProfitLoss}")
print(f"Average Change: ${round(AverageChange,2)}")
print(f"Greatest Increase in Profits: {ProfitDate} ${GreatestProfit}")
print(f"Greatest Decrease in Profits: {LossDate} ${GreatestLoss}")
#In addition, your final script should both print the analysis to the terminal and export a text file with the results
output = open("output.txt", "w")
Row1 = ("Financial Analysis")
Row2 = ("----------------------------")
Row3 = (f"Total Months: {TotalMonths}")
Row4 = (f"Total: ${ProfitLoss}")
Row5 = (f"Average Change: ${round(AverageChange,2)}")
Row6 = (f"Greatest Increase in Profits: {ProfitDate} ${GreatestProfit}")
Row7 = (f"Greatest Decrease in Profits: {LossDate} ${GreatestLoss}")
#You define a string with curly braces {} as placeholders for where you want to insert values.
#You call the .format() method on the string and pass the values you want to insert into the placeholders as arguments to the method.
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(Row1,Row2,Row3,Row4,Row5,Row6,Row7))