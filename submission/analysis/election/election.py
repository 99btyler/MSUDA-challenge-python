import csv

# paths
file_read = "../../data/election_data.csv"
file_write = "election-analysis.txt"

# variables
total_votes = 0

candidates = {}
winner = None

# data
with open(file_read, "r") as election_data:
    
    csv_reader = csv.reader(election_data)

    header = next(csv_reader)
    for row in csv_reader:

        candidate = row[2]

        total_votes += 1

        if candidate in candidates:
            candidates[candidate] += 1
            if candidates[winner] < candidates[candidate]:
                winner = candidate
        else:
            candidates[candidate] = 1
            if winner == None:
                winner = candidate

# output (print)
print(f"total_votes: {total_votes:,}")
for candidate in candidates:
    print(f"candidate: {candidate} {round((candidates[candidate] / total_votes) * 100, 3)}% ({candidates[candidate]:,})")
print(f"winner: {winner}")

# output (write)
with open(file_write, "w") as election_analysis:
    election_analysis.write(f"total_votes: {total_votes:,}\n")
    for candidate in candidates:
        election_analysis.write(f"candidate: {candidate} {round((candidates[candidate] / total_votes) * 100, 3)}% ({candidates[candidate]:,})\n")
    election_analysis.write(f"winner: {winner}\n")