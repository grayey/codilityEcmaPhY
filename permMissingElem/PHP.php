<?php

#Move 1.

 #Detected time complexity: O(N ** 2)
 #Task Score: 60%
 #Correctness: 100%
 #Performance: 20%
 #TOTAL SCORE: 60%

function solution_A($A){
    $max_integer = count($A) ?  max($A)  : 0; // 
    for($i=1; $i<$max_integer; $i++){
      if(!in_array($i,$A)) return $i;
    }
    return $max_integer + 1;
  }



#Move 2

#Detected time complexity: O(N) or O(N * log(N))
#Task Score: 100%
#Correctness: 100%
#Performance: 100%
#TOTAL SCORE: 100%

function solution_B($A){

    // An arithmetic progression, namely: a, a+d, a+2d, ...
    //Nth term = a + (n-1)d; where a is first_term, d is difference, 
      sort($A);//sort so it's in ascending order as all AP's should. Sort mutates A
     $first_term = 1;
     $difference = 1;
     $last_term = 0;
     $closure = function($n) use($first_term, $difference) {
       return $first_term + ($n-1)*$difference;
    };
     for($idx =0; $idx<count($A); $idx++){
        $should_be = $closure($idx) + 1;
        $digit = $A[$idx];
        $last_term = $digit;
        if($should_be != $digit){
          return $should_be;
        }
          
     }
 
     return $last_term + 1;
   }




#Mercenary Move_1; 

#Detected time complexity: O(N) or O(N * log(N))
#Task Score: 100%
#Correctness: 100%
#Performance: 100%
#TOTAL SCORE: 100%

function solution_C($A){
  $array_length = count($A);
    $should_be = $array_length;# you never see N+1 in the iteration
    $sum_is = 0;
    for($i=0; $i<$array_length; $i++){
      $sum_is += $A[$i];
      $should_be += $i+1;
    }
    return ($should_be - $sum_is +1);

}
  

  
$X =  [2,3,4,5,6,7,9,8,10, 11, 12, 13];

print(solution_A($X));
echo "\n";
print(solution_B($X));
echo "\n";
print(solution_C($X));