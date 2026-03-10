def count_common_courses(students_courses: list[list[str]]) -> int:
    """
    Determines how many elective courses were chosen by all students.
    
    Args:
        students_courses (list[list[str]]): A list where each element is a list of a student's courses.
        
    Returns:
        int: The number of courses chosen by absolutely everyone.
    """
    if not students_courses:
        return 0
        
    common_courses = set(students_courses[0])
    
    for courses in students_courses[1:]:
        common_courses = common_courses.intersection(set(courses))
        
    return len(common_courses)
if name == "main":
    n_2 = int(input())
    courses_2 = []
    for _ in range(n_2):
        courses_2.append(input().split())
    print(count_common_courses(courses_2))