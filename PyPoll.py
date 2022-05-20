#Data to be retrieved
import csv
import os

#Assign a variable to load a file from a path.
file_to_load=os.path.join("Resources","election_results.csv")

#Create a filename variable to a direct or indirect path to the file.
file_to_save=os.path.join("analysis","election_analysis.txt")

#Using the with statement open the election results and read the file

with open(file_to_load) as election_data:
    file_reader=csv.reader(election_data)

#Read and print the header row.
    headers=next(file_reader)
    print (headers)
    
#To do: read and analyze the data
    


#create a filename variable to a direct or indirect path to the file.


#use the open statement to open the file as a text file.

#Write some data in the file.

#Close file

#Total number of votes cast
#Complete list of candidates
#Total number of votes each candidate received
#Percentage of votes each candidate won
#Winner of the election based on popular vote
