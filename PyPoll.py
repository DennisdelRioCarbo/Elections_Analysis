#Data to be retrieved
import csv
import os

#Assign a variable to load a file from a path.
file_to_load=os.path.join("Resources","election_results.csv")

#Create a filename variable to a direct or indirect path to the file.
file_to_save=os.path.join("analysis","election_analysis.txt")

#1.Initialzea total vote counter.
total_votes=0

#Candidate options
candidate_options=[]

#Declare empty dictionary.
candidate_votes={}

#Winning candidate and winning count tracker
winning_candidate=""

winning_count=0

winning_percentage=0

#Using the with statement open the election results and read the file
with open(file_to_load) as election_data:
    file_reader=csv.reader(election_data)

#Read the header row
    headers=next(file_reader)

#Print each row in the CSV file.
    for row in file_reader:

        #Add to the total vote count.
        total_votes += 1

        #Print the candidate name from each row.
        candidate_name=row[2]

        if candidate_name not in candidate_options:
            
        #Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

        #Begin tracking that candidate's vote count.
            candidate_votes[candidate_name]=0

            #Add a vote to that candidate's count.
        candidate_votes[candidate_name]+=1

#Determine the percentage of votes for each candidate by looping through the counts.
#.Iterate through the candidate list.
for candidate_name in candidate_votes:

    #.Retrieve vote count of a candidate.
    votes=candidate_votes[candidate_name]

    #.Calculate the percentage of votes.
    vote_percentage=float(votes)/float(total_votes)*100

    if (votes>winning_count) and (vote_percentage>winning_percentage):
        winning_count=votes

        winning_percentage=vote_percentage

        winning_candidate=candidate_name

    #4.Print the candidate name and percentage of votes.
    print(f'{candidate_name}:{vote_percentage:.1f}% ({votes:,})\n')

winning_candidate_summary=(
    f"--------------------------------\n"
    f"Winner:{winning_candidate}\n"
    f"Winning vote count:{winning_count:n}\n"
    f"Winning percentage: {winning_percentage:.1f}%\n"
    f"--------------------------------\n")
print(winning_candidate_summary)

