from django.test import TestCase, Client
from TA_Scheduler.models import User, Course
# Create your tests here.
class CreateCourse(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(username="supervisor", password="secret")

    def test_createCourseRedirect(self):
        self.client.post("/", {"username": "supervisor", "password": "secret"})
        response = self.client.post("/createcourse/", {"name": "new course", "number": "1"})
        self.assertEquals(response.url.__str__(), '/courses/', msg="Creating courses does not redirect to courses page")

    def test_createNewCourse(self):
        self.client.post("/", {"username": "supervisor", "password": "secret"})
        response = self.client.post("/createcourse/", {"name": "new course", "number": "1"}, follow=True)
        self.assertEqual(response.context["courses"], [self.course.name, "added"], msg="Can not add course")

    def test_createDuplicateCourseName(self):
        self.client.post("/", {"username": "supervisor", "password": "secret"})
        self.client.post("/createcourse/", {"name": "new course", "number": "1"}, follow=True)
        response = self.client.post("/createcourse/", {"name": "new course", "number": "2"}, follow=True)
        self.assertEqual(response.context["message"], "Enter a unique course name and number",
                         msg="Course name was duplicated")

    def test_createDuplicateCourseNumber(self):
        self.client.post("/", {"username": "supervisor", "password": "secret"})
        response = self.client.post("/createcourse/", {"name": "new course", "number": "1"}, follow=True)
        response = self.client.post("/createcourse/", {"name": "another new course", "number": "1"}, follow=True)
        self.assertEqual(response.context["message"], "Enter a unique course name and number",
                         msg="Course number was duplicated")

    def test_createCourseNoName(self):
        self.client.post("/", {"username": "supervisor", "password": "secret"})
        response = self.client.post("/createcourse/", {"name": "", "number": "1"}, follow=True)
        self.assertEqual(response.context["message"], "Enter a unique course name and number",
                         msg="Course did not have a name")

    def test_createCourseNoNumber(self):
        self.client.post("/", {"username": "supervisor", "password": "secret"})
        response = self.client.post("/createcourse/", {"name": "new course", "number": ""}, follow=True)
        self.assertEqual(response.context["message"], "Enter a unique course name and number",
                         msg="Course did not have a number")

    def test_createCourseNotANumber(self):
        self.client.post("/", {"username": "supervisor", "password": "secret"})
        response = self.client.post("/createcourse/", {"name": "new course", "number": "a"}, follow=True)
        self.assertEqual(response.context["message"], "Enter a unique course name and number",
                         msg="Course number was not an integer")


