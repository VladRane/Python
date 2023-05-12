import random

class Bank:
    def __init__(self):
        self.users = {}

    def create_account(self):
        while True:
            # Generate a random card number
            card_number = ''.join(str(random.randint(0, 9)) for _ in range(16))
            # Check the card number using the Luhn algorithm
            if self.luhn_check(card_number):
                break

        pin = input("Enter a PIN code: ")
        # Save the user data
        self.users[card_number] = {'pin': pin, 'balance': 0}
        print(f"Account created successfully. Card number: {card_number}\n")

    def luhn_check(self, card_number):
        """Check the card number using the Luhn algorithm"""
        sum = 0
        num_digits = len(card_number)
        oddeven = num_digits & 1
        for i in range(0, num_digits):
            digit = int(card_number[i])
            if not ((i & 1) ^ oddeven):
                digit *= 2
            if digit > 9:
                digit -= 9
            sum += digit
        return (sum % 10) == 0

    def login(self):
        card_number = input("Enter card number: ")
        pin = input("Enter PIN code: ")

        if card_number in self.users and self.users[card_number]['pin'] == pin:
            print("Login successful.\n")
            self.menu(card_number)
        else:
            print("Incorrect card number or PIN code.\n")

    def menu(self, card_number):
        while True:
            print("Menu:\n1. Deposit money\n2. Withdraw money\n3. Check balance\n4. Exit")
            choice = input("Select an option: ")

            if choice == "1":
                amount = int(input("Enter the amount to deposit: "))
                self.users[card_number]['balance'] += amount
                print(f"Balance updated. Current balance: {self.users[card_number]['balance']} rub.\n")
            elif choice == "2":
                amount = int(input("Enter the amount to withdraw: "))
                if self.users[card_number]['balance'] >= amount:
                    self.users[card_number]['balance'] -= amount
                    print(f"{amount} rub. withdrawn successfully. Current balance: {self.users[card_number]['balance']} rub.\n")
                else:
                    print("Insufficient funds.\n")
            elif choice == "3":
                print(f"Current balance: {self.users[card_number]['balance']} rub.\n")
            elif choice == "4":
                break
            else:
                print("Invalid choice.\n")

if __name__ == '__main__':
    bank = Bank()

    while True:
        print("Welcome to the bank!")
        print("1. Create an account\n2. Login\n3. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            bank.create_account()
        elif choice == "2":
            bank.login()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.\n")
