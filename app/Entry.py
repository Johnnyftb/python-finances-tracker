class Entry:
    def __init__(self, date, description, category, amount):
        self.date = date
        self.description = description
        self.category = category
        self.amount = amount

    def get_date(self):
        return self.date

    def set_date(self, new_date):
        self.date = new_date

    def get_month(self):
        return self.date.year

    def get_week(self):
        return self.date.isocalender()[1]

    def get_description(self):
        return self.description

    def set_description(self, new_description):
        self.description = new_description

    def get_category(self):
        return self.category

    def set_category(self, new_category):
        self.category = new_category

    def get_amount(self):
        return self.amount

    def set_amount(self, new_amount):
        self.amount = new_amount
