class Account:
    def __init__(self, debits: float, credits: float, fees: float):
        self.debits = debits
        self.credits = credits
        self.fees = fees
        self.balance = credits - debits - fees


def print_balance(account: Account) -> None:
    print(f"{'Debits':<10}: {account.debits:10.2f}")
    print(f"{'Credits':<10}: {account.credits:10.2f}")

    if account.fees < 0:
        print(f"{'Fees':<10}: {-account.fees:10.2f}")
    else:
        print(f"{'Fees':<10}: {account.fees:10.2f}")

    print("----------------------")

    if account.balance < 0:
        print(f"{'Balance':<10}: {-account.balance:10.2f}")
    else:
        print(f"{'Balance':<10}: {account.balance:10.2f}")


if __name__ == "__main__":
    account = Account(
        debits=1234.56,
        credits=2000.00,
        fees=25.00
    )
    print_balance(account)