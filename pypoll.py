import os
import csv
uploadfile=os.path.join("Resources","Election_results.csv")
Total_votes=0
candidate_options = []
candidate_votes={}
winning_candidate = ""
winning_count = 0
winning_percentage = 0
with open(uploadfile) as resultfile:
    csvreader=csv.reader(resultfile)
    header=next(csvreader)
    print(header)
    for row in csvreader:
       Total_votes=Total_votes+1
       candidate_name=row[2]
       if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)  
            candidate_votes[candidate_name]=0
       candidate_votes[candidate_name]+=1      

print(f' Total votes= {Total_votes}')

for candidate_name in candidate_votes:
    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes) / float(Total_votes) * 100
    
    
    if (votes>winning_count) and (vote_percentage>winning_percentage):
        winning_count=votes
        winning_percentage=vote_percentage
        winning_candidate=candidate_name
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)
     
      