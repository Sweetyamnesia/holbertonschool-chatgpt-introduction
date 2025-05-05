class Checkbook:
    """
    A simple Checkbook class to manage deposits, withdrawals, and balance tracking.
    """

    def __init__(self):
        """
        Initializes the Checkbook with a starting balance of 0.0.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Adds a specified amount to the current balance.

        Parameters:
        amount (float): The amount of money to deposit.

        Returns:
        None
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Subtracts a specified amount from the current balance if sufficient funds are available.

        Parameters:
        amount (float): The amount of money to withdraw.

        Returns:
        None
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Displays the current balance.

        Parameters:
        None

        Returns:
        None
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """
    Main loop for interacting with the Checkbook via user input.
    Allows the user to deposit, withdraw, check balance, or exit.
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").lower()
        
        if action == 'exit':
            break
        elif action == 'deposit':
            while True:
                try:
                    amount = float(input("Enter the amount to deposit: $"))
                    if amount < 0:
                        print("Amount must be positive. Please try again.")
                        continue
                    cb.deposit(amount)
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number for deposit.")
        elif action == 'withdraw':
            while True:
                try:
                    amount = float(input("Enter the amount to withdraw: $"))
                    if amount < 0:
                        print("Amount must be positive. Please try again.")
                        continue
                    cb.withdraw(amount)
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number for withdrawal.")
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
