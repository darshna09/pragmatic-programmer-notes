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

## Duplication in Documentation

**Before:**

📄 [doc_duplication.py](./doc_duplication.py)

Comments restated what the code already made obvious, adding no new information.

**After:**

📄 [doc_duplication_fixed.py](./doc_duplication_fixed.py)

Removed redundant comments and relied on clearer function and variable names to make the code self-explanatory.

## DRY Violation in Data

- File 1: 📄 [doc_data.py](./doc_data.py)
- File 2: 📄 [doc_data_fixed.py](./doc_data_fixed.py)

| Aspect                  | File 1        | File 2                     |
| ----------------------- | ------------- | -------------------------- |
| Exposes internals       | ✅            | ❌                          |
| Can become inconsistent | ✅            | ❌                          |
| DRY violation           | ❌ accidental | ⚠️ intentional & controlled |
| Follows UAP             | ❌            | ✅                          |
| Safe to evolve          | ❌            | ✅                          |
