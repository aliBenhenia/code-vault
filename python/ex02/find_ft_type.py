def all_thing_is_obj(object: any) -> int:
    """
    Prints the type of the given object with a formatted message.
    Returns 42.
    """
    type_map = {
        list: "List",
        tuple: "Tuple",
        set: "Set",
        dict: "Dict",
        str: None,
    }
    obj_type = type(object)
    if obj_type in type_map:
        label = type_map[obj_type]
        if label is None:
            print(f"{object} is in the kitchen : {obj_type}")
        else:
            print(f"{label} : {obj_type}")
    else:
        print("Type not found")
    return 42
