import csv
from datetime import datetime
from Entry import Entry

CATEGORIES = ["Rent", "Transport", "Groceries", "Other Expenses", "Credit Card", "Savings", "Wants",
              "General Spendings", "Holiday", "Tax"]

class FinanceTracker:
    def __init__(self):
        self.entries = []
        self.categories = CATEGORIES
        return

    def load(self):
        with open('../entries.csv', 'r') as csv_file:
            for entry in csv_file:
                date_string = entry[0]
                date = datetime.strptime(date_string, "%d/%m/%Y")

                description = entry[1]
                category = entry[2]
                amount = float(entry[3])

                new_entry = Entry(date, description, category, amount)
                self.entries.append(new_entry)

        print(self.entries)


    def save(self):
        return
