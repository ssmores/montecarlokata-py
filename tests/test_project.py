from unittest import TestCase
from project import Project


class TestProject(TestCase):
    def test_exists(self):
        self.assertIsNotNone(Project())

    def test_zero_items(self):
        self.assertEqual(0, Project().iterations())

    def test_ten_items(self):
        self.assertEqual(5, Project(10, [2]).iterations())

    def test_ten_items_with_multiple_samples(self):
        self.assertEqual(3, Project(10, [2, 3, 4]).iterations())

