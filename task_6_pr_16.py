def solve_cryptarithm() -> list[str]:
    """
    Solves the cryptarithm ХОД + ХОД + ХОД = МАТ.
    Letters Х, О, Д, М, А, Т represent distinct decimal digits (0-9).
    'Х' and 'М' cannot be 0 because they are the first digits of 3-digit numbers.
    
    Returns:
        list[str]: List of formatted solutions.
    """
    results = []

    for hod_value in range(100, 334):
        mat_value = hod_value * 3
        
        s_hod = str(hod_value)
        s_mat = str(mat_value)
        
        х = s_hod[0]
        о = s_hod[1]
        д = s_hod[2]
        
        м = s_mat[0]
        а = s_mat[1]
        т = s_mat[2]
        
        unique_digits = {х, о, д, м, а, т}
        
        if len(unique_digits) == 6:
            results.append(f"{х}{о}{д} + {х}{о}{д} + {х}{о}{д} = {м}{а}{т}")
            
    return results

if name == "main":
    solutions = solve_cryptarithm()
    
    if solutions:
        for res in solutions:
            print(res)
    else:
        print("Решений не найдено.")
    
    numbers_7 = list(map(int, input().split()))
    print(get_lexicographical_permutations(numbers_7))