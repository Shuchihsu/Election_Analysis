#The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidates won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# Assign a variable for the file to load and the path
import csv
#from distutils import text_file
import os 
#file_to_load = 'Resources/election_results.csv'
file_to_load = os.path.join('Resources','election_results.csv')
#open the election data results and read the file
#election_data = open(file_to_load,'r')
#election_data.close
#with open(file_name) as file_variable:

#with open (file_to_load) as election_data:
        #print(election_data)

#create a filename variable to a direct or indirect path to the file
#file_to_save = os.path.join("analysis","election_analysis.txt")
#open(file_to_save,"w")
#Outfile = open(file_to_save,"w")
#Write some data to the file.
#Outfile.write("Hello world")

#close the file
#Outfile.close()

file_to_save = os.path.join("analysis","election_analysis.txt")
#with open(file_to_save,"w") as txt_file:
    #txt_file.write("Hello world")
    #txt_file.write("A, ")
   # txt_file.write("B, ")
    #txt_file.write("C")
    #txt_file.write("Walla\n \nA\nB\nC")
with open (file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    #for row in file_reader:
        #print(row)
        #Read the file object with the reader function
    file_reader = csv.reader(election_data)
        #print out the header row.
    headers = next(election_data)
    print(headers)

