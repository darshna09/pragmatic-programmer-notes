# Topic 9: Code Duplication

This topic explores code duplication, DRY violations, and when duplication is intentional.

## DRY violations with example

**Before**

📄 [code_duplication.py](./code_duplication.py)

- Formatting logic duplicated for each field
- Conditionals used to handle negative values
- `print_balance` handled both layout and formatting

**After**

📄 [code_duplication_fixed.py](./code_duplication_fixed.py)

- Extracted formatting into `format_amount`
- Removed unnecessary conditionals
- `print_balance` now expresses intent, not mechanics

**Why**

- Reduces duplication
- Improves readability
- Makes formatting changes easier and safer

## DRY is about Knowledge, not Text

📄 [not_code_duplication.py](./not_code_duplication.py)

`validate_age` and `validate_quantity` look similar, but they represent different rules.

Combining them would reduce clarity and increase coupling.

This duplication is intentional and correct.
