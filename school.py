import sys

head_teachers = []
teachers = []
students = []


def download_data():
    data = []
    while True:
        data.append(input())
        if data[-1] == "":
            del data[-1]
            break
    return data


class HeadTeacher:

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __str__(self):
        return f'{self.name} - {self.grade}'


class Teacher:

    def __init__(self, name, subject, grade):
        self.name = name
        self.subject = subject
        self.grade = grade


class Student:

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade


def wychowawca():
    name = input()
    head_teacher = HeadTeacher(name, download_data())
    head_teachers.append(head_teacher)


def nauczyciel():
    name = input()
    subject = input()
    teacher = Teacher(name, subject, download_data())
    teachers.append(teacher)


def uczen():
    name = input()
    grade = input()
    student = Student(name, grade)
    students.append(student)


def print_head_teacher_argv():
    for head_teacher in head_teachers:
        if sys.argv[1] in head_teacher.grade:
            print(head_teacher.name)
        if head_teacher.name == sys.argv[1]:
            for student in students:
                if student.grade in head_teacher.grade:
                    print(student.name)


def print_teacher_argv():
    for teacher in teachers:
        if teacher.name == sys.argv[1]:
            for head_teacher in head_teachers:
                for grade in head_teacher.grade:
                    if grade in teacher.grade:
                        print(head_teacher.name)
                        break


def print_student_argv():
    for student in students:
        if sys.argv[1] == student.grade:
            print(student.name)
        if student.name == sys.argv[1]:
            for teacher in teachers:
                if student.grade in teacher.grade:
                    print(teacher.subject)
                    print(teacher.name)


def argv():
    print_head_teacher_argv()
    print_teacher_argv()
    print_student_argv()


def main():
    actions = {
        "uczen": uczen,
        "nauczyciel": nauczyciel,
        "wychowawca": wychowawca
    }

    while True:

        selection = input()
        if "koniec" == selection:
            return
        toDo = actions.get(selection, "Brak takiej komendy!")
        toDo()


if __name__ == "__main__":
    main()
    argv()
