// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

//Example test:   [3, 1, 2, 4, 3]

function solution(A) {
    // write your code in JavaScript (Node.js 8.9.4)
    let i = 0;
    let shift = 0;
    let mins = [];

    const possible_splits = A.length - 1;
    while(i < possible_splits){
        shift = i+1;
        let left = i==0 ? [A[0]] : A.slice(0,shift);
        let right = A.slice(shift, A.length);
        let left_sum = left.reduce((a,b) => a+b, 0);
        let right_sum = right.reduce((c,d) => c+d, 0);
        let abs_diff = Math.abs(left_sum - right_sum);
        mins.push(abs_diff);
        i+=1;
        
        }
  return Math.min(...mins);
}



// Mercenary: One pass
function solution_B(A) {

  let sum=A.reduce((a,b)=> a+b, 0);
  let size=A.length;
  let temp=0;
  let arr_temp=[];
  for(let i=0; i<size-1;i++){
      if(i==0) temp=A[i];
      else  temp+=A[i];
      arr_temp[i] = Math.abs((sum - temp) - temp);
  }
  return Math.min(...arr_temp);
}


const ex =[3, 1, 2, 4, 3, 8,9,23, 67,90,87];
console.log(solution(ex));
console.log(solution_B(ex));