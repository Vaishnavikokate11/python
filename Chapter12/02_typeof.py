from typing import List, Dict, Tuple

a : int = 5
name : str = "vaishu"

List_of_ints : List[int] = [1,2,3,4]
Tuple_of_str_int: Tuple[str,int] = ("Vaishu", 5)

print(List_of_ints)

def sum(a: int, b: int) -> int:
    return a + b

sum(3,6)