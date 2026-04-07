class Student:
    "Representa un estudiante con sus notas por materia y por periodo."

    def __init__(self, name: str):
        self.name = name
        self.grades: dict[str, list[float]] = {}

    def addGrade(
        self,
        subjectName: str,
        period: int,
        grade: float,
        periodCount: int,
    ) -> None:
        "Guarda la nota en el periodo correspondiente."
        if subjectName not in self.grades:
            self.grades[subjectName] = [0.0] * periodCount

        self.grades[subjectName][period - 1] = grade

    def displayGrades(self) -> None:
        "Muestra las notas registradas."
        print(f"\nNotas de {self.name}:")
        for subjectName, grades in self.grades.items():
            print(f"- {subjectName}:")
            for index, grade in enumerate(grades, start=1):
                print(f"Periodo {index}: {grade}")
