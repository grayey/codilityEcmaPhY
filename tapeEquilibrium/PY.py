import sys
#Example test:   [3, 1, 2, 4, 3]
#Output: 1


#My move: Running sum() in a loop. Bad move
def solution(B):
    i = 0;
    shift = 0;
    mins = list();
    possible_splits = len(B) - 1;
    for i in range(possible_splits):
        shift = i+1;
        left = [B[0]] if i==0 else B[:shift];
        right = B[shift:];
        left_sum = sum(left);
        right_sum = sum(right);
        abs_diff = abs(left_sum - right_sum);
        mins.append(abs_diff);
        i+=1;
    return min(mins);



#Mercenary Move_1: Two passes
def solution_B(A): 
  
    #1st pass
    parts = [0] * len(A)
    parts[0] = A[0]
  
    for idx in range(1, len(A)):
        parts[idx] = A[idx] + parts[idx-1]
  
    #2nd pass
    solution = sys.maxsize
    for idx in range(0, len(parts)-1):
        solution = min(solution,abs(parts[-1] - 2 * parts[idx]));  
  
    return solution


#Mercenary Move_2: One pass
def solution_C(A):
    sumLeft = A[0]
    sumRight = sum(A[1:])
    difference = abs(sumLeft - sumRight)

    for i in range (1, len(A) - 1):
        sumLeft += A[i]
        sumRight -= A[i]
        tempDifference = abs(sumLeft - sumRight)

        if (tempDifference < difference):
            difference = tempDifference

        i = i + 1

    return difference


#Mercenary Move_3: One pass
def solution_D(A):
    P = 1
    N = len(A)
    L = sum(A[:P])
    R = sum(A[P:])
    minimal_difference = abs(L - R)
    for P in range(2, N):
        current = A[P - 1]
        L += current
        R -= current
        minimal_difference = min(minimal_difference, abs(L - R))
    return minimal_difference
    



# ex =[3, 1, 2, 4, 3, 8,9,23, 67,90,87];
# ex = [3, 1, 2, 4, 3, 8,9,23, 67,90,87, 89,74,56,29,91,46,73];
# ex = [0] * 100000; #Performance test array


# print(solution(ex)); # Test solution A
# print(solution_B(ex)); #Test solution B
# print(solution_C(ex)); #Test solution C
# print(solution_D(ex)); #Test solution D


#TEST correctness
import unittest
class TapeEquilibrium(unittest.TestCase):

    def test_solution(self):
        input1 =  [3, 1, 2, 4, 3, 8,9,23, 67,90,87];
        input2 =  [3, 1, 2, 4, 3, 8,9,23, 67,90,87, 89,74,56,29,91,46,73];
        missing1 = solution(input1);
        missing2 = solution(input2);
        self.assertEqual(missing1,57,'Should be 57');
        self.assertEqual(missing2,17,'Should be 17');

        
    def test_solution_B(self):
        input1 =  [3, 1, 2, 4, 3, 8,9,23, 67,90,87];
        input2 =  [3, 1, 2, 4, 3, 8,9,23, 67,90,87, 89,74,56,29,91,46,73];
        missing1 = solution_B(input1);
        missing2 = solution_B(input2);
        self.assertEqual(missing1,57,'Should be 57');
        self.assertEqual(missing2,17,'Should be 17');

        
    def test_solution_C(self):
        input1 =  [3, 1, 2, 4, 3, 8,9,23, 67,90,87];
        input2 =  [3, 1, 2, 4, 3, 8,9,23, 67,90,87, 89,74,56,29,91,46,73];
        missing1 = solution_C(input1);
        missing2 = solution_C(input2);
        self.assertEqual(missing1,57,'Should be 57');
        self.assertEqual(missing2,17,'Should be 17');

    def test_solution_D(self):
        input1 =  [3, 1, 2, 4, 3, 8,9,23, 67,90,87];
        input2 =  [3, 1, 2, 4, 3, 8,9,23, 67,90,87, 89,74,56,29,91,46,73];
        missing1 = solution_D(input1);
        missing2 = solution_D(input2);
        self.assertEqual(missing1,57,'Should be 57');
        self.assertEqual(missing2,17,'Should be 17');


if __name__=='__main__':
    unittest.main();