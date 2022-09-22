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

#open results and read file
with open(file_to_load) as election_data:

    #read file w reader function
    file_reader = csv.reader(election_data)
    
    #print header row
    headers = next(file_reader)
    print(headers)
