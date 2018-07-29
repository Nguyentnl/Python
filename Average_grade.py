lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

# Add your function below!
def average(numbers):
    total = float(sum(numbers))
    result = total / len(numbers)
    return result


def get_average(students):
    homework = average(students["homework"])
    quizzes = average(students["quizzes"])
    tests = average(students["tests"])
    sum = 0.1 * homework + 0.3 * quizzes + 0.6 * tests
    return sum


def get_letter_grade(score):
    if int(score) >= 90:
        return "A"
    elif 90 > int(score) >= 80:
        return "B"
    elif 80 > int(score) >= 70:
        return "C"
    elif 70 > int(score) >= 60:
        return "D"
    else:
        return "F"


print get_letter_grade(get_average(lloyd))
print get_letter_grade(get_average(alice))
print get_letter_grade(get_average(tyler))

def get_class_average(class_list):
    results = []
    for student in class_list:
        results.append(get_average(student))
    return average(results)


students = [alice, lloyd, tyler]
print get_class_average(students)
print get_letter_grade(get_class_average(students))
