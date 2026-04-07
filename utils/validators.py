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
            print("Error: LA NOTA DEBE ESTAR ENTRO 0 Y 10")
        except ValueError:
            print("Error: ENTRADA INVÁIDA.")
