import math

def solution(X,Y,D):
    return math.ceil((Y-X)/D);



#TEST
import unittest
class TestFrogJump(unittest.TestCase):

    def test_solution(self):
        X = 11;
        Y = 150;
        D = 100;
        jumps =  solution(X,Y,D);
        self.assertEqual(jumps,2,'Should be 2');

if __name__=='__main__':
    unittest.main();