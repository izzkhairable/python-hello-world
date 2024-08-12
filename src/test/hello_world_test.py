import unittest
from src.hello_world.hello_world import hello_world


class TestHelloWorld(unittest.TestCase):
    def test_hello_world_specific_values(self):
        raised = False
        try:
            hello_world()
        except (RuntimeError, TypeError, NameError, ImportError):
            raised = True
        self.assertFalse(raised, 'hello_world() function raised an exception')


if __name__ == '__main__':
    unittest.main()
