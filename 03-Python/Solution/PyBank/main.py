import csv

csvpath = "C:/Users/Gage/Desktop/SMU Bootcamp/GITHUB/smu_hw_oct_2022/03-Python/Solution/PyBank/Resources/budget_data.csv"

rows = 0
total = 0

last_profit = 0
total_changes = 0
change_count = 0

min_change = 999999999
max_change = -999999999

min_month = ""
max_month = ""

with open(csvpath, encoding='utf-8') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csvheader = next(csvreader)

    for row in csvreader:

        rows += 1
        total += int(row[1])

        if rows != 1:
            change = int(row[1]) - last_profit
            total_changes += change
            change_count += 1

            if (change > max_change):
                max_change = change
                max_month = row[0]
            elif (change < min_change):
                min_change = change
                min_month = row[0]
            else:
                pass

        last_profit = int(row[1])

csvfile.close()

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {change_count + 1}")
print(f"Total: {total}")
print(f"Average Change: ${round((total_changes / change_count), 2)}")
print(f"Greatest Increase in Profits: {max_month} (${max_change})")
print(f"Greatest Decrease in Profits: {min_month} (${min_change})")

outputpath = "C:/Users/Gage/Desktop/SMU Bootcamp/GITHUB/smu_hw_oct_2022/03-Python/Solution/PyBank/Analysis/output.txt"

with open(outputpath, 'w') as outputfile:
    outputfile.write("Financial Analysis\n")
    outputfile.write("----------------------------\n")
    outputfile.write(f"Total Months: {change_count + 1}\n")
    outputfile.write(f"Total: {total}\n")
    outputfile.write(f"Average Change: ${round((total_changes / change_count), 2)}\n")
    outputfile.write(f"Greatest Increase in Profits: {max_month} (${max_change})\n")
    outputfile.write(f"Greatest Decrease in Profits: {min_month} (${min_change})")

outputfile.close()