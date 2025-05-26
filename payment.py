class Payment:
    def __init__(self, amount, due_date, is_paid=False):
        self.amount = amount
        self.due_date = due_date
        self.is_paid = is_paid

    def pay(self):
        self.is_paid = True

    def reminder(self):
        if not self.is_paid:
            print(f"Reminder: Payment of ${self.amount} is due on {self.due_date}.")

    def penalty(self):
        if not self.is_paid:
            print(f"Penalty applied: Late payment for ${self.amount} due on {self.due_date}.")

    def __str__(self):
        return f"${self.amount} on {self.due_date} - {'Paid' if self.is_paid else 'Unpaid'}"