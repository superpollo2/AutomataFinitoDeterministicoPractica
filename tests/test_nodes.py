
import sys
sys.path.append('../src')
import unittest
from nodes import Letter, Append, Or, Kleene, Plus, Expression

class TestRegexClasses(unittest.TestCase):

    def test_letter(self):
        letter = Letter('a')
        self.assertEqual(str(letter), 'a')

    def test_append(self):
        append = Append('a', 'b')
        self.assertEqual(str(append), '(a.b)')

    def test_or(self):
        or_expression = Or('a', 'b')
        self.assertEqual(str(or_expression), '(a|b)')

    def test_kleene(self):
        kleene = Kleene('a')
        self.assertEqual(str(kleene), 'a*')

    def test_plus(self):
        plus = Plus('a')
        self.assertEqual(str(plus), 'a+')

    def test_expression(self):
        expression1 = Expression('a', 'b')
        self.assertEqual(str(expression1), 'ab')

        expression2 = Expression('a')
        self.assertEqual(str(expression2), 'a')

if __name__ == '__main__':
    unittest.main()
