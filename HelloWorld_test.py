import unittest
from HelloWorld import HelloWorld

class MyTestCase(unittest.TestCase):
    def test_default_greeting_set(self):
        hw = HelloWorld()
        self.assertEqual(hw.message, 'Hello world!')

    def test_isgt_lt(self):
        hw = HelloWorld()
        self.assertFalse(hw.isgt(3, 4))

    def test_isgt_gt(self):
        hw = HelloWorld()
        self.assertTrue(hw.isgt(4, 3))

    def test_isgt_notnumber(self):
        hw = HelloWorld()
        self.assertRaises(ValueError, hw.isgt, "4", "5")



    # def test_demo(self):
    #    self.fail()

if __name__ == '__main__':
    unittest.main()