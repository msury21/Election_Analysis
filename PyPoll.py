# The data we need to retrieve:
# 1) Total number of votes cast
# 2) Complete list of candidates who received votes
# 3) Percentage of votes each candidate won
# 4) Total number of votes each candidate won
# 5) Winner of election (popular vote)

import csv
import os

#assign variable to load file from path
file_to_load = os.path.join("Resources", "election_results.csv")

#assign variable to save file to path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#variable to count votes
total_votes = 0

#list to hold candidate options
candidate_options = []

#dict to hold votes per candidate
candidate_votes = {}

#track winning candidate and winning count
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#open results and read file
with open(file_to_load) as election_data:

    #read file w reader function
    file_reader = csv.reader(election_data)
    
    #read header row
    headers = next(file_reader)

    #print rows in file
    for row in file_reader:
        
        #add to total votes
        total_votes += 1

        #print candidate name
        candidate_name = row[2]

        #check if candidate name is in list
        if candidate_name not in candidate_options:

            #add candidate name to list (if not already in)
            candidate_options.append(candidate_name)

            #initialize amt of votes for each candidate
            candidate_votes[candidate_name] = 0

        #add votes for whatever candidate
        candidate_votes[candidate_name] += 1
        
#journey to find percentage of vote for each candidate
#iterate thru candidate list
for candidate_name in candidate_votes:

    #retrieve vote count of candidate
    votes = candidate_votes[candidate_name]

    #calculate percentage of votes
    vote_percentage = float(votes) / float(total_votes) * 100

    #print candidate name + vote percentage + votes
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    #journey to determine winning candidate + count
    #determine whether votes greater than winning count
    if (votes > winning_count) and (vote_percentage > winning_percentage):

        #if true, set new winning count and percentage
        winning_count = votes
        winning_percentage = vote_percentage

        #set winner = candidate name
        winning_candidate = candidate_name

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")

print(winning_candidate_summary)
        