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

def algebraic_sum(dict1, dict2):
    result = {}
    for key in set(dict1) | set(dict2):
        result[key] = dict1.get(key, 0) + dict2.get(key, 0)
    return result

def bounded_sum(dict1, dict2):
    result = {}
    for key in set(dict1) | set(dict2):
        total = dict1.get(key, 0) + dict2.get(key, 0)
        result[key] = total
    return result

def bounded_difference(dict1, dict2):
    result = {}
    for key in set(dict1) | set(dict2):
        difference = dict1.get(key, 0) - dict2.get(key, 0)
        result[key] = difference
    return result

# Input
print("Enter the first dictionary:")
dict1 = get_dict_input()
print("Enter the second dictionary:")
dict2 = get_dict_input()

if dict1 is not None and dict2 is not None:
    # Intersection
    print("Intersection:", intersection(dict1, dict2))

    # Union
    print("Union:", union(dict1, dict2))

    # Algebraic Sum
    print("Algebraic Sum:", algebraic_sum(dict1, dict2))

    # Bounded Sum
    print("Bounded Sum:", bounded_sum(dict1, dict2))

    # Bounded Difference
    print("Bounded Difference:", bounded_difference(dict1, dict2))
