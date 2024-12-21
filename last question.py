students_scores = {"Tabish": (85, 90, 78),"Umaan": (92, 88, 84),"Kamraan": (79, 80, 85),"Taha": (88, 91, 93)}

def calculate_average_scores(students_scores):
    for student, scores in students_scores.items():
        average_score = sum(scores) / len(scores)
        print(f"{student}'s average score: {average_score:.2f}")

def highest_average_score(students_scores):
    highest_avg = 0
    top_student = ""
    for student, scores in students_scores.items():
        average_score = sum(scores) / len(scores)
        if average_score > highest_avg:
            highest_avg = average_score
            top_student = student
    print(f"\nThe student with the highest average score is {top_student} with an average score of {highest_avg:.2f}")

calculate_average_scores(students_scores)
highest_average_score(students_scores)
