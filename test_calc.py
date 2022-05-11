import unittest                         # import unit_testing
from unit_testing import Calc           # file to do unit testing on
from unit_testing import Employee


class TestUnitTesting(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print('setupClass')

    @classmethod
    def tearDownClass(cls) -> None:
        print('teardownClass')

    def setUp(self):    # set base parameters so it is not needed to create everytime new
        print('setUp')
        self.emp_1 = Employee('Corey', 'Schafer', 50000)
        self.emp_2 = Employee('Sue', 'Smith', 60000)

    def tearDown(self):
        print('tearDown')
        pass

    def test_add(self):                     # name has to start with test_ -> if not it is not running the test
        self.assertEqual(Calc.add(10, 5), 15)
        self.assertEqual(Calc.add(-1, 1), 0)
        self.assertEqual(Calc.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(Calc.subtract(10, 5), 5)
        self.assertEqual(Calc.subtract(-1, 1), -2)
        self.assertEqual(Calc.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(Calc.multiply(10, 5), 50)
        self.assertEqual(Calc.multiply(-1, 1), -1)
        self.assertEqual(Calc.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(Calc.divide(10, 5), 2)
        self.assertEqual(Calc.divide(-1, 1), -1)
        self.assertEqual(Calc.divide(-1, -1), 1)
        self.assertEqual(Calc.divide(5, 2), 2.5)

        with self.assertRaises(ValueError):   # check if ValueError is raised if dividing by 0
            Calc.divide(10, 0)

    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp_1.email, 'Corey.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Sue.Smith@email.com')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.email, 'John.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Jane.Smith@email.com')

    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.emp_1.full_name, 'Corey Schafer')
        self.assertEqual(self.emp_2.full_name, 'Sue Smith')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.full_name, 'John Schafer')
        self.assertEqual(self.emp_2.full_name, 'Jane Smith')
    
    def test_apply_raise(self):
        print('test_raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()
        
        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)


if __name__ == '__main__':
    unittest.main()
