class ValidationError(Exception):
    """Base class for validation errors."""
    pass


class AgeValidationError(ValidationError):
    pass


class QuantityValidationError(ValidationError):
    pass


def validate_age(age) -> None:
    """
    Validates whether an age is acceptable.
    Rules:
    - Must be an integer
    - Must be between 18 and 120
    """
    if not isinstance(age, int):
        raise AgeValidationError("Age must be an integer")

    if age < 18 or age > 120:
        raise AgeValidationError("Age must be between 18 and 120")


def validate_quantity(quantity) -> None:
    """
    Validates whether a quantity is acceptable.
    Example: number of wine bottles.
    Rules:
    - Must be an integer
    - Must be between 1 and 24
    """
    if not isinstance(quantity, int):
        raise QuantityValidationError("Quantity must be an integer")

    if quantity < 1 or quantity > 24:
        raise QuantityValidationError("Quantity must be between 1 and 24")


if __name__ == "__main__":
    # ---- AGE TESTS ----
    try:
        validate_age(25)
        print("Age 25 is valid")
    except ValidationError as e:
        print(f"Age error: {e}")

    try:
        validate_age("twenty")
    except ValidationError as e:
        print(f"Age error: {e}")

    # ---- QUANTITY TESTS ----
    try:
        validate_quantity(6)
        print("Quantity 6 is valid")
    except ValidationError as e:
        print(f"Quantity error: {e}")

    try:
        validate_quantity(100)
    except ValidationError as e:
        print(f"Quantity error: {e}")