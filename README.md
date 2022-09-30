# Election Analysis

## Overview of Project 
The purpose of this election audit analysis is to develop a script that can assist with auditing an election in a Colorado precinct. The analysis portion has essentially three parts to it. First, it counts up the total amount of votes. Then, using the amount of votes from each of the three counties involved in the election, finds the percentage of votes from each county and the county with the largest voter turnout. Finally, it calculates the vote percentage from the amount of votes doled out to each candidate and declares the winner.

## Results
* There were 369,711 votes cast in this congressional election.
* The number of votes and the percentage of total votes for each county in the district is:
    - Jefferson, with 38,855 votes, contributed 10.5% of the vote.
    - Denver, with 306,055 votes, contributed 82.8% of the vote.
    - Arapahoe, with 24,801 votes, contributed 6.7% of the vote.
* Of all the counties, Denver had the largest voter turnout.
* The number of votes and the percentage of total votes for each candidate is:
    - Charles Casper Stockham, with 85,213 votes, received 23.0% of the vote.
    - Diana DeGette, with 272,892 votes, received 73.8% of the vote.
    - Raymon Anthony Doane, with 11,606 votes, received 3.1% of the vote.
* With 73.8% of the vote (272,892 votes), Diana DeGette won the election.

## Summary
This script can fairly easily be converted for other election audits. The script is versatile in the sense that the lists accumulating candidates and counties have no limitations on them (or really, they only have unreasonable limitations on them; from my research, it seems that you can put at least 500,000 items in a list, which is more than 100 times the amount of counties in the United States). Additionally, the script collects candidates/counties while searching the data, not requiring that information to be loaded into a list beforehand. This script can have an alteration to have collect votes on referendums, where winning candidate would be replaced by the issue that was voted on. Additionally, the script can collect additional data; other lists can be used to keep track of ethnicity (Hispanic votes for x,y, and z candidates and non-Hispanic votes for x,y, and z candidates), gender, household income, etc.