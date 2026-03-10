def sieve_of_eratosthenes_set(n: int) -> list[int]:
    """
    Finds all prime numbers less than n using the Sieve of Eratosthenes algorithm and sets.
    
    Args:
        n (int): The upper bound (exclusive).
        
    Returns:
        list[int]: Sorted list of prime numbers less than n.
    """
    if n <= 2:
        return []
        
    numbers_set = set(range(2, n))
    p = 2
    
    while p * p < n:
        if p in numbers_set:
            multiples = set(range(p * p, n, p))
            numbers_set = numbers_set.difference(multiples)
        p += 1
        
    return sorted(list(numbers_set))
if name == "main":
    n_5 = int(input())
    print(sieve_of_eratosthenes_set(n_5))