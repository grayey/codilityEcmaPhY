<?php

function solution($X,$Y,$D){
  return ceil(($Y-$X)/$D);

}

$X = 11;
$Y = 150;
$D = 100;

// print(solution($X,$Y,$D));

function ab($y){
  return function($x) use($y){
    return str_repeat($y,$x);
  };
}

// $a = ab(2);
// $b = ab(3);
// echo $a(3).$b(2);



// echo '3'.(print'5')+7;

// echo "1" + 2*"007";

echo ($c="t")."r";