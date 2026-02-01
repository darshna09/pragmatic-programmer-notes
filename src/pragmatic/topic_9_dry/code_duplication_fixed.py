class Account:
    def __init__(self, debits: float, credits: float, fees: float):
        self.debits = debits
        self.credits = credits
        self.fees = fees
        self.balance = credits - debits - fees


def format_amount(label: str, amount: float) -> None:
    print(f"{label:<10}: {amount:10.2f}")


def print_balance(account: Account) -> None:
    format_amount("Debits", account.debits)
    format_amount("Credits", account.credits)
    format_amount("Fees", account.fees)

    print("----------------------")

    format_amount("Balance", account.balance)


if __name__ == "__main__":
    account_negative = Account(
        debits=5234.56,
        credits=2000.00,
        fees=25.00
    )
    print_balance(account_negative)

    print("\n****************************\n")

    account_positive = Account(
        debits=5234,
        credits=6234,
        fees=25.00
    )
    print_balance(account_positive)