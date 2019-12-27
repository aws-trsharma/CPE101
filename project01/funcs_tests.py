import unittest
from funcs import *
class TestCases(unittest.TestCase):
 def test_poundsToKG_1(self):
      self.assertAlmostEqual(poundsToKG(0), 0.0)
 def test_poundsToKG_2(self):
      self.assertAlmostEqual(poundsToKG(10), 4.53592)
 def test_poundsToKg_3(self):
       self.assertAlmostEqual(poundsToKG(25), 11.3398)
 def test_getMassObject_1(self):
       self.assertEqual(getMassObject('t'), 0.1)
 def test_getMassObject_2(self):
       self.assertEqual(getMassObject('p'),1.0)
 def test_getMassObject_3(self):
       self.assertEqual(getMassObject('r'), 3.0)
 def test_getMassObject_4(self):
       self.assertEqual(getMassObject('g'), 5.3)
 def test_getMassObject_5(self):
       self.assertEqual(getMassObject('l'), 9.07)
 def test_getMassObject_6(self):
       self.assertAlmostEqual(getMassObject('z'),0.0)
 def test_getVelocityObject_2(self):
       self.assertAlmostEqual(getVelocityObject(10),7)
 def test_getVelocitySkater_1(self):
       self.assertAlmostEqual(getVelocitySkater(100, 0, 100), 0.0)
 def test_getVelocitySkater_2(self):
       self.assertAlmostEqual(getVelocitySkater(45.3592,5.3,15.65),1.82862572532143)    
# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

