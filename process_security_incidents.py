# Step 1: Import the necessary csv module
import csv

# Step 2: Define the file names
input_file = 'security_incidents.csv'
output_file = 'security_incidents_modified.csv'

# Step 3: Read the CSV file and store the data in a list
data = []
with open(input_file, mode='r', newline='') as file:
    reader = csv.reader(file)
    headers = next(reader)  # Read the header row
    data = list(reader)     # Read the remaining data

# Step 4: Add a new column named 'Status' with a default value of 'Pending' for all rows
headers.append('Status')
for row in data:
    row.append('Pending')

# Step 5: Save the modified data to a new CSV file
with open(output_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)  # Write the header row
    writer.writerows(data)    # Write the data rows

print(f"Modified data has been saved to {security_incidents.csv}")
