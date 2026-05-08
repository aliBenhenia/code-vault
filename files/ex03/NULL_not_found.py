import math


def NULL_not_found(object: any) -> int:
    """
    Prints the type of 'null-like' values.
    Returns 0 on success, 1 on unrecognized type.
    """
    if object is None:
        print(f"Nothing: {object} {type(object)}")
        return 0
    if isinstance(object, float) and math.isnan(object):
        print(f"Cheese: {object} {type(object)}")
        return 0
    if isinstance(object, int) and not isinstance(object, bool) and object == 0:
        print(f"Zero: {object} {type(object)}")
        return 0
    if isinstance(object, str) and object == "":
        print(f"Empty: {type(object)}")
        return 0
    if isinstance(object, bool) and object is False:
        print(f"Fake: {object} {type(object)}")
        return 0
    print("Type not Found")
    return 1
