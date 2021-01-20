<?php

// Example test:   [3, 1, 2, 4, 3]
// Output: 1 


function solution($A) {
    // write your code in JavaScript (Node.js 8.9.4)
    $i = 0;
    $shift = 0;
    $mins = [];
    $possible_splits = count($A) - 1;
    while($i < $possible_splits){
        $shift = $i+1;
        $left = $i==0 ? [$A[0]] : array_slice($A,0,$shift); // from 0 to next index
        $right = array_slice($A, $shift); //till the end of the array
        $left_sum = array_sum($left);
        $right_sum = array_sum($right);
        $abs_diff = abs($left_sum - $right_sum);
        $mins[] = $abs_diff;
        $i++;
        }
  return min($mins); // No need to spread
}


// Mercenary: One pass
function solution_B($A) {
  $sum=array_sum($A);
  $size=count($A);
  $temp=0;
  $arr_temp=array();
  for($i=0; $i<$size-1;$i++){
      if($i==0) $temp=$A[$i];
      else $temp+=$A[$i];
      $arr_temp[$i] = abs(($sum - $temp) - $temp);
  }
  return min($arr_temp);
}


$ex = [3, 1, 2, 4, 3, 8,9,23, 67,90,87];
echo solution($ex);
echo "\r\n";
echo solution_B($ex);
