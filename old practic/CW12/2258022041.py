
import unittest
import redis

from model import Student

class TestStudentMethods(unittest.TestCase):

    def setUp(self):
        self.redis_client = redis.Redis()

    def test_save(self):
        student = Student('Ali', 20)
        student.save()

        student_from_redis = self.redis_client.hmget(
            f'student:{student.student_number}:info',
            'name'
        )

        print(student_from_redis)

        self.assertIsNotNone(student_from_redis)
        self.assertEqual(student_from_redis[0].decode('utf-8'), student.name)

    def test_student_number_incr(self):
        student_number = self.redis_client.get('student_number').decode('utf-8')

        student = Student('Ali', 20)
        student.save()

        student = Student('Mohammad', 25)
        student.save()

        new_student_number = self.redis_client.get('student_number').decode('utf-8')

        self.assertEqual(int(new_student_number), int(student_number)+2)