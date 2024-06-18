################ Person Class ################

class PersonAccount():
    
    def __init__(self, first_name, last_name, incomes, expenses, properties):
        
        self.first_name = first_name
        self.last_name = last_name
        self.incomes = incomes
        self.expenses = expenses
        self.properties = properties
        
        
    def total_income(self):
        pass
    
    def total_expenses(self):
        pass
    
    def account_info(self):
        pass
    
    def add_income(self):
        pass
    
    def add_expenses(self):
        pass
    
    def account_balance(self):
        pass
    
    def personInfo(self):
        return f'Full Name: {self.first_name} {self.last_name}\nTotal Income: {self.incomes}\nTotal Expenses: {self.expenses}\nProperties: {self.properties}'
p = PersonAccount('Brandon', 'Braxton', 50000, 40000, False)
print(p.personInfo())