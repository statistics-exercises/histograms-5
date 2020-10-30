import unittest
import scipy.stats as st
from main import *

class UnitTests(unittest.TestCase) :
    def test_function(self) : 
       for l in range(1,9) :
           mean = 0
           for i in range(100) : mean = mean + poisson( 2 )
           mean = mean  / 100 

           bar = np.sqrt(l/100)*st.norm.ppf( (0.99 + 1) / 2 )
           self.assertTrue( np.fabs( mean - 2 )<bar, "your function appears to sampling the wrong distribution" )
