#Add our dependencies
import csv
import os

#Assign a variable to load a file from a path.
file_to_load=os.path.join("Resources","election_results.csv")

#Assign a variable to a direct or indirect path to the file.
file_to_save=os.path.join("analysis","election_analysis.txt")

#Initialzea total vote counter.
total_votes=0

#Candidate options
candidate_options=[]

#Declare empty dictionary.
candidate_votes={}

#Winning candidate and winning count tracker
winning_candidate=""

winning_count=0

winning_percentage=0

#open the election results and read the file
with open(file_to_load) as election_data:

    file_reader=csv.reader(election_data)

    #Read the header row
    headers=next(file_reader)

    #Print each row in the CSV file.
    for row in file_reader:

        #Add to the total vote count.
        total_votes=total_votes + 1

        #Get  the candidate name from each row.
        candidate_name=row[2]

        #If the candidate name does not match the any existing candidate add it to the candidate list.
        if candidate_name not in candidate_options:
            
        #Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

        #Begin tracking that candidate's vote count.
            candidate_votes[candidate_name]=0

            #Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1


#Save the results to our text file.        
with open(file_to_save, "w") as txt_file:

        #After opening the file print the final vote count to the terminal.
    election_results=(
        f'\nElection Results\n'
        f"----------------------\n"
        f"Total Votes:{total_votes:,}\n"
        f"----------------------\n")

    print(election_results, end="")

#After printing the final vote count to the terminal save the final vote count to the text file.

    txt_file.write(election_results)
        
    for candidate_name in candidate_votes:

        #.Retrieve vote count of a candidate.
         votes=candidate_votes.get(candidate_name)

        #.Calculate the percentage of votes.
         vote_percentage=float(votes)/float(total_votes)*100

         candidate_results=(
            f"{candidate_name}:{vote_percentage:.1f}% ({votes:,})\n")

        #Print each candidate's voter count and percentage to the terminal.
         print(candidate_results)
        

        #Save the candidate results to our text file.
         txt_file.write(candidate_results)

        #Determine winning vote count, winning percentage, and winning candidate.
         if (votes > winning_count) and (vote_percentage > winning_percentage):
                winning_count=votes
                winning_candidate=candidate_name
                winning_percentage=vote_percentage

#print the winning's candidate results to the terminal.
    winning_candidate_summary=(
            f"-------------------------\n"
            f"Winner:{winning_candidate}\n"
            f"Winning vote count:{winning_count:,}\n"
            f"Winning percentage:{winning_percentage:.1f}%\n"
            f"--------------------------\n")

    print(winning_candidate_summary)

    txt_file.write(winning_candidate_summary)

        