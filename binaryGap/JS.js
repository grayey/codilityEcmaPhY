
//My move 1
//Correctness:100%
//Task Score:100%
//Performance: Not assessed

function solution(N){

    N = N.toString(2); // convert to base 2
    if(!N.includes('0')) return 0;
        
    let max_zeros = 0;
    let string_list = N.split('1');

    const list_length = string_list.length;
    
    const first = string_list[0];
    const last = string_list[list_length - 1];

    if(last == '' || N.endsWith('0')) string_list.pop(); // remove the last element. Mutates array
    if (first=='' || N.startsWith('0')) string_list.shift(); // remove the first element. Mutates array
            
    const string_set = new Set(string_list);
    for(const item of string_set){
        zeros_count = item.split('0').length - 1; // occurrences of 0
        max_zeros = max_zeros < zeros_count ? zeros_count : max_zeros;
    }
        
    return max_zeros;

}


//mercenary move 1
//Correctness:100%
//Task Score:100%
//Performance: Not assessed

function solution_A(N) {
    // write your code in JavaScript (Node.js 8.9.4)
    let gap = 0;
    let curgap = 0;
    let string_ = N.toString(2);
    let endIndex = string_.length-1;
    for (endIndex; endIndex >= 0; endIndex--) {
        if (string_.charAt(endIndex) != '0') {
            break;
        }
    }
    for (let i = endIndex - 1; i >= 0; i--) {
        if (string_.charAt(i) == '0') {
            curgap = curgap+1;
        } else {
            if (curgap > gap) {
                gap = curgap;
            }
            curgap = 0;
        }
    }
    return gap;
}



console.log(solution(600))
console.log(solution_A(600))
