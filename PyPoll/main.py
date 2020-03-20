import os
import csv

# Vars
totalNumVote = 0
runners = {}
runnerNum = 0
winner = ""

# data will hold all of the csv as lists
data = []
runnerIndex = 2

# os paths for input and output
inPath = os.path.join("Resources", "election_data.csv")
output_path = os.path.join("output", "ElectionResults.txt")

# Start of Code
# Start of input


def createCandidateDict(name):
    name = {"votes": 0}
    return name


def getData(csv):
    # loop through the csv data sheet
    info = []
    for row in csv:
        info.append(row)
    return info


with open(inPath) as file:
    reader = csv.reader(file, delimiter=',')
    header = next(reader)
    data = getData(reader)

# End of input
# Start of Calc

for row in data:
    if row[2] in runners.keys():
        runners[row[2]]["votes"] += 1
        totalNumVote += 1
    elif row[2] not in runners.keys():
        runners[row[2]] = createCandidateDict(row[2])
        runners[row[2]]["votes"] += 1
        totalNumVote += 1

for runner in runners:
    votes = runners[runner].get('votes')
    percent = votes/totalNumVote
    runners[runner]["percent"] = percent * 100

winningVotes = 0
for runner in runners:
    if runners[runner]["votes"] > winningVotes:
        winningVotes = runners[runner]["votes"]
        winner = runner


# End of Calc
# Start of output
# outputs the Data to terminal for the user to read immediately
str1 = f"""
    Election Results
    ----------------------------------------
    Total Votes: {totalNumVote}
    ----------------------------------------"""
str2 = f"""    ---------------------------------------
    Winner : {winner}
    ----------------------------------------"""
print(str1)
for runner in runners:
    print(f"\t{runner}: {runners[runner].get('percent'):.3f}% ({runners[runner].get('votes')})")
print(str2)


# Checks if the directory exists, if it dosen't it makes one.
if not os.path.isdir("output"):
    os.mkdir("output")
else:
    pass

# Checks if path is valid. if it is, it creates a txt file containing the data
# else it gives as os error
# writes output into the txt file
try:
    with open(output_path, "w+") as dataOut:
        dataOut.writelines(str1 + "\n")
        for runner in runners:
            dataOut.writelines(f"\t{runner}: {runners[runner].get('percent'):.3f}% ({runners[runner].get('votes')})\n")
        dataOut.writelines(str2)
except OSError:
    print("Creation of txt file failed")
else:
    pass
# End Of output
# End Of Code
