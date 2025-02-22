import csv

# paths
file_read = "../../data/budget_data.csv"
file_write = "budget_analysis.txt"

# variables
total_months = 0
total_net = 0

net_changes = []
previous_net = -1

# data
with open(file_read, "r") as budget_data:
	
	csv_reader = csv.reader(budget_data)

	header = next(csv_reader)
	for row in csv_reader:

		month = row[0]
		net = int(row[1])

		total_months += 1
		total_net += net

		if previous_net != -1:
			net_changes.append(net - previous_net)
		previous_net = net

# calculating
total_net_change = 0
for net_change in net_changes:
	total_net_change += net_change
average_net_change = total_net_change / len(net_changes)

greatest_positive_change = max(net_changes)
greatest_negative_change = min(net_changes)

# output (print)
print(f"total_months: {total_months}")
print(f"total_net: {total_net:,}")
print(f"average_net_change: {round(average_net_change,2):,}")
print(f"greatest_positive_change: {greatest_positive_change:,}")
print(f"greatest_negative_change: {greatest_negative_change:,}")

# output (write)
with open(file_write, "w") as budget_analysis:
	budget_analysis.write(f"total_months: {total_months}\n")
	budget_analysis.write(f"total_net: {total_net:,}\n")
	budget_analysis.write(f"average_net_change: {round(average_net_change,2):,}\n")
	budget_analysis.write(f"greatest_positive_change: {greatest_positive_change:,}\n")
	budget_analysis.write(f"greatest_negative_change: {greatest_negative_change:,}\n")