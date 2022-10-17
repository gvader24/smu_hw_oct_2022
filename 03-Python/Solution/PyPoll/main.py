import csv

csvpath = "C:/Users/Gage/Desktop/SMU Bootcamp/GITHUB/smu_hw_oct_2022/03-Python/Solution/PyPoll/Resources/election_data.csv"

rows = 0
votes = {}

with open(csvpath, encoding='utf-8') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csvheader = next(csvreader)

    for row in csvreader:

        rows += 1
        candidate = row[2]

        if candidate in votes.keys():
            votes[candidate] += 1
        else:
            votes[candidate] = 1

csvfile.close()



print("Election Results")
print("-------------------------")
print(f"Total Votes: {rows}")
print("-------------------------")
for x in votes.keys():
    print(f"{x}: {round((100 * votes[x] / rows), 3)}% ({votes[x]})")
print("-------------------------")
#https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
winner = max(votes, key=votes.get)
print(f"Winner: {winner}")
print("-------------------------")

outputpath = "C:/Users/Gage/Desktop/SMU Bootcamp/GITHUB/smu_hw_oct_2022/03-Python/Solution/PyPoll/Analysis/output.txt"

with open(outputpath, 'w') as outputfile:
    outputfile.write("Election Results\n")
    outputfile.write("-------------------------\n")
    outputfile.write(f"Total Votes: {rows}\n")
    outputfile.write("-------------------------\n")
    for x in votes.keys():
        outputfile.write(f"{x}: {round((100 * votes[x] / rows), 3)}% ({votes[x]})\n")
    outputfile.write("-------------------------\n")
    outputfile.write(f"Winner: {winner}\n")
    outputfile.write("-------------------------")

outputfile.close()