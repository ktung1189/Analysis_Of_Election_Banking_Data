#PyPoll.py
# import the os and csv to be able to read the csv fil
import os
import csv

#set the name of csv and define the path to attrive the csv file
election_csv = os.path.join("..", "Resources", "election_data.csv")

count = 0

#Initial list to for election data
candidate = []
#List to find the unique candidates in total list
unique_candidate = []
#List for to get vote counts
vote_total = []
#List to keep track of percentage of votes for unique candidates
vote_percent = []

with open(election_csv, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter =",")
    csv_header = next(csvreader)

    #Iterate through all the rows in csv file and get total count of rows
    #Insert candidates into candidate list
    for row in csvreader:
        count = count + 1
        candidate.append(row[2])
    #Use set() to find each unique candidate in list of candidates
    for i in set(candidate):
        #For each unique candidate add into unique_candidate list
        unique_candidate.append(i)
        unique_count = candidate.count(i)
        #Get the total for each unique candidate
        vote_total.append(unique_count)
        #Find the percentage from each unique candidate from total vote count
        percent_totals = (unique_count/count) * 100
        vote_percent.append(percent_totals)
    #Find the max of from list of vote_total
    winner_count = max(vote_total)
    #Find the winner of election by adding all the votes for each unique_candidate in 
    #unique candidate list
    #By the max amount in the vote_total list determine the winner
    candidate_winner = unique_candidate[vote_total.index(winner_count)]

#Display to output
line = ("-------------------------")
print("Election Results")
print(line)
print("Total Votes :" + str(count))
print(line)
#Display all unique candidates, vote_percentage, and vote_total
for x in range(len(unique_candidate)):
    print(unique_candidate[x] + ": " + "{:.3f}".format(vote_percent[x]) + "% (" + str(vote_total[x]) + ")")
print(line)
print("The winner is: " + candidate_winner)
print(line)

#Write out as txt file
with open('election_results.txt', 'w') as text:
    text.write("Election Results\n")
    text.write(line + '\n')
    text.write("Total Vote: " + str(count) + "\n")
    text.write(line + '\n')
    for x in range(len(set(unique_candidate))):
        text.write(unique_candidate[x] + ": " + str(vote_percent[x]) + "% (" + str(vote_total[x]) + ")\n")
    text.write(line + '\n')
    text.write("The winner is: " + candidate_winner + "\n")
    text.write(line + '\n')