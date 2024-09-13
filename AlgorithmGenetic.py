import prettytable as prettytable
import random as rnd

POPULATION_SIZE = 50
NUMB_OF_ELITE_SCHEDULES = 1
TOURNAMENT_SELECTION_SIZE = 3
MUTATION_RATE = 0.1


class Data:
    # salones
    ROOMS = [["R1", "R1"], ["R2", "R2"]]
    # horas del dia
    MEETING_TIMES = [
        ["1", "Lunes 07:00 - 9:00"],
        ["1", "Lunes 9:00 - 11:00"],
        ["1", "Lunes 11:00 - 13:00"],
        ["2", "Martes 07:00 - 9:00"],
        ["2", "Martes 9:00 - 11:00"],
        ["2", "Martes 11:00 - 13:00"],
        ["3", "Miercoles 07:00 - 9:00"],
        ["3", "Miercoles 9:00 - 11:00"],
        ["3", "Miercoles 11:00 - 13:00"],
        ["4", "Jueves 07:00 - 9:00"],
        ["4", "Jueves 9:00 - 11:00"],
        ["4", "Jueves 11:00 - 13:00"],
        ["5", "Viernes 07:00 - 9:00"],
        ["5", "Viernes 9:00 - 11:00"],
        ["5", "Viernes 11:00 - 13:00"],
    ]
    # maestros
    INSTRUCTORS = [
        ["I1", "Dr Joel"],
        ["I2", "Mr. Julio"],
        ["I3", "Dr Hector"],
        ["I4", "Gabriel Canto"],
        ["I5", "Dr. Moncada"],
        ["I6", "Dr. Justino"],  # Da ingles,
        ["I7", "Jose Canepa"],
        ["I8", "Coco"],
        ["I9", "Chadble"],
        ["I10", "Buscando"],
        ["I11", "Buscando2"],
        ["I12", "Wicho"],
        ["I13", "Santy"],
        ["I14", "Sebas"],
        ["I15", "Interian"],
    ]

    def __init__(self):
        self._rooms = []
        self._meetingTimes = []
        self._instructors = []
        for i in range(0, len(self.ROOMS)):
            self._rooms.append(Room(self.ROOMS[i][0], self.ROOMS[i][1]))
        for i in range(0, len(self.MEETING_TIMES)):
            self._meetingTimes.append(
                MeetingTime(self.MEETING_TIMES[i][0], self.MEETING_TIMES[i][1])
            )
        for i in range(0, len(self.INSTRUCTORS)):
            self._instructors.append(
                Instructor(self.INSTRUCTORS[i][0], self.INSTRUCTORS[i][1])
            )
        # Materia -> nombre,edificio, maestro que la pueden dar,Salon
        # Materias de ITS 1
        course1 = Course("Elaboracion de Textos", "Edificio B", [self._instructors[0]], "R1")
        course2 = Course("Ingles 1", "Edificio B", [self._instructors[1]], "R1")
        course3 = Course("Algebra y Geometria", "Edificio B", [self._instructors[2]], "R1")
        course4 = Course("Metodologia", "Edificio B", [self._instructors[3]], "R1")
        course5 = Course("Fundamentos de programacion", "Edificio B", [self._instructors[4]], "R1")
        course6 = Course("Introduccion a la ingenieria", "Edificio B", [self._instructors[5]], "R1")
        course7 = Course("Quimica", "Edificio B", [self._instructors[6]], "R1")

        # Materias de ISC 1  8-15
        course8 = Course("Algebra Superior", "Edificio C", [self._instructors[7]], "R2")
        course9 = Course("Geometria", "Edificio C", [self._instructors[8]], "R2")
        course10 = Course("Expresion Grafica", "Edificio C", [self._instructors[9]], "R2")
        course11 = Course("Logica de la programacion", "Edificio C", [self._instructors[10]], "R2")
        course12 = Course( "Calculo diferencial", "Edificio C", [self._instructors[11]], "R2")
        course13 = Course( "Elaboracion de Textos", "Edificio C", [self._instructors[12]], "R2")
        course14 = Course("Ingles 1", "Edificio C", [self._instructors[13]], "R2")
        course15 = Course( "Introduccion a la ingenieria", "Edificio C", [self._instructors[14]], "R2")
        # course16 = Course("Materia extra","Edificio C", [self._instructors[9]], "R2")
        # Se crean los cursos
        self._courses = [
            course1,
            course2,
            course3,
            course4,
            course5,
            course6,
            course7,
            course8,
            course9,
            course10,
            course11,
            course12,
            course13,
            course14,
            course15,
        ]
        # grupo con los cursos que se dan
        dept0 = Department(
            "ITS_1_A",
            [
                course1,
                course1,
                course2,
                course2,
                course3,
                course3,
                course3,
                course4,
                course4,
                course5,
                course5,
                course6,
                course6,
                course7,
                course7,
            ],
        )
        # Compartidas 1ero
        dept1 = Department(
            "ISC_1_A",
            [
                course8,
                course8,
                course9,
                course9,
                course10,
                course10,
                course11,
                course11,
                course12,
                course12,
                course13,
                course13,
                course14,
                course14,
                course15,
            ],
        )  # ,course3])
        dept2 = Department(
            "ISC_1_B",
            [
                course8,
                course8,
                course9,
                course9,
                course10,
                course10,
                course11,
                course11,
                course12,
                course12,
                course13,
                course13,
                course14,
                course14,
                course15,
                course15,
            ],
        )  # ,course3])

        # ISC1 A y B
        # dept8 = Department("Algebra Superior", [course2,course3])
        # dept9 = Department("Geometria", [course2, course3])
        # dept10 = Department("Expresion Grafica", [course2 , course3])
        # dept11 = Department("Logica de la programacion", [course2, course3])
        # dept12 = Department("Calculo diferencial", [course2, course3])

        # Compartidas 3ero
        # dept13 = Department("Probabilidad y estadistica", [course4, course5,course6])
        # dept14 = Department("Ingles 3", [course4, course5, course6])
        # dept15 = Department("Calculo Vectorial", [course4, course5, course6])

        # ITS 3ero
        # dept16 = Department("Sistemas Operativos", [course4])
        # dept17 = Department("Logica digital", [course4])
        # dept18 = Department("Estructura de Datos", [course4])
        # dept19 = Department("Fisica 1", [course4])

        # ISC 3ero
        # dept20 = Department("Analisis de Circuitos", [course5, course6])
        # dept21 = Department("Contabilidad", [course5, course6])
        # dept22 = Department("Lenguaje de programacion 2", [course5, course6])
        # dept23 = Department("Matematicas para la computacion", [course5, course6])
        self._depts = [dept0]  # , dept1,dept2
        # self._depts = [dept1, dept2, dept3,dept4, dept5,dept6, dept7]#,dept8, dept9, dept10,dept11, dept12]
        # dept13, dept14, dept15,dept16, dept17,dept18, dept19,dept20, dept21, dept22,dept23]
        self._numberOfClasses = 0
        for i in range(0, len(self._depts)):
            self._numberOfClasses += len(self._depts[i].get_courses())

    def get_rooms(self):
        return self._rooms

    def get_instructors(self):
        return self._instructors

    def get_courses(self):
        return self._courses

    def get_depts(self):
        return self._depts

    def get_meetingTimes(self):
        return self._meetingTimes

    def get_numberOfClasses(self):
        return self._numberOfClasses


