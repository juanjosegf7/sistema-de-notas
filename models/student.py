class Student:
    "Representa un estudiante con sus notas por materia y por periodo."

    def __init__(self, name: str):
        self.name = name
        self.grades: dict[str, list[float]] = {}
        self.finalGrades: dict[str, float] = {}
        self.average: float = 0.0

    def addGrade(
        self,
        subjectName: str,
        period: int,
        grade: float,
        periodCount: int,
    ) -> None:
        "Guarda la nota en el periodo correspondiente usando un vector de periodos."
        if subjectName not in self.grades:
            self.grades[subjectName] = [0.0] * periodCount

        self.grades[subjectName][period - 1] = grade

    def calculateFinalGrade(self, subjectName: str) -> float:
        "Calcula la definitiva de una materia."
        if subjectName not in self.grades or len(self.grades[subjectName]) == 0:
            self.finalGrades[subjectName] = 0.0
            return 0.0

        finalGrade = sum(self.grades[subjectName]) / len(self.grades[subjectName])
        self.finalGrades[subjectName] = finalGrade
        return finalGrade

    def calculateAverage(self) -> float:
        "Calcula el promedio general del estudiante."
        if len(self.finalGrades) == 0:
            self.average = 0.0
            return self.average

        self.average = sum(self.finalGrades.values()) / len(self.finalGrades)
        return self.average
