from react import *
import requests
from record import *
import unittest


reminder_str = "Please remind me to order a pizza at 7pm"
origin = "Paris"


class ParsingFunctionsTests(unittest.TestCase):

    def test_task_parsing(self):
        self.assertEqual(parse_task(reminder_str), "order a pizza")

    def test_time_parsing(self):
        self.assertEqual(parse_time(reminder_str), "2017-01-29 19:00")


class APICallsTests(unittest.TestCase):

    def test_get_weather(self):
        r = requests.get("http://127.0.0.1:8000/weather/london")
        self.assertEqual(r.status_code, 200)

    def test_get_directions(self):
        r = requests.get("http://127.0.0.1:8000/directions/paris/brussels")
        self.assertEqual(r.status_code, 200)
