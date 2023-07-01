import os
import csv
uploadfile=os.path.join("Resources","Election_results.csv")
with open(uploadfile) as resultfile:
    csvreader=csv.reader(resultfile)
    header=next(csvreader)
    print(header)
    for row in resultfile:
       print(row)
      