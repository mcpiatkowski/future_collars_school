import sys

wychowawcy = []
nauczyciele = []
uczniowie = []


def divider():
    print(46 * "#")


def download_data():
    data = []
    while True:
        data.append(input("Jaka klasa? "))
        if data[-1] == "":
            del data[-1]
            break
    return data


class Wychowawca:

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade


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
    name = input("Jakie imię? ")
    wychowawca = Wychowawca(name, download_data())
    wychowawcy.append(wychowawca)
    print(wychowawcy)
    print("Imię wychowawcy: ", wychowawca.name)
    print("Klasy wychowawcy: ", wychowawca.grade)
    return wychowawca


def argv_wychowawca():
    for wychowawca in wychowawcy:
        divider()
        print("Wychowawca: ", wychowawca.name)
        print("Klasy które prowadzi: ", wychowawca.grade)


def nauczyciel():
    name = input("Jakie imię? ")
    subject = input("Jaki przedmiot? ")
    nauczyciel = Nauczyciel(name, subject, download_data())
    nauczyciele.append(nauczyciel)
    return nauczyciel


def argv_nauczyciel():
    for nauczyciel in nauczyciele:
        divider()
        print("Naczuczyciel: ", nauczyciel.name)
        print("Przedmiot: ", nauczyciel.subject)
        print("Klasy: ", nauczyciel.grade)


def uczen():
    name = input("Jakie imię? ")
    grade = input("Jaka klasa? ")
    uczen = Uczen(name, grade)
    uczniowie.append(uczen)
    return uczen


def argv_uczen():
    for uczen in uczniowie:
        divider()
        print("Uczeń: ", uczen.name)
        print("Klasa: ", uczen.grade)


def argv():
    if sys.argv[1] == 'wychowawca':
        argv_wychowawca()
    if sys.argv[1] == 'uczen':
        argv_uczen()
    if sys.argv[1] == 'nauczyciel':
        argv_nauczyciel()


def menu():
    print(20 * "#" + " MENU " + 20 * "#")
    print(46 * "#")
    print("KOMENDY: uczen, nauczyciel, wychowawca, koniec")


def main():
    actions = {
        "uczen": uczen,
        "nauczyciel": nauczyciel,
        "wychowawca": wychowawca
    }

    while True:

        menu()
        selection = input("Komenda: ")
        if "koniec" == selection:
            return
        toDo = actions.get(selection, "Brak takiej komendy!")
        toDo()


if __name__ == "__main__":
    main()
    argv()
    divider()
