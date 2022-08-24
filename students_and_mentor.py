from statistics import mean


class Student:
    students = []

    def __init__(self, name, surname, gender):
        self.students.append(self)
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        learning = ', '.join(self.courses_in_progress)
        finished = ', '.join(self.finished_courses)
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за домашние задания: {round(self.average_rating(), 1)}\n' \
               f'Курсы в процессе изучения: {learning}\n' \
               f'Завершенные курсы: {finished}'

    def rate_lecture(self, lecturer, course_leads, grade_lecture):
        if isinstance(lecturer, Lecturer) and course_leads in lecturer.courses_attached:
            if course_leads in self.courses_in_progress:
                if course_leads in lecturer.leads_the_course:
                    lecturer.leads_the_course[course_leads] += [grade_lecture]
                else:
                    lecturer.leads_the_course[course_leads] = [grade_lecture]
            else:
                return 'Ошибка'

    def average_rating(self):
        all_grade = []
        for i in self.grades.values():
            all_grade += i
        av_rating = mean(all_grade)
        return round(av_rating, 1)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.leads_the_course = {}
        if isinstance(self, Lecturer):
            Lecturer.lecturers.append(self)

    def rate_hw(self, student, course, grade):
        if isinstance(self, Reviewer) and isinstance(student, Student) and course in self.courses_attached:
            if course in student.courses_in_progress:
                if course in student.grades:
                    student.grades[course] += [grade]
                else:
                    student.grades[course] = [grade]
            else:
                return 'Ошибка'
        else:
            return 'Ошибка'


class Reviewer(Mentor):
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


class Lecturer(Mentor):
    lecturers = []

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за лекции: {round(self.average_rating(), 1)}'

    def average_rating(self):
        all_grade = []
        for i in self.leads_the_course.values():
            all_grade += i
        av_rating = mean(all_grade)
        return round(av_rating, 1)


def average_grade_students(list_students, course):
    aver_grades =[]
    for i in list_students:
        if isinstance(i, Student) and course in i.courses_in_progress:
            aver_grades += i.grades[course]
    return f'Средняя оценка студентов на курсе "{course}" - {mean(aver_grades)} %'


def average_grade_lecturer(list_lecturer, course):
    aver_grades = []
    for i in list_lecturer:
        if isinstance(i, Lecturer) and course in i.courses_attached:
            aver_grades += i.leads_the_course[course]
    return f'Средняя оценка лекторов за лекции по курсу "{course}" - {mean(aver_grades)} %'


student_1 = Student('Ruoy', 'Eman', 'your_gender')
student_1.courses_in_progress += ['Python', 'Git']
student_1.finished_courses += ['Введение в программирование']
student_2 = Student('Rubby', 'Weltson', 'male')
student_2.courses_in_progress += ['Git']
student_2.finished_courses += ['Старт в программировании']

reviewer_1 = Reviewer('Some', 'Buddy')
reviewer_1.courses_attached += ['Python']
reviewer_2 = Reviewer('Alan', 'Fron')
reviewer_2.courses_attached += ['Git']

reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 9.7)
reviewer_2.rate_hw(student_1, 'Git', 10)
reviewer_2.rate_hw(student_2, 'Git', 10)
reviewer_2.rate_hw(student_2, 'Git', 9.7)

lecturer_1 = Lecturer('Some', 'Buddy')
lecturer_1.courses_attached += ['Python']
lecturer_2 = Lecturer('Frank', 'Summers')
lecturer_2.courses_attached += ['Python', 'Git']
student_1.rate_lecture(lecturer_1, 'Python', 10)
student_1.rate_lecture(lecturer_1, 'Python', 9.8)
student_1.rate_lecture(lecturer_2, 'Python', 10)
student_1.rate_lecture(lecturer_2, 'Python', 10)
student_1.rate_lecture(lecturer_2, 'Git', 9.9)

print(reviewer_1, '\n')
print(lecturer_1, '\n')
print(student_1, '\n')

print(lecturer_1.average_rating() > lecturer_2.average_rating())
print(lecturer_2.average_rating() > lecturer_1.average_rating())
print(student_1.average_rating() > student_2.average_rating())
print(student_2.average_rating() > student_1.average_rating())

course_s = 'Git'
course_l = 'Python'
print(average_grade_students(Student.students, course_s))
print(average_grade_lecturer(Lecturer.lecturers, course_l))
