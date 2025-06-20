class Expense:

#Creating an expense class
    def __init__(self,name,category,amount) -> None:
        self.name=name
        self.category=category
        self.amount=amount

    def __repr__(self):
        return f"<Expense: {self.name}, {self.category}, ${self.amount:,2f} >"

    def __str__(self):
        return f"Expense(name={self.name}, category={self.category}, amount={self.amount})"