class Account:
    def __init__(self, returned_check_count: int, overdraft_days: int, average_balance: float):
        self.returned_check_count = returned_check_count
        self.overdraft_days = overdraft_days
        self.average_balance = average_balance

# Calculate the fees for this account.
#
# * Each returned check cost USD 20
# * If the account is in overdraft for more than 3 days,
#    charge USD 10 for each day
# * If the average account balance is greater than USD 2000
#    reduce the fees by 50%
def fees(a: Account) -> int:
    f = 0

    if a.returned_check_count > 0:
        f += 20 * a.returned_check_count

    if a.overdraft_days > 3:
        f += 10 * a.overdraft_days

    if a.average_balance > 2000:
        f //= 2

    return f


if __name__ == "__main__":
    account = Account(
        returned_check_count=2,
        overdraft_days=5,
        average_balance=2500
    )

    total_fees = fees(account)
    print(f"Total fees: USD {total_fees:.2f}")
