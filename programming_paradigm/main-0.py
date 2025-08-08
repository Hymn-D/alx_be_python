import sys
from bank_account import BankAccount

def parse_amount(text):
    try:
        value = float(text)
        if value < 0:
            raise ValueError("Amount must be non-negative.")
        return value
    except ValueError:
        return None

def main():
    # Adjust the initial balance as needed for testing
    account = BankAccount(100)

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command_parts = sys.argv[1].split(':', 1)
    command = command_parts[0].strip().lower()
    amount = None

    if len(command_parts) > 1 and command_parts[1].strip() != "":
        amount = parse_amount(command_parts[1].strip())
        if amount is None:
            print("Invalid amount. Use a non-negative number, e.g., deposit:50")
            sys.exit(1)

    if command == "deposit":
        if amount is None:
            print("Deposit requires an amount, e.g., deposit:50")
            sys.exit(1)
        account.deposit(amount)
        print(f"Deposited: ${amount}")
    elif command == "withdraw":
        if amount is None:
            print("Withdraw requires an amount, e.g., withdraw:20")
            sys.exit(1)
        if account.withdraw(amount):
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command. Use deposit, withdraw, or display.")

if __name__ == "__main__":
    main()

