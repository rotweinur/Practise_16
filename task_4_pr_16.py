def check_in_intersection(list1: list[int], list2: list[int], target: int) -> bool:
    """
    Checks if a given number belongs to the intersection of two sets.
    
    Args:
        list1 (list[int]): First list of elements.
        list2 (list[int]): Second list of elements.
        target (int): The number to check.
        
    Returns:
        bool: True if target is in the intersection, False otherwise.
    """
    set1 = set(list1)
    set2 = set(list2)
    
    intersection = set1.intersection(set2)
    
    return target in intersection
if name == "main":
    list1_4 = list(map(int, input().split()))
    list2_4 = list(map(int, input().split()))
    target_4 = int(input())
    print(check_in_intersection(list1_4, list2_4, target_4))