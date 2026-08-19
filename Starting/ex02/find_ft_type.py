def all_thing_is_obj(object: any) -> int:
    obty = type(object)
    if obty is str:
        print(object, " is in the kitchen : ", obty)
    elif obty is int:
        print("Type not found")
    elif obty:
        print(obty.__name__, " : ", obty)
    return 42