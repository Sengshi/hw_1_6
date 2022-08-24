class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

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
    pass


class Lecturer(Mentor):
    pass


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python']

some_reviewer.rate_hw(best_student, 'Python', 10)
some_reviewer.rate_hw(best_student, 'Python', 10)
some_reviewer.rate_hw(best_student, 'Python', 10)

some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.courses_attached += ['Python']
best_student.rate_lecture(some_lecturer, 'Python', 10)
best_student.rate_lecture(some_lecturer, 'Python', 10)
# best_student.rate_lecture(some_lecturer, 'Git', 10) # тест наличия курса

print(best_student.grades)
print(some_lecturer.leads_the_course)