class Schedule:
    def __init__(self):
        self._data = data
        self._classes = []
        self._numbOfConflicts = 0
        self._fitness = -1
        self._classNumb = 0
        self._isFitnessChanged = True

    def get_classes(self):
        self._isFitnessChanged = True
        return self._classes

    def get_numbOfConflicts(self):
        return self._numbOfConflicts

    def get_fitness(self):
        if self._isFitnessChanged == True:
            self._fitness = self.calculate_fitness()
            self._isFitnessChanged = False
        return self._fitness

    def initialize(self):
        depts = self._data.get_depts()
        for i in range(0, len(depts)):
            courses = depts[i].get_courses()
            for j in range(0, len(courses)):
                newClass = Class(self._classNumb, depts[i], courses[j])
                self._classNumb += 1
                newClass.set_meetingTime(
                    data.get_meetingTimes()[
                        rnd.randrange(0, len(data.get_meetingTimes()))
                    ]
                )
                newClass.set_room(
                    data.get_rooms()[rnd.randrange(0, len(data.get_rooms()))]
                )
                newClass.set_instructor(
                    courses[j].get_instructors()[
                        rnd.randrange(0, len(courses[j].get_instructors()))
                    ]
                )
                self._classes.append(newClass)
        return self

    def calculate_fitness(self):
        self._numbOfConflicts = 0
        classes = self.get_classes()

        for i in range(len(classes)):
            # Verifica si la capacidad del aula es menor que el número máximo de estudiantes del curso
            if (
                classes[i].get_room().get_seatingCapacity()
                != classes[i].get_course().salon()
            ):
                self._numbOfConflicts += 1

            for j in range(i + 1, len(classes)):
                # Verifica si el horario y el aula coinciden
                if (
                    classes[i].get_meetingTime() == classes[j].get_meetingTime()
                    and classes[i].get_id() != classes[j].get_id()
                ):
                    if classes[i].get_room() == classes[j].get_room():
                        self._numbOfConflicts += 1
                    # Verifica si el instructor coincide
                    if classes[i].get_instructor() == classes[j].get_instructor():
                        self._numbOfConflicts += 1

                # **Nueva Verificación: Mismo Curso en el Mismo Día**
                if classes[i].get_course() == classes[j].get_course():
                    if (
                        classes[i].get_meetingTime().get_id()
                        == classes[j].get_meetingTime().get_id()
                    ):
                        self._numbOfConflicts += 1

        return 1 / ((1.0 * self._numbOfConflicts + 1))

    def __str__(self):
        returnValue = ""
        for i in range(0, len(self._classes) - 1):
            returnValue += str(self._classes[i]) + ", "
        returnValue += str(self._classes[len(self._classes) - 1])
        return returnValue


