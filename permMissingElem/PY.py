
 #My Move_1
 
 #Detected time complexity: O(N) or O(N * log(N))
 #Task Score: 100%
 #Correctness: 100%
 #Performance: 100%
 #TOTAL SCORE: 100%
def solution_A(A):
    # An arithmetic progression, namely: a, a+d, a+2d, ...
    #Nth term = a + (n-1)d; where a is first_term, d is difference, 
    A = sorted(A); #sort so it's in ascending order as all AP's should
    first_term = 1;
    difference = 1;
    last_term = 0;
    def nth_term(n):
        return first_term + (n-1)*difference;
    for idx, digit in enumerate(A):
        should_be = nth_term(idx) + 1;
        last_term = digit;
        if should_be != digit:
            return should_be;

    return last_term + 1;



#### OR ###  


#Mercenary Move_1

#Detected time complexity: O(N) or O(N * log(N))
#Task Score: 100%
#Correctness: 100%
#Performance: 100%
#TOTAL SCORE: 100%
def solution_C(A):
    N = len(A) + 1
    missing = ((N + 1) * N) / 2
    for x in A:
        missing -= x
    return round(missing);


### OR ###


#Mercenary Move_2

#Detected time complexity: O(N) or O(N * log(N))
#Task Score: 100%
#Correctness: 100%
#Performance: 100%
#TOTAL SCORE: 100%
def solution_D(A):
    should_be = len(A) # you never see N+1 in the iteration
    sum_is = 0;
    for idx in range(len(A)):
        sum_is += A[idx]
        should_be += idx+1
    return should_be - sum_is +1;


### OR ###


#My Move_2

 #Detected time complexity: O(N ** 2)
 #Task Score: 60%
 #Correctness: 100%
 #Performance: 20%
 #TOTAL SCORE: 60%
def solution_B(A):
    max_integer = max(A) if  len(A) else 0;
    for i in range(1,max_integer):
        if i not in A:
            return i;
    return max_integer+ 1;
    

## OR ###

#Solution B enhanced? 
 #Detected time complexity: O(N ** 2)
 #Task Score: 60%
 #Correctness: 100%
 #Performance: 20%
 #TOTAL SCORE: 60%
def solution_BX(A):
    '''
    Assumption:
    Internally the in-built function max() still runs a loop which drops performance as A gets larger.
    So first sort to order in ascending. Then get the last item; invariably max;
    '''
    A = sorted(A);
    try:
        max_integer = A[len(A)-1];
    except IndexError:
        max_integer = 0;
    for i in range(1,max_integer):
        if i not in A:
            return i;
    return max_integer+ 1;

    '''
    Was solution B enhanced? NO!
    Conclusion:
    The performance drop comes from starting iteration from 1. It's most efficient to loop only on the array.
    Also, I don't think that max() internally runs a loop. [TODO: check]
    '''


#BAD move: don't use. [TODO: Fix Later]
def solution_X(B):
    # An arithmetic progression, namely: a, a+d, a+2d, ...
    # Sum of all terms in a finite AP with the last term as ‘l’ = N/2(a + l)
    #but in this case N=N+1, and l = l+1

    A = sorted(B); #sorting puts them in ascending order
    length_ = len(A);
    first_term = 1;
    iterations = 0;

    try:
        last_term = A[length_ - 1];
    except IndexError:
        last_term = 0;
    def sum_all_terms(n):
        return (n/2)*(first_term+last_term+1); #
    sum_of_terms = sum_all_terms(length_);
    for digit in A:
        sum_of_terms -= digit;
        last_term = digit;
    
    terms_are_complete = iterations==length_;# means that the missing term is OUTSIDE the given list; that is, the next term in the AP
    sum_of_terms = last_term+1 if terms_are_complete else sum_of_terms;
    return round(sum_of_terms);



# X =  [1,2,3,5]


# print(solution_A(X))
# print(solution_B(X))
# print(solution_C(X))
# print(solution_D(X))
# print(solution_X(X))

#TEST correctness
import unittest
class PermMissingElem(unittest.TestCase):

    def test_solution_A(self):
        input1 =  [1,2,3,5];
        input2 =  [1,2,3,4,5];
        missing1 = solution_A(input1);
        missing2 = solution_A(input2);
        self.assertEqual(missing1,4,'Should be 4');
        self.assertEqual(missing2,6,'Should be 6');

        
    def test_solution_B(self):
        input1 =  [1,2,3,5];
        input2 =  [1,2,3,4,5];
        missing1 = solution_B(input1);
        missing2 = solution_B(input2);
        self.assertEqual(missing1,4,'Should be 4');
        self.assertEqual(missing2,6,'Should be 6');

        
    def test_solution_C(self):
        input1 =  [1,2,3,5];
        input2 =  [1,2,3,4,5];
        missing1 = solution_C(input1);
        missing2 = solution_C(input2);
        self.assertEqual(missing1,4,'Should be 4');
        self.assertEqual(missing2,6,'Should be 6');

    def test_solution_D(self):
        input1 =  [1,2,3,5];
        input2 =  [1,2,3,4,5];
        missing1 = solution_D(input1);
        missing2 = solution_D(input2);
        self.assertEqual(missing1,4,'Should be 4');
        self.assertEqual(missing2,6,'Should be 6');


if __name__=='__main__':
    unittest.main();