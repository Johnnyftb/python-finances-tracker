import csv

def read_csv_and_return_arrays(filename):
    entries = []
    with open(filename, mode='r') as file:
        csv_file = csv.reader(file)
        next(csv_file)
        for entry in csv_file:
            entries.append(entry)


    return entries

# txt File Format:
#
# date | description | category | amount
def append_to_csv(date, description, category, amount):
    fields = [date, description, category, amount]
    with open(r'../entries.csv', 'a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(fields)

def process_entries(entries):
    for entry in entries:
        date = entry[0]
        description = entry[3]

        category = ""
        if entry[4] == "Car / Transport":
            category = "Transport"
        else:
            category = entry[4]

        amount = 0
        if entry[5][0] == "-":
            amount = "-" + entry[5][2:]
        else:
            amount = entry[5][1:]

        append_to_csv(date, description, category, amount)

def main():
    entries = read_csv_and_return_arrays("../raw_entries.csv")
    process_entries(entries)
    return

main()