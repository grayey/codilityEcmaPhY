<?php


//My move 1
//Correctness:100%
//Task Score:100%
//Performance: Not assessed
function solution($N){
    $N = decbin($N); // convert to base 2
    if(!strpos($N,'0')) return 0;
        
    $max_zeros = 0;
    $string_list = explode('1',$N);
    $list_length = count($string_list);
    $N_length = strlen($N);
    
    $first = $string_list[0];
    $last = $string_list[$list_length - 1];

    if($last == '' or $N[$N_length - 1] == '0') array_pop($string_list); // remove the last element. Mutates array
    if ($first=='' or  $N[0] == '0') array_shift($string_list); // remove the first element. Mutates array

    $string_set = array_unique($string_list);
    
    foreach($string_set as $item){
        $zeros_count = count(explode('0',$item)) - 1; // occurrences of 0
        $max_zeros = $max_zeros < $zeros_count ? $zeros_count : $max_zeros;
    }
   
    return $max_zeros;
    
    }
    

print(solution(600));


