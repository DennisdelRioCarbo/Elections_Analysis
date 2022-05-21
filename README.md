# Elections_Analysis

##**Project Overview**
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election.

1.Calculate the total number of votes cast.
2.Get a complete list of candidates who received votes.
3.Calculate the total number of votes each candidate received.
4.Calculate the percentage of votes each candidate won.
5.Determine the winner of the election based on popular vote.

##**Resources**
-Data Source:election_results.csv
-Software:Python 3.10, Visual Studio Code 1.76.2,

##**Summary**
The analysis of the election shows that:
-There were **369,711 votes** cast in the election.

-The candidates were:
  -*Charles Casper Stockham*
  -*Diana Degette*
  -*Raymon Anthony Doane*

-The candidate results were:
  -*Charles Casper Stockham* received 23.0% of the votes and 85,213 number of votes.
  -*Diana Degette* received 73.8% of the vote and 272,892 number of votes.
  -*Raymon Anthony Doane* received 3.1% of the vote and 11,606 number of votes.
  
-The winner of the election was:
  -**Diana Degette**, who received **73.8%** of the vote and **272,892** number of votes.
  
##**Challenge Overview**
  The election comission has requested some additional data to complete the audit:
   
  -Voter turnout for each county:
    Jefferson:38,855 votes.
    Denver:306,055 votes.
    Arapahoe:24,801 votes.
    
  -The percentage of votes from each county out of the total count:
    Jefferson:10.5%
    Denver:82.8% 
    Arapahoe: 6.7%
    
  -The county with the highest turnout was **Denver**

  ##**Challenge Summary**
This script could work  to calculate the results of many type of elections, even state elections, with minor modifications. This applies even if we had more candidates or more counties. It would even work if the csv files were organized differently as all we would have to do is change how the script reads through the rows and update the position certain elements hold in the dictionaries or the lists. Also the print statments would have to be modified if we wanted to display the information in a different order  but the basic structure of the script would not need to be modified which would make it very useful for this type of analysis.  
