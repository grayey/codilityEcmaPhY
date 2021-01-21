// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(N) {
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