class Population:
    def __init__(self, size):
        self._size = size
        self._data = data
        self._schedules = []
        for i in range(0, size):
            self._schedules.append(Schedule().initialize())

    def get_schedules(self):
        return self._schedules


class GeneticAlgorithm:
    def evolve(self, population):
        return self._mutate_population(self._crossover_population(population))

    def _crossover_population(self, pop):
        crossover_pop = Population(0)
        for i in range(NUMB_OF_ELITE_SCHEDULES):
            crossover_pop.get_schedules().append(pop.get_schedules()[i])
        i = NUMB_OF_ELITE_SCHEDULES
        while i < POPULATION_SIZE:
            schedule1 = self._select_tournament_population(pop).get_schedules()[0]
            schedule2 = self._select_tournament_population(pop).get_schedules()[0]
            crossover_pop.get_schedules().append(
                self._crossover_schedule(schedule1, schedule2)
            )
            i += 1
        return crossover_pop

    def _mutate_population(self, population):
        for i in range(NUMB_OF_ELITE_SCHEDULES, POPULATION_SIZE):
            self._mutate_schedule(population.get_schedules()[i])
        return population

    def _crossover_schedule(self, schedule1, schedule2):
        crossoverSchedule = Schedule().initialize()
        for i in range(0, len(crossoverSchedule.get_classes())):
            if rnd.random() > 0.5:
                crossoverSchedule.get_classes()[i] = schedule1.get_classes()[i]
            else:
                crossoverSchedule.get_classes()[i] = schedule2.get_classes()[i]
        return crossoverSchedule

    def _mutate_schedule(self, mutateSchedule):
        schedule = Schedule().initialize()
        for i in range(0, len(mutateSchedule.get_classes())):
            if MUTATION_RATE > rnd.random():
                mutateSchedule.get_classes()[i] = schedule.get_classes()[i]
        return mutateSchedule

    def _select_tournament_population(self, pop):
        tournament_pop = Population(0)
        i = 0
        while i < TOURNAMENT_SELECTION_SIZE:
            tournament_pop.get_schedules().append(
                pop.get_schedules()[rnd.randrange(0, POPULATION_SIZE)]
            )
            i += 1
        tournament_pop.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
        return tournament_pop


class Course:
    def __init__(self, number, name, instructors, salon):  # maxNumbOfStudents):
        self._number = number
        self._name = name
        self._salon = salon
        self._instructors = instructors

    def get_number(self):
        return self._number

    def get_name(self):
        return self._name

    def get_instructors(self):
        return self._instructors

    def salon(self):
        return self._salon

    def __str__(self):
        return self._name


