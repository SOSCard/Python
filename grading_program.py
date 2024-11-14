# grading_program.py

# Diccionario de puntajes de los estudiantes (no modificar)
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

# Diccionario para almacenar las calificaciones
student_grades = {}

# Iteramos sobre el diccionario student_scores
for student, score in student_scores.items():
    if 91 <= score <= 100:
        grade = "Outstanding"
    elif 81 <= score <= 90:
        grade = "Exceeds Expectations"
    elif 71 <= score <= 80:
        grade = "Acceptable"
    else:
        grade = "Fail"
    
    student_grades[student] = grade

# Imprimimos el resultado
print(student_grades)
