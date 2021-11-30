from django.test import TestCase, Client
from TA_Scheduler.models import User
# Create your tests here.
class Login(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(username="existingUser", password="secret")

    def test_loginGoesToHomeView(self):
        response = self.client.post("/", {"username": "existingUser", "password": "secret"})
        self.assertEquals(response.url.__str__(), '/homeView/',
                          msg="Logging in does not navigate user to user's home page")

    def test_wrongPasssword(self):
        response = self.client.post("/", {"username": "existingUser", "password": "wrongPassword"}, follow=True)
        self.assertEqual(response.context["message"], "bad password", msg="Wrong password message not displayed with incorrect password")

    def test_noPassword(self):
        response = self.client.post("/", {"username": "existingUser", "password": ""}, follow=True)
        self.assertEqual(response.context["message"], "bad password",
                         msg="No bad password message when user does not enter a password")

    def test_wrongUsername(self):
        response = self.client.post("/", {"wrongUsername": "", "password": "secret"}, follow=True)
        self.assertEqual(response.context["message"], "bad username",
                         msg="No bad username message when user does not enter a password")

    def test_noUsername(self):
        response = self.client.post("/", {"username": "", "password": "secret"}, follow=True)
        self.assertEqual(response.context["message"], "bad username",
                         msg="No bad username message when user does not enter a password")

    def test_logout(self):
        self.client.post("/", {"username": "existingUser", "password": "secret"}, follow=True)
        response = self.client.get("/", {}, follow=True)
        with self.assertRaises(KeyError, msg="Logged in user did not successfully logout"):
            response.context["username"]

    def test_switchUsers(self):
        self.client.post("/", {"username": "existingUser", "password": "secret"}, follow=True)
        self.client.get("/", {}, follow=True)
        response = self.client.post("/", {"username": "newUser", "password": "secret"}, follow=True)
        self.assertEquals(response.context["username"], "newUser", msg="Switching users was unsuccessful")

