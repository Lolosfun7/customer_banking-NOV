""" Create a Account class with methods"""

class Account:
    """Creating an Account class with methods"""
    def __init__(self, balance, interest_rate):
        self.balance = balance
        self.interest_rate = interest_rate
        self.interest_earned = 0

    # This method sets the balance of the account.
    def set_balance(self, balance):
        """Sets the balance for the for the account"""
        self.balance = balance
        

    # The method sets the interest gained for the account.
    def set_interest(self, interest):
        """Sets the interest gained for the the account"""
        self.interest_earned = interest_earned

    def calculate_interest(self, months):
        return self.balance * (self.interest_rate / 100) * (months / 12)
        
