import itertools
def get_all_subsets(numbers: list[int]) -> list[tuple[int, ...]]:
    """
    Generates a list of all subsets (the power set) for a given list of numbers.
    
    Args:
        numbers (list[int]): The input list of numbers.
        
    Returns:
        list[tuple[int, ...]]: A list of all subsets.
    """
    subsets = []
    
    for length in range(len(numbers) + 1):
        combinations = list(itertools.combinations(numbers, length))
        subsets.extend(combinations)
        
    return subsets
if name == "main":
    numbers_8 = list(map(int, input().split()))
    for subset in get_all_subsets(numbers_8):

        print(subset)
