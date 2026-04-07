from models.student import Student
from models.subject import Subject
from utils.validators import requestInteger, requestText, requestGrade


class GradeSystem:
    "Gestiona estudiantes, materias, periodos y notas."

    def __init__(self):
        self.students: list[Student] = []
        self.subjects: list[Subject] = []
        self.periodCount: int = 0

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
        subjectCount = requestInteger("Ingrese la cantidad de materias: ")

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

    def displayData(self) -> None:
        "Muestra los datos registrados."
        print("\n*** DATOS REGISTRADOS ***")
        print(f"Cantidad de periodos: {self.periodCount}")

        for student in self.students:
            student.displayGrades()
