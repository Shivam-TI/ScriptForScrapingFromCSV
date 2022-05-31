import csv
import os

# dummy values
network_usage_types = ["a", "b", "c"]

for filename in os.listdir(os.path.join(os.getcwd(), 'bills')):
	with open(os.path.join(os.getcwd(), 'bills', filename), 'r') as billing_file:
		bill_reader = csv.reader(billing_file)

		# Getting the list of servies being used
		usage_types_in_bill = next(bill_reader)

		# Second row is total for all the months for which the CSV file is generated
		next(bill_reader)
		
		# ut = usage_type
		column_no_for_ut = {}
		for column_no in range(len(usage_types_in_bill)):
			# if usage_types_in_bill[column_no] in network_usage_types:
				column_no_for_ut[usage_types_in_bill[column_no]] = column_no
		
		for month_bill in bill_reader:
			filename_with_path = os.path.join("aggregated_bills", month_bill[0] + ".csv")
			with open(filename_with_path, 'w') as month_file:
				if os.stat(filename_with_path).st_size == 0:
					month_file.write(",".join(["NetworkUsageTypes", *network_usage_types]) + "\n")
				month_bill_writer = csv.writer(month_file)
				costs = [os.path.splitext(filename)[0]]
				for usage_type in network_usage_types:
					if usage_type in usage_types_in_bill:
						costs.append(month_bill[column_no_for_ut[usage_type]])
					else:
						costs.append("0")
				month_bill_writer.writerow(costs)


