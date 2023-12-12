import csv #imports the csv library
#define the file path
filepath="C:/Users/jacqu/vu_bootcamp/VU-VIRT-DATA-PT-11-2023-U-LOLC/03-Python/Starter_Code/PyPoll/Resources/election_data.csv"
row_count=0#variable to count rows/votes
vote_count=0#variable to count votes
ccs=0#variable for vote for Charles
dd=0#variable for vote for Diana
rad=0#variable for vote for Raymon
#initializes all values
with open(filepath) as csv_file: #opens the file and defines it as csv_file
    csv_reader=csv.reader(csv_file,delimiter=",")#defines the csv reader
    csv_header=next(csv_file)#saves the header of the file to a seperate variable
    for row in csv_reader:#for loop to run through the file
        row_count+=1#counting the amount of loops/rows/votes
        candidate=row[2]#sets the variable equal to the current rows candidate
        if candidate=="Charles Casper Stockham":
            ccs+=1#counting up the vote total for Charles
        elif candidate=="Diana DeGette":
            dd+=1#counting up the vote total for Diana
        else:
            rad+=1#counting up the vote total for Raymon
            #logic for counting the votes by comparing the strings of the candidates
ccs_format="{:,.3%}".format(ccs/row_count)#creating a formatted percentage value for Charles
dd_format="{:,.3%}".format(dd/row_count)#creating a formatted percentage value for Diana
rad_format="{:,.3%}".format(rad/row_count)#creating a formatted percentage value for Raymon
if dd > ccs and dd > rad:
    winner="Diana DeGette"#sets winner as Diana
elif ccs > dd and ccs> rad:
    winner="Charles Casper Stockham"#sets winner as Charles
else:
    winner="Raymon Anthony Doane"#sets winner as Raymon
    #logic to determine winner
print("Election Results")
print(f"Total Votes: {row_count}")
print(f"Charles Casper Stockham: {ccs_format} ({ccs})\nDiana DeGette: {dd_format} ({dd})\nRaymon Anthony Doane: {rad_format} ({rad})")
print(f"Winner is {winner}")
#print statements for display
output_path="C:/Users/jacqu/vu_bootcamp/VU-VIRT-DATA-PT-11-2023-U-LOLC/03-Python/Starter_Code/PyPoll/Resources/pypoll.csv"
#sets output file path
with open(output_path,'w') as csv_file:#opens the file and sets it as csv_file
    csvwriter=csv.writer(csv_file)#defining the writer class
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow([f"Total Votes: {row_count}"])
    csvwriter.writerow([f"Charles Casper Stockham: {ccs_format} ({ccs})"+f"\nDiana DeGette: {dd_format} ({dd})\nRaymon Anthony Doane: {rad_format} ({rad})"])
    csvwriter.writerow([f"Winner is {winner}"])
    #print statements for writing in the csv file
