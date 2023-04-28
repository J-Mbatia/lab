class Account:
    def __init__(self, name: str) -> None:
        """
        Function to set up account object
        :param name: Account name
        """
        self.account_name = name
        self.account_balance = 0

    def deposit(self, amount) -> bool:
        """
        Function to add to object
        :param amount: Numeric value to add
        :return: Boolean value to show if the value went through
        """
        if amount > 0:
            self.account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount) -> bool:
        """
        Function to subtract from object
        :param amount: Numeric value to subtract
        :return: Boolean value to show if the value went through
        """
        if (amount > 0) and (amount <= self.account_balance):
            self.account_balance -= amount
            return True
        else:
            return False

    def get_balance(self) -> int:
        """
        Function to get the numeric value from object
        :return: Numeric value of account_balance
        """
        return self.account_balance

    def get_name(self) -> str:
        """
        Function to get the value from object
        :return: String value of account_name
        """
        return self.account_name
    