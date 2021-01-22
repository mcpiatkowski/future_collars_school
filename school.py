import sys

wychowawcy = []
nauczyciele = []
uczniowie = []


def download_data():
    data = []
    while True:
        data.append(input())
        if data[-1] == "":
            del data[-1]
            break
    return data


class Wychowawca:

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __str__(self):
        return f'{self.name} - {self.grade}'


class Nauczyciel:

    def __init__(self, name, subject, grade):
        self.name = name
        self.subject = subject
        self.grade = grade


class Uczen:

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade


def wychowawca():
    name = input()
    wychowawca = Wychowawca(name, download_data())
    wychowawcy.append(wychowawca)


def nauczyciel():
    name = input()
    subject = input()
    nauczyciel = Nauczyciel(name, subject, download_data())
    nauczyciele.append(nauczyciel)


def uczen():
    name = input()
    grade = input()
    uczen = Uczen(name, grade)
    uczniowie.append(uczen)


def print_wychowawca_argv():
    for wychowawca in wychowawcy:
        if sys.argv[1] in wychowawca.grade:
            print(wychowawca.name)
        if wychowawca.name == sys.argv[1]:
            for uczen in uczniowie:
                if uczen.grade in wychowawca.grade:
                    print(uczen.name)


def print_teacher_argv():
    for nauczyciel in nauczyciele:
        if nauczyciel.name == sys.argv[1]:
            for wychowawca in wychowawcy:
                for grade in wychowawca.grade:
                    if grade in nauczyciel.grade:
                        print(wychowawca.name)
                        break


def print_student_argv():
    for uczen in uczniowie:
        if sys.argv[1] == uczen.grade:
            print(uczen.name)
        if uczen.name == sys.argv[1]:
            for nauczyciel in nauczyciele:
                if uczen.grade in nauczyciel.grade:
                    print(nauczyciel.subject)
                    print(nauczyciel.name)


def argv():
    print_wychowawca_argv()
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
