grade_points = {
    "S": 10,
    "A": 9,
    "B": 8,
    "C": 7,
    "D": 6,
    "E": 5,
    "F": 4
}

def calculate_gpa(total_sem, semesters_data):
    gpa_list = []

    for sem in range(total_sem):
        total_credit_points = 0
        total_credits = 0

        for grade in semesters_data[sem]["theory"]:
            if grade in grade_points:
                total_credit_points += grade_points[grade] * 4
                total_credits += 4

        for grade in semesters_data[sem]["practical"]:
            if grade in grade_points:
                total_credit_points += grade_points[grade] * 2
                total_credits += 2

        gpa = total_credit_points / total_credits if total_credits else 0
        gpa_list.append(round(gpa, 2))

    cgpa = round(sum(gpa_list) / len(gpa_list), 2) if gpa_list else 0
    return gpa_list, cgpa
