def get_lexicographical_permutations(numbers: list[int]) -> list[tuple[int, ...]]:
    """
    Returns all permutations of a given list of numbers in lexicographical order.
    
    Args:
        numbers (list[int]): The input list of numbers.
        
    Returns:
        list[tuple[int, ...]]: A list of tuples containing the permutations.
    """
    sorted_numbers = sorted(numbers)
    permutations = list(itertools.permutations(sorted_numbers))
    
    return permutations
if name == "main":
    numbers_7 = list(map(int, input().split()))
    for perm in get_lexicographical_permutations(numbers_7):
        print(perm)