import unittest
from Tax import singleTaxCal, marriedCouple,main

class TestUM(unittest.TestCase):
    def test_single(self):
        self.assertEqual(singleTaxCal(320000,320000),7955.00)
        self.assertEqual(singleTaxCal(350000, 0), 5252.50)
        self.assertEqual(singleTaxCal(0, 350000), 5252.50)
    def test_married(self):
        self.assertEqual(marriedCouple(320000,320000),25320.0)
        self.assertEqual(marriedCouple(450000,60000),6315.00)
        self.assertEqual(marriedCouple(100,10000),0.00)
    def test_main(self):
        print("\n")
        print("-------------------------------start test main-------------------------------")
        self.assertEqual(main(450000,60000),"Choose Married Tax")
        self.assertEqual(main(350000,0),"Choose Married Tax")
        self.assertEqual(main(320000, 320000), "Choose single tax")
        self.assertEqual(main(0,0), "There are no different")

if __name__ == '__main--':
    unittest.main()