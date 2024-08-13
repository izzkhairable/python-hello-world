import unittest
import warnings
from ..hello_world.hello_world import hello_world

class TestHelloWorld(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', category=ResourceWarning)

    def test_hello_world(self):
        styled_hw, plain_hw ,random_quote, random_sentence = hello_world()
        expected_plain_hw = "Here is the plain:\nHello World\n"
        self.assertEqual(plain_hw, expected_plain_hw)
        self.assertEqual(len(styled_hw), 348)
        self.assertRegex(random_quote, r"Here's a random quote:\n*")
        self.assertRegex(random_sentence, r"Here's a random sentence:\n*")


if __name__ == '__main__':
    unittest.main()
