from models.gradeSystem import GradeSystem


def main() -> None:
    print("*** SISTEMA DE REGISTRO DE NOTAS ***")

    system = GradeSystem()
    system.registerPeriods()
    system.registerSubjects()
    system.registerStudents()
    system.requestGrades()
    system.displayData()


if __name__ == "__main__":
    main()
