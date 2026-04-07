def requestInteger(message: str) -> int:
    "Solicita un número entero válido."
    while True:
        try:
            value = int(input(message))
            if value > 0:
                return value
            print("Error: INGRESE UN NÚMERO MAYOR QUE CERO.")
        except ValueError:
            print("Error: SÓLO SE PERMITEN NÚMEROS ENTEROS.")


def requestText(message: str) -> str:
    "Solicita texto no vacío."
    while True:
        value = input(message).strip()
        if value:
            return value
        print("Error: EL TEXTO NO PUEDE ESTAR VACÍO.")


def requestGrade(message: str) -> float:
    "Solicita una nota entre 0 y 10."
    while True:
        try:
            value = float(input(message))
            if 0 <= value <= 10:
                return value
            print("Error: LA NOTA DEBE ESTAR ENTRE 0 Y 10.")
        except ValueError:
            print("Error: ENTRADA INVÁLIDA.")


def getEquivalentLetter(grade: float) -> str:
    "Retorna la equivalencia en letra con signo según la nota."
    if grade < 0 or grade > 10:
        return "SIN EQUIVALENCIA"

    if grade < 7.0:
        return buildLetterWithSign(grade, 0.0, 6.9, "F")
    if grade < 8.0:
        return buildLetterWithSign(grade, 7.0, 7.9, "R")
    if grade < 9.0:
        return buildLetterWithSign(grade, 8.0, 8.9, "B")
    return buildLetterWithSign(grade, 9.0, 10.0, "A")


def buildLetterWithSign(
    grade: float, rangeStart: float, rangeEnd: float, letter: str
) -> str:
    "Asigna signo -, neutro o + dentro del rango de la letra."
    if grade == rangeEnd:
        return f"{letter}+"

    rangeWidth = rangeEnd - rangeStart
    if rangeWidth <= 0:
        return letter

    relativePosition = (grade - rangeStart) / rangeWidth

    if relativePosition < (1 / 3):
        return f"{letter}-"
    if relativePosition < (2 / 3):
        return letter
    return f"{letter}+"
