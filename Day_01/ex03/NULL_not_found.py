def NULL_not_found(obj: any) -> int:
    """
    Prints the object type of "null-like" objects:
      None, NaN, 0, empty string, False
    Return 0 if recognized, else 1.
    """
    # 1) None -> "Nothing: None <class 'NoneType'>"
    if obj is None:
        print(f"Nothing: None {type(obj)}")
        return 0
    
    # 2) float('NaN') -> "Cheese: nan <class 'float'>"
    #    We can check if something is NaN via math.isnan
    import math
    if isinstance(obj, float) and math.isnan(obj):
        print(f"Cheese: nan {type(obj)}")
        return 0
        
    # 5) False -> "Fake: False <class 'bool'>"
    # Need 5 before 3 otherwise Fake fall in 3
    if obj is False:
        print(f"Fake: False {type(obj)}")
        return 0

    # 3) 0 -> "Zero: 0 <class 'int'>"
    if obj == 0 and isinstance(obj, int):
        print(f"Zero: 0 {type(obj)}")
        return 0

    # 4) '' (empty string) -> "Empty:  <class 'str'>"
    if obj == '' and isinstance(obj, str):
        print(f"Empty: {type(obj)}")
        return 0

    # If not any of the above
    print("Type not Found")
    return 1

Nothing = None
Garlic = float("NaN")
Zero = 0
Empty = ''
Fake = False
NULL_not_found(Nothing)
NULL_not_found(Garlic)
NULL_not_found(Zero)
NULL_not_found(Empty)
NULL_not_found(Fake)
print(NULL_not_found("Brian"))