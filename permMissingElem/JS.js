//Detected time complexity: O(N) or O(N * log(N))
  //Task Score: 100%
  //Correctness: 100%
  //Performance: 100%
  //TOTAL SCORE: 100%
  function solution_A(A){

    // An arithmetic progression, namely: a, a+d, a+2d, ...
    //Nth term = a + (n-1)d; where a is first_term, d is difference, 
     A = A.sort((a,b)=> a - b);//sort so it's in ascending order as all AP's should
     let first_term = 1;
     let difference = 1;
     let last_term = 0;
     const nth_term = (n) => first_term + (n-1)*difference;
     for(let idx =0; idx<A.length; idx++){
       let should_be = nth_term(idx) + 1;
       let digit = A[idx];
       last_term = digit;
       if(should_be != digit){
         return should_be;
       }
          
     }
 
     return last_term + 1;
   }
  
   

// OR //

   

 //Detected time complexity: O(N ** 2)
 //Task Score: 60%
 //Correctness: 100%
 //Performance: 20%
 //TOTAL SCORE: 60%
function solution(A){
  
  let max_integer = A.length ? Math.max(...A) : 0;
    for(let i=1; i<(max_integer+1); i++){
      if(!A.includes(i)){
        return i;
      }
    }
    return max_integer+ 1;
  }

  


  
const X =  []

console.log(solution(X));
console.log(solution_A(X));