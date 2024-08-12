import unittest
from hello_world import hello_world  # Replace 'your_module' with the actual module name


class TestHelloWorld(unittest.TestCase):
    def test_hello_world_specific_values(self):
        raised = False
        try:
            hello_world()
        except (RuntimeError, TypeError, NameError):
            raised = True
        self.assertFalse(raised, 'hello_world() function raised an exception')

if __name__ == '__main__':
    unittest.main()
