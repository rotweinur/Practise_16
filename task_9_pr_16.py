import itertools
def get_k_element_subsets(numbers: list[int], k: int) -> list[tuple[int, ...]]:
    """
    Generates a list of all K-element subsets for a given list of numbers.
    
    Args:
        numbers (list[int]): The input list of numbers.
        k (int): The size of the subsets to generate.
        
    Returns:
        list[tuple[int, ...]]: A list of K-element subsets.
    """
    if k > len(numbers):
        return []
        
    subsets = list(itertools.combinations(numbers, k))
    
    return subsets
if name == "main":
    numbers_9 = list(map(int, input().split()))
    k_9 = int(input())
    for subset in get_k_element_subsets(numbers_9, k_9):

        print(subset)