class Instructor:
    def __init__(self, id, name):
        self._id = id
        self._name = name

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def __str__(self):
        return self._name


class Room:
    def __init__(self, number, seatingCapacity):
        self._number = number
        self._seatingCapacity = seatingCapacity

    def get_number(self):
        return self._number

    def get_seatingCapacity(self):
        return self._seatingCapacity


class MeetingTime:
    def __init__(self, id, time):
        self._id = id
        self._time = time

    def get_id(self):
        return self._id

    def get_time(self):
        return self._time


class Department:
    def __init__(self, name, courses):
        self._name = name
        self._courses = courses

    def get_name(self):
        return self._name

    def get_courses(self):
        return self._courses


class Class:
    def __init__(self, id, dept, course):
        self._id = id
        self._dept = dept
        self._course = course
        self._instructor = None
        self._meetingTime = None
        self._room = None

    def get_id(self):
        return self._id

    def get_dept(self):
        return self._dept

    def get_course(self):
        return self._course

    def get_instructor(self):
        return self._instructor

    def get_meetingTime(self):
        return self._meetingTime

    def get_room(self):
        return self._room

    def set_instructor(self, instructor):
        self._instructor = instructor

    def set_meetingTime(self, meetingTime):
        self._meetingTime = meetingTime

    def set_room(self, room):
        self._room = room

    def __str__(self):
        return (
            str(self._dept.get_name())
            + ","
            + str(self._course.get_number())
            + ","
            + str(self._room.get_number())
            + ","
            + str(self._instructor.get_id())
            + ","
            + str(self._meetingTime.get_id())
        )


class DisplayMgr:
    def print_available_data(self):
        print("> All Available Data")
        self.print_dept()
        self.print_course()
        self.print_room()
        self.print_instructor()
        self.print_meeting_times()

    def print_dept(self):
        depts = data.get_depts()
        availableDeptsTable = prettytable.PrettyTable(["dept", "courses"])
        for i in range(0, len(depts)):
            courses = depts.__getitem__(i).get_courses()
            tempStr = "["
            for j in range(0, len(courses) - 1):
                tempStr += courses[j].__str__() + ", "
            tempStr += courses[len(courses) - 1].__str__() + "]"
            availableDeptsTable.add_row([depts.__getitem__(i).get_name(), tempStr])
        print(availableDeptsTable)

    def print_course(self):
        availableCoursesTable = prettytable.PrettyTable(
            ["id", "course #", "max # of students", "instructors"]
        )
        courses = data.get_courses()
        for i in range(0, len(courses)):
            instructors = courses[i].get_instructors()
            tempStr = ""
            for j in range(0, len(instructors) - 1):
                tempStr += instructors[j].__str__() + ", "
            tempStr += instructors[len(instructors) - 1].__str__()
            availableCoursesTable.add_row(
                [
                    courses[i].get_number(),
                    courses[i].get_name(),
                    str(courses[i].salon()),
                    tempStr,
                ]
            )
        print(availableCoursesTable)

    def print_instructor(self):
        availableInstructorsTable = prettytable.PrettyTable(["id", "instructor"])
        instructors = data.get_instructors()
        for i in range(0, len(instructors)):
            availableInstructorsTable.add_row(
                [instructors[i].get_id(), instructors[i].get_name()]
            )
        print(availableInstructorsTable)

    def print_room(self):
        availableRoomsTable = prettytable.PrettyTable(
            ["room #", "max seating capacity"]
        )
        rooms = data.get_rooms()
        for i in range(0, len(rooms)):
            availableRoomsTable.add_row(
                [str(rooms[i].get_number()), str(rooms[i].get_seatingCapacity())]
            )
        print(availableRoomsTable)

    def print_meeting_times(self):
        availableMeetingTimeTable = prettytable.PrettyTable(["id", "Meeting Time"])
        # esta variable es interesante no se que hace
        meetingTimes = data.get_meetingTimes()
        for i in range(0, len(meetingTimes)):
            availableMeetingTimeTable.add_row(
                [meetingTimes[i].get_id(), meetingTimes[i].get_time()]
            )
        print(availableMeetingTimeTable)

    def print_generation(self, population):
        table1 = prettytable.PrettyTable(
            [
                "schedule #",
                "fitness",
                "# of conflicts",
                "classes [dept,class,room,instructor,meeting-time]",
            ]
        )
        schedules = population.get_schedules()
        for i in range(0, len(schedules)):
            table1.add_row(
                [
                    str(i),
                    round(schedules[i].get_fitness(), 3),
                    schedules[i].get_numbOfConflicts(),
                    schedules[i].__str__(),
                ]
            )
        print(table1)

    def print_schedule_as_table(self, schedule):
        classes = schedule.get_classes()
        classes_by_day = {}

        # agrupar clases por día
        for c in classes:
            day = c.get_meetingTime().get_id()  # obtener el ID del día (1 para lunes, 2 para martes, etc.)
            if day not in classes_by_day:
                classes_by_day[day] = []
            classes_by_day[day].append(c)

        # ordenar los días en orden ascendente (lunes = 1, martes = 2, etc.)
        for day in sorted(classes_by_day.keys()):
            # ordenar las clases dentro del día por hora
            day_classes = classes_by_day[day]
            day_classes.sort(key=lambda x: x.get_meetingTime().get_time())

            # encabezado del día
            print(f"\nDía {day}")  
            
            # crear la tabla para el día
            table = prettytable.PrettyTable(["Time", "Course", "Room", "Instructor"])
            
            # añadir las clases a la tabla con su información
            for c in day_classes:
                table.add_row(
                    [
                        c.get_meetingTime().get_time(),  # Hora de la clase
                        f"{c.get_course().get_name()} ({c.get_course().get_number()}, {c.get_course().salon()})",  # Curso
                        f"{c.get_room().get_number()} ({c.get_room().get_seatingCapacity()})",  # Aula
                        f"{c.get_instructor().get_name()} ({c.get_instructor().get_id()})",  # Instructor
                    ]
                )
            # imprimir la tabla del día
            print(table)


