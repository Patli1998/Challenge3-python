## Importing Lib
import os
import csv

#path
election_file = "./PyPoll/Resources/election_data.csv"
total_number_of_votes_cast = 0
votes = dict()
with open(election_file, newline='') as csvfile:
    spamreader = csv.DictReader(csvfile, delimiter=',')
    ## next(csvfile) ##
    for row in spamreader:
        total_number_of_votes_cast += 1
        if row["Candidate"] in votes:
            votes[row["Candidate"]] += 1
        else:
            votes[row["Candidate"]] = 1

winner = max(votes, key=votes.get)






print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {total_number_of_votes_cast}")
print(f"-------------------------")
for candidate in votes.keys():
    print(f"{candidate} {round(100*(votes[candidate]/ total_number_of_votes_cast), 3)}% ({votes[candidate]})")
print(f"-------------------------")
print(f"Winner: {winner}")

print(f"-------------------------")



with open('./PyPoll/Analysis/output.txt', 'w') as f:
    f.write(f"Election Results\n")
    f.write(f"-------------------------\n")
    f.write(f"Total Votes: {total_number_of_votes_cast}\n")
    f.write(f"-------------------------\n")
    for candidate in votes.keys():
        f.write(f"{candidate} {round(100*(votes[candidate]/ total_number_of_votes_cast), 3)}% ({votes[candidate]})\n")
    f.write(f"-------------------------\n")
    f.write(f"Winner: {winner}\n")

    f.write(f"-------------------------\n")

