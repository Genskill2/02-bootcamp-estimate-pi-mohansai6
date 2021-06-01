import math
import unittest
import random

def wallis(n):
    p=1
    for i in range(1,n+1):
        x=float(4*i*i)
        y=float(x-1)
        z=x/y
    return(2*p)
        
def monte_carlo(n):
    cp= 0
    sp= 0
    for i in range(1,n+1):
        rand_x= random.uniform(0, 1)
        rand_y= random.uniform(0, 1)
        origin_dist= rand_x**2 + rand_y**2
        if origin_dist <= 1:
            cp = cp + 1
        sp = sp + 1
        pi = 4*(cp/sp)
        return(pi)



class TestWallis(unittest.TestCase):
    def test_low_iters(self):
        for i in range(0, 5):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) > 0.15, msg=f"Estimate with just {i} iterations is {pi} which is too accurate.\n")
            
    def test_high_iters(self):
        for i in range(500, 600):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) < 0.01, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")


class TestMC(unittest.TestCase):
    def test_randomness(self):
        pi0 = monte_carlo(15000)
        pi1 = monte_carlo(15000)
        
        self.assertNotEqual(pi0, pi1, "Two different estimates for PI are exactly the same. This is almost impossible.")

        self.assertFalse(abs(pi0 - pi1) > 0.05, "Two different estimates of PI are too different. This should not happen")

    def test_accuracy(self):
        for i in range(500, 600):
            pi = monte_carlo(i)
            self.assertTrue(abs(pi - math.pi) < 0.4, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")
        
    
if __name__ == "__main__":
    unittest.main()
