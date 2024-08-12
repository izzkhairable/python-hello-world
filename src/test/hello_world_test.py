import unittest
import warnings
from src.hello_world.hello_world import hello_world


class TestHelloWorld(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', category=ResourceWarning)

    # TODO: Implement a further fine-grained test-case
    def test_hello_world(self):
        raised = False
        try:
            hello_world()
        except (RuntimeError, TypeError, NameError, ImportError):
            raised = True
        self.assertFalse(raised, 'hello_world() function raised an exception')


if __name__ == '__main__':
    unittest.main()
