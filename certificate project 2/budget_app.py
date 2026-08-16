class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({
            "amount": amount,
            "description": description
        })

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({
                "amount": -amount,
                "description": description
            })
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = self.name.center(30, "*")
        lines = [title]

        for item in self.ledger:
            description = item["description"][:23]
            amount = f"{item['amount']:.2f}"
            lines.append(f"{description:<23}{amount:>7}")

        lines.append(f"Total: {self.get_balance():.2f}")

        return "\n".join(lines)


def create_spend_chart(categories):

    spending = []

    for category in categories:
        total = 0
        for item in category.ledger:
            if item["amount"] < 0:
                total += -item["amount"]
        spending.append(total)

    total_spending = sum(spending)

    percentages = []
    for amount in spending:
        percentage = int((amount / total_spending) * 100)
        percentage = (percentage // 10) * 10
        percentages.append(percentage)

    lines = ["Percentage spent by category"]

    for level in range(100, -1, -10):
        line = f"{level:>3}|"
        for percentage in percentages:
            if percentage >= level:
                line += " o "
            else:
                line += "   "
        line += " "
        lines.append(line)
    lines.append("    " + "-" * (len(categories) * 3 + 1))
    max_name_length = max(len(category.name) for category in categories)

    for i in range(max_name_length):
        line = "     "
        for category in categories:
            if i < len(category.name):
                line += category.name[i] + "  "
            else:
                line += "   "
        line = line.rstrip() + "  "
        lines.append(line)

    return "\n".join(lines)