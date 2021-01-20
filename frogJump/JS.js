function solution(X,Y,D){
  return Math.ceil((Y-X)/D);
}

let X = 11;
let Y = 150;
let D = 100;

console.log(solution(X,Y,D));