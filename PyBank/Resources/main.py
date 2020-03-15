# Import modules
import os
import csv


def getData(csv):
    # Vars to store data
    months = 0
    total = 0
    maxrev = 0
    minrev = 0
    avgchange = 0
    maxmonth = ""
    minmonth = ""
    lastmonth = None
    changes = []
    for row in csv:
        currentMonth = row[0]
        currentPnl = int(row[1])
        total += currentPnl
        months += 1
        if lastmonth is not None:
            currentChange = currentPnl-lastmonth
            changes.append(currentChange)
            if currentChange > maxrev:
                maxrev = currentChange
                maxmonth = currentMonth
            if currentChange < minrev:
                minrev = currentChange
                minmonth = currentMonth

        lastmonth = currentPnl
    avgchange = sum(changes)/len(changes)
    return [months, total, maxrev, minrev, avgchange, maxmonth, minmonth]


with open("budget_data.csv") as file:
    csvreader = csv.reader(file, delimiter=',')
    header = next(csvreader)
    analysis = getData(csvreader)


def outPut(analysis):
    outputStr = (f"""
    Financial Analysis
    --------------------------------------------------
    Total Months: {analysis[0]}
    Total: ${round(analysis[1], 2)}
    Average Change: ${round(analysis[4], 2)}
    Greatest Increase: {analysis[5]} - ($ {analysis[2]})
    Greatest Decrease: {analysis[6]} - ($ {analysis[3]})
    """)
    return outputStr


# Set output file path
# Save the stuff to a text file
output_path = os.path.join("..", "output", "FinancialAnalysis.txt")

# Checks if the directory exists, if it dosen't it makes one.
if not os.path.isdir("../output"):
    os.mkdir("../output")
else:
    pass

# Checks if path is valid. if it is, it creates a txt file containing the data
# else it gives as os error
try:
    with open(output_path, "w+") as dataOut:
        dataOut.writelines(outPut(analysis))
except OSError:
    print("Creation of txt file failed")
else:
    pass

# outputs the Data to terminal for the user to read immediately
print(f"""
    Financial Analysis
    --------------------------------------------------
    Total Months: {analysis[0]}
    Total: ${round(analysis[1], 2)}
    Average Change: ${round(analysis[4], 2)}
    Greatest Increase: {analysis[5]} - ($ {analysis[2]})
    Greatest Decrease: {analysis[6]} - ($ {analysis[3]})
    """)
