from models.student import Student
from models.subject import Subject
from utils.validators import (
    requestInteger,
    requestText,
    requestGrade,
    getEquivalentLetter,
)


class GradeSystem:
    "Gestiona estudiantes, materias, periodos y notas."

    def __init__(self):
        self.students: list[Student] = []
        self.subjects: list[Subject] = []
        self.periodCount: int = 0
        self.courseAverage: float = 0.0
        self.failedByPeriod: dict[int, int] = {}
        self.failedFinal: int = 0
        self.approvalPercentage: float = 0.0
        self.failurePercentage: float = 0.0

    def registerPeriods(self) -> None:
        "Solicita la cantidad de periodos (mínimo 3)."
        while True:
            periodCount = requestInteger("Ingrese la cantidad de periodos (mínimo 3): ")
            if periodCount >= 3:
                self.periodCount = periodCount
                break
            print("Error: DEBE INGRESAR MÍNIMO 3 PERÍODOS.")

    def registerSubjects(self) -> None:
        "Solicita y registra las materias."
        while True:
            subjectCount = requestInteger(
                "Ingrese la cantidad de materias (mínimo 3): "
            )
            if subjectCount >= 3:
                break
            print("Error: DEBE INGRESAR MÍNIMO 3 MATERIAS.")

        for index in range(subjectCount):
            subjectName = requestText(f"Ingrese el nombre de la materia #{index + 1}: ")
            self.subjects.append(Subject(subjectName))

    def registerStudents(self) -> None:
        "Solicita y registra los estudiantes."
        studentCount = requestInteger("Ingrese la cantidad de estudiantes: ")

        for index in range(studentCount):
            studentName = requestText(
                f"Ingrese el nombre del estudiante #{index + 1}: "
            )
            self.students.append(Student(studentName))

    def requestGrades(self) -> None:
        "Solicita las notas por materia y por periodo."
        for student in self.students:
            print(f"\nRegistro de notas para {student.name}")

            for subject in self.subjects:
                print(f"\nMateria: {subject.name}")

                for period in range(1, self.periodCount + 1):
                    grade = requestGrade(
                        f"Ingrese la nota del periodo {period} para {student.name}: "
                    )
                    student.addGrade(
                        subject.name,
                        period,
                        grade,
                        self.periodCount,
                    )

    def calculateFinalGrades(self) -> None:
        "Calcula definitivas por materia y promedio por estudiante."
        for student in self.students:
            for subject in self.subjects:
                student.calculateFinalGrade(subject.name)
            student.calculateAverage()

    def calculateCourseAverage(self) -> float:
        "Calcula el promedio general del curso."
        total = 0.0
        count = 0

        for student in self.students:
            for subject in self.subjects:
                if subject.name in student.finalGrades:
                    total += student.finalGrades[subject.name]
                    count += 1

        if count > 0:
            self.courseAverage = total / count
        else:
            self.courseAverage = 0.0

        return self.courseAverage

    def calculateStatistics(self) -> None:
        "Calcula reprobados por periodo y estadísticas finales."
        self.failedByPeriod = {}
        self.failedFinal = 0

        for period in range(1, self.periodCount + 1):
            self.failedByPeriod[period] = 0

        totalFinals = 0

        for student in self.students:
            for subject in self.subjects:
                subjectGrades = student.grades.get(subject.name, [])

                for periodIndex, grade in enumerate(subjectGrades, start=1):
                    if grade < 7.0:
                        self.failedByPeriod[periodIndex] += 1

                finalGrade = student.finalGrades.get(subject.name, 0.0)
                totalFinals += 1
                if finalGrade < 7.0:
                    self.failedFinal += 1

        if totalFinals > 0:
            approvedCount = totalFinals - self.failedFinal
            self.approvalPercentage = (approvedCount / totalFinals) * 100
            self.failurePercentage = (self.failedFinal / totalFinals) * 100
        else:
            self.approvalPercentage = 0.0
            self.failurePercentage = 0.0

    def displayData(self) -> None:
        "Muestra los datos registrados y las salidas solicitadas."
        print("\n*** RESULTADOS DEL SISTEMA ***")
        print(f"Cantidad de periodos: {self.periodCount}")

        for student in self.students:
            print(f"\nEstudiante: {student.name}")

            for subject in self.subjects:
                print(f"- {subject.name}:")
                grades = student.grades.get(subject.name, [])

                for index, grade in enumerate(grades, start=1):
                    print(f"  Periodo {index}: {grade:.2f}")

                finalGrade = student.finalGrades.get(subject.name, 0.0)
                letter = getEquivalentLetter(finalGrade)
                status = "APRUEBA" if finalGrade >= 7.0 else "REPRUEBA"
                print(f"  Definitiva: {finalGrade:.2f} -> {letter} ({status})")

            averageLetter = getEquivalentLetter(student.average)
            print(f"Promedio del estudiante: {student.average:.2f} -> {averageLetter}")

        print(
            f"\nPromedio general del curso: {self.courseAverage:.2f} -> {getEquivalentLetter(self.courseAverage)}"
        )

        print("\nCantidad de reprobados por periodo:")
        for period, failedCount in self.failedByPeriod.items():
            print(f"- Periodo {period}: {failedCount}")

        print(f"\nCantidad de reprobados en definitiva: {self.failedFinal}")
        print(f"Porcentaje de aprobación: {self.approvalPercentage:.2f}%")
        print(f"Porcentaje de desaprobación: {self.failurePercentage:.2f}%")