data = Data()
displayMgr = DisplayMgr()
displayMgr.print_available_data()
generationNumber = 0
print("\n> Generation # " + str(generationNumber))
population = Population(POPULATION_SIZE)
population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
displayMgr.print_generation(population)
displayMgr.print_schedule_as_table(population.get_schedules()[0])
geneticAlgorithm = GeneticAlgorithm()
while population.get_schedules()[0].get_fitness() != 1.0:
    generationNumber += 1
    print("\n> Generation # " + str(generationNumber))
    population = geneticAlgorithm.evolve(population)
    population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
    displayMgr.print_generation(population)
    displayMgr.print_schedule_as_table(population.get_schedules()[0])
print("\n\n")
"""
    MEETING_TIMES_5 = [["1", "Lunes 07:00 - 9:00"],
                    ["1", "Lunes 9:00 - 11:00"],
                    ["1", "Lunes 11:00 - 13:00"],
                    ["1", "Lunes 13:00 - 15:00"],
                    ["1", "Lunes 15:00 - 17:00"],
                    ["2", "Martes 07:00 - 9:00"],
                    ["2", "Martes 9:00 - 11:00"],
                    ["2", "Martes 11:00 - 13:00"],
                    ["2", "Martes 13:00 - 15:00"],
                    ["2", "Martes 15:00 - 17:00"],
                    ["3", "Miercoles 07:00 - 9:00"],
                    ["3", "Miercoles 9:00 - 11:00"],
                    ["3", "Miercoles 11:00 - 13:00"],
                    ["3", "Miercoles 13:00 - 15:00"],
                    ["3", "Miercoles 15:00 - 17:00"],
                    ["4", "Jueves 07:00 - 9:00"],
                    ["4", "Jueves 9:00 - 11:00"],
                    ["4", "Jueves 11:00 - 13:00"],
                    ["4", "Jueves 13:00 - 15:00"],
                    ["4", "Jueves 15:00 - 17:00"],                     
                    ["5", "Viernes 07:00 - 9:00"],
                    ["5", "Viernes 9:00 - 11:00"],
                    ["5", "Viernes 11:00 - 13:00"],
                    ["5", "Viernes 13:00 - 15:00"],
                    ["5", "Viernes 15:00 - 17:00"]
    ]
"""
