class Policyholder:
    def __init__(self, name, policy_id):
        self.name = name
        self.policy_id = policy_id
        self.status = "active"
        self.payments = []

    def suspend(self):
        self.status = "suspended"

    def reactivate(self):
        self.status = "active"

    def display_details(self):
        print(f"Policyholder: {self.name}")
        print(f"Policy ID: {self.policy_id}")
        print(f"Status: {self.status}")
        print("Payments:")
        for payment in self.payments:
            print(f"  - {payment}")
