class Account:
    def __init__(self, returned_check_count: int, overdraft_days: int, average_balance: float):
        self.returned_check_count = returned_check_count
        self.overdraft_days = overdraft_days
        self.average_balance = average_balance


def calculate_account_fees(account: Account) -> int:
    fees = 20 * account.returned_check_count

    if account.overdraft_days > 3:
        fees += 10 * account.overdraft_days

    if account.average_balance > 2000:
        fees //= 2

    return fees


if __name__ == "__main__":
    account = Account(
        returned_check_count=2,
        overdraft_days=5,
        average_balance=2500
    )

    total_fees = calculate_account_fees(account)
    print(f"Total fees: USD {total_fees:.2f}")
