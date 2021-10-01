from typing import AsyncGenerator
import redis
redis_client = redis.Redis()
redis_client.set("student_number", 1400)


class Student:
    all_student = []

    def __init__(self, name, age) -> None:
        redis_client.incr('student_number')
        self.student_number = redis_client.get(
            'student_number').decode('utf-8')
        self.name = name
        self.age = age
        self.save()
        self.get_all_students()

    def save(self):
        redis_client.hmset(
            f'student:{self.student_number}:info',
            {
                "name": self.name,
                "age": self.age,
                "student_number": self.student_number
            }
        )

    def add_grade(self, *args):
        self.args = args
        redis_client.rpush(
            f'student:{self.student_number}:grade',
            *self.args
        )

    def get_gpa(self):
        l = list(map(int, redis_client.lrange("student:1401:grade", 0, -1)))
        self.gpa = sum(l)/len(l)
        redis_client.set(
            f'student:{self.student_number}:gpa',
            self.gpa
        )

    def add_course(self, name, term):
        self.crsename = name
        self.crseterm = term
        self.crse = Course(name, term)
        redis_client.hmset(
            f'student:{self.student_number}:cource',
            {
                f"name:{self.crse.course_id}": self.crsename,
                f"term:{self.crse.course_id}": self.crseterm,
            }
        )
    import re

    def get_all_students(self):
        redis_client.hmset(
            'student',
            {
                f"name:{self.student_number}": f"{self.name}:{self.age}",
            }
        )
        return redis_client.hgetall("student")

    @ staticmethod
    def get_all_courses(cls):
        redis_client.hgetall()

    @ staticmethod
    def get_all_courses_by_term(cls, term):
        pass


redis_client.set("course_id", 140000)


class Course:

    def __init__(self, name, term) -> None:
        redis_client.incr('course_id')
        self.course_id = redis_client.get('course_id').decode('utf-8')
        self.name = name
        self.term = term


a = Student(1, 2)
print(a.student_number)
b = Student(2, 3)
print(b.student_number)
print(redis_client.hgetall("student:1401:info"))
a.add_grade(12, 13, 14, 15, 16, 17)
a.get_gpa()
print(redis_client.lrange("student:1401:grade", 0, -1))
print(redis_client.get("student:1401:gpa"))
a.add_course(10, 10)
a.add_course(30, 30)
print(redis_client.hgetall("student:1401:cource"))
print(a.get_all_students())
