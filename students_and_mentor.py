class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        arith_mean = 0
        for v in self.grades.values():
            arith_mean += sum(v) / len(v)
        arith_mean = arith_mean / len(self.grades.keys())
        learning = ', '.join(self.courses_in_progress)
        finished = ', '.join(self.finished_courses)
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: ' \
               f'{round(arith_mean, 1)}\nКурсы в процессе изучения: {learning}\nЗавершенные курсы: {finished}'

    def rate_lecture(self, lecturer, course_leads, grade_lecture):
        if isinstance(lecturer, Lecturer) and course_leads in lecturer.courses_attached:
            if course_leads in self.courses_in_progress:
                if course_leads in lecturer.leads_the_course:
                    lecturer.leads_the_course[course_leads] += [grade_lecture]
                else:
                    lecturer.leads_the_course[course_leads] = [grade_lecture]
            else:
                return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.leads_the_course = {}

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
    def __str__(self):
        av_rating = 0
        for i in self.leads_the_course.values():
            av_rating += sum(i) / len(i)
        av_rating = av_rating / len(self.leads_the_course.keys())
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {round(av_rating, 1)}'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'Git']
best_student.finished_courses += ['Введение в программирование']

some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python']

some_reviewer.rate_hw(best_student, 'Python', 10)
some_reviewer.rate_hw(best_student, 'Python', 10)
some_reviewer.rate_hw(best_student, 'Python', 9.7)

some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.courses_attached += ['Python']
best_student.rate_lecture(some_lecturer, 'Python', 10)
best_student.rate_lecture(some_lecturer, 'Python', 9.8)

print(some_reviewer, '\n')
print(some_lecturer, '\n')
print(best_student, '\n')
