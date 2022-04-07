'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function(inputStdin) {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.split('\n');

    main();
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the 'plusMinus' function below.
 *
 * The function accepts INTEGER_ARRAY arr as parameter.
 */

function plusMinus(arr) {
    // Write your code here
     let pos = 0, neg = 0, zero = 0, length = arr.length
     arr.forEach( n => {
         if ( n > 0 )
             pos++
         else if( n < 0 )
             neg++
         else
             zero++
     } )
     console.log( (pos / length).toFixed(6) )
     console.log( (neg / length).toFixed(6) )
     console.log( (zero / length).toFixed(6) )
     
}

function main() {
    const n = parseInt(readLine().trim(), 10);

    const arr = readLine().replace(/\s+$/g, '').split(' ').map(arrTemp => parseInt(arrTemp, 10));

    plusMinus(arr);
}