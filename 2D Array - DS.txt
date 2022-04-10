'use strict';

const fs = require('fs');

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
 * Complete the 'hourglassSum' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts 2D_INTEGER_ARRAY arr as parameter.
 */

function hourglassSum(arr) {
    // Write your code here
    let highestSum = -9 * 7 - 1;
    for(let index1 = 1;index1 < arr.length - 1;index1++){
        for(let index2 = 1;index2 < arr[0].length - 1;index2++){
            let sum = 0;
            for(let indexTop=-1+index2;indexTop<2+index2;indexTop++) {
                sum += arr[index1-1][indexTop];
            }
            sum += arr[index1][index2];
            for (let indexBottom=-1+index2;indexBottom<2+index2;indexBottom++){
               sum += arr[index1+1][indexBottom]; 
            }
            highestSum = sum > highestSum ? sum : highestSum;
        }
        
    }
    return highestSum;
        

}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    let arr = Array(6);

    for (let i = 0; i < 6; i++) {
        arr[i] = readLine().replace(/\s+$/g, '').split(' ').map(arrTemp => parseInt(arrTemp, 10));
    }

    const result = hourglassSum(arr);

    ws.write(result + '\n');

    ws.end();
}
