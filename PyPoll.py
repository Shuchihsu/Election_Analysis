# Add our dependencies.
import csv
import os 
#Assign a variable to load and the path for the file 
file_to_load = os.path.join('Resources','election_results.csv')
# Assign a variable to save and the path for the file 
file_to_save = os.path.join("analysis","election_analysis.txt")
# Initialize a total vote counter
total_votes = 0 
# Candidate options
candidate_options = []
# 1. Declare the empty dictionary
candidate_votes = {}
# Open the election results and read the file
with open (file_to_load) as election_data:
    file_reader = csv.reader(election_data)
  
    #Read the file object with the reader function
    file_reader = csv.reader(election_data)
        #Read the header row
    headers = next(election_data)
    #print(headers)
    #Print each row in the CSV file.
    for row in file_reader:
        #2 Add to the total vote count
        total_votes += 1
         # Print the candidate name from each row
        candidate_name = row [2]
         
        if candidate_name not in candidate_options:
            # Add it to the candidate_options
            candidate_options.append(candidate_name)
          # 2. Begin trackign that candidate's vote count.
            candidate_votes[candidate_name] = 0 
            # Add a vote to that candidate's name
        candidate_votes[candidate_name] += 1 
        # Determine the percentage of votes for each candidate by looping through the counts.
        # 1. Iterate through the candidate list
for candidate_name in candidate_votes:
            #2 Retrieve vote count of a candidate
    votes = candidate_votes[candidate_name]
            # 3. Calculate the percentage of votes for each candidate
    vote_percentage = float(votes)/float(total_votes)*100
            # Print out the candidate vote dictionary.
    print(f"{candidate_name}:received {vote_percentage}% of the vote")

 
