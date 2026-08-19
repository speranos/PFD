def NULL_not_found(object: any) -> int:
    obty = type(object)

    if obty is type(None) and object is None:
        print("Nothing: ", obty)
    elif obty is type(float("NaN")) and object != object:
        print("Cheese : ", obty)
    elif obty is int and object == 0:
        print("Zero: ", obty)
    elif obty is str and object == "":
        print("Empty: ", obty)
    elif obty is bool and object is False:
        print("Fake: ", obty)
    else:
        print("Type not found")
        return 1
    return 0