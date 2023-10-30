def get_dict_input():
    try:
        dict_str = input("Enter a dictionary in the format {'key1': value1, 'key2': value2, ...}: ")
        dictionary = eval(dict_str)  # Parse the input string as a dictionary
        if not isinstance(dictionary, dict):
            raise ValueError("Invalid input. Please enter a valid dictionary.")
        return dictionary
    except (SyntaxError, ValueError):
        print("Invalid input format. Please enter a dictionary in the correct format.")
        return None

def intersection(dict1, dict2):
    return {key: dict1[key] for key in dict1 if key in dict2}

def union(dict1, dict2):
    result = dict1.copy()
    result.update(dict2)
    return result

def test_demorgans_laws(dict1, dict2):
    # De Morgan's Laws:
    # 1. not (A union B) == (not A) intersection (not B)
    law1_lhs = union(dict1, dict2)
    law1_rhs = intersection(dict1, dict2)
    is_law1_satisfied = law1_lhs == law1_rhs

    # 2. not (A intersection B) == (not A) union (not B)
    law2_lhs = intersection(dict1, dict2)
    law2_rhs = union(dict1, dict2)
    is_law2_satisfied = law2_lhs == law2_rhs

    return is_law1_satisfied, is_law2_satisfied

# Input
print("Enter the first dictionary:")
dict1 = get_dict_input()
print("Enter the second dictionary:")
dict2 = get_dict_input()

if dict1 is not None and dict2 is not None:
    # Test De Morgan's Laws
    law1_satisfied, law2_satisfied = test_demorgans_laws(dict1, dict2)

    if law1_satisfied and law2_satisfied:
        print("The input dictionaries satisfy De Morgan's Laws.")
    else:
        print("The input dictionaries do not satisfy De Morgan's Laws.")
