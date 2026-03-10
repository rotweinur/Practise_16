def count_unique_preferences(main_person_prefs: list[str], friends_prefs: list[list[str]]) -> int:
    """
    Determines how many products only the main person likes.
    
    Args:
        main_person_prefs (list[str]): List of products the main person likes.
        friends_prefs (list[list[str]]): List of lists containing friends' preferences.
        
    Returns:
        int: The number of products unique to the main person.
    """
    main_set = set(main_person_prefs)
    friends_union = set()
    
    for friend_pref in friends_prefs:
        friends_union.update(set(friend_pref))
        
    unique_prefs = main_set.difference(friends_union)
    
    return len(unique_prefs)
if name == "main":
    main_prefs_3 = input().split()
    n_3 = int(input())
    friends_prefs_3 = []
    for _ in range(n_3):
        friends_prefs_3.append(input().split())
    print(count_unique_preferences(main_prefs_3, friends_prefs_3))