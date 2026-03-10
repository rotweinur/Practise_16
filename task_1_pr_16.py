def check_if_repeated(numbers: list[int], target: int) -> bool:
    """
    Checks if the target number belongs to the set of repeated numbers.
    
    Args:
        numbers (list[int]): A list of natural numbers.
        target (int): The number to check.
        
    Returns:
        bool: True if the target is in the set of repeated numbers, False otherwise.
    """
    seen_numbers = set()
    repeated_numbers = set()
    
    for num in numbers:
        if num in seen_numbers:
            repeated_numbers.add(num)
        else:
            seen_numbers.add(num)
            
    return target in repeated_numbers
if name == "main":
    numbers_1 = list(map(int, input().split()))
    target_1 = int(input())
    print(check_if_repeated(numbers_1, target_1))
