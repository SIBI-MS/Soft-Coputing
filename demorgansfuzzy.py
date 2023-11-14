def get_input_set(message, size):
    """
    Helper function to get user input for a set.

    Args:
    - message: A message to prompt the user.
    - size: Number of inputs expected.

    Returns:
    - A dictionary representing the set.
    """
    input_set = {}
    print(message)
    for _ in range(size):
        key, value = input().split()
        if 0.0 <= float(value) <= 1.0:
            input_set[key] = float(value)
        else:
            print("Invalid input. Values must be between 0 and 1.")
            return None
    return input_set


def calculate_complement(input_set):
    """
    Calculate the complement of a set.

    Args:
    - input_set: The set for which the complement is to be calculated.

    Returns:
    - A dictionary representing the complement of the set.
    """
    complement_set = {}
    for key in input_set:
        complement_set[key] = 1.0 - input_set[key]
    return complement_set


def apply_demorgans_laws(X, Y):
    """
    Apply De Morgan's laws and check if they are satisfied.

    Args:
    - X: First set.
    - Y: Second set.
    """
    complement_X = calculate_complement(X)
    complement_Y = calculate_complement(Y)

    if complement_X is None or complement_Y is None:
        return  # Exit if there's an invalid input

    # First Theorem: X' ∩ Y' = (X ∪ Y)'
    Z_intersection = {key: min(complement_X[key], complement_Y[key]) for key in complement_X}
    complement_union = calculate_complement({key: max(X[key], Y[key]) for key in X})
    print("First Theorem Satisfied:", Z_intersection == complement_union)

    # Second Theorem: X' ∪ Y' = (X ∩ Y)'
    Z_union = {key: max(complement_X[key], complement_Y[key]) for key in complement_X}
    complement_intersection = calculate_complement({key: min(X[key], Y[key]) for key in X})
    print("Second Theorem Satisfied:", Z_union == complement_intersection)


def main():
    # No. of inputs by the user
    n = int(input('No of inputs in first set: '))
    X = get_input_set("Enter the values in first set X:", n)

    m = int(input('No of inputs in second set: '))
    Y = get_input_set("Enter the values in second set Y:", m)

    if X is not None and Y is not None:
        print("Values in the first set X:", X)
        print("Values in the second set Y:", Y)
        apply_demorgans_laws(X, Y)


if __name__ == "__main__":
    main()

