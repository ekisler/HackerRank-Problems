'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.replace(/\s*$/, '')
        .split('\n')
        .map(str => str.replace(/\s*$/, ''));

    main();
});

function readLine() {
    return inputString[currentLine++];
}

// Complete the minimumSwaps function below.
function minimumSwaps(arr) {
    let swapCount = 0;
    for (let index = 0; index < arr.length; index++) {
        const currentInt = arr[index];
        const position = index + 1;
        if (currentInt !== position) {
            let indexToSwap
            for (let i = 0; i < arr.length; i++) {
                if (arr[i] === position) {
                    indexToSwap =i;
                    break
                }
            }
            arr[indexToSwap] = currentInt;
            arr[index] = position;
            swapCount = swapCount = swapCount +1;
        }
    }
    return swapCount;

}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const n = parseInt(readLine(), 10);

    const arr = readLine().split(' ').map(arrTemp => parseInt(arrTemp, 10));

    const res = minimumSwaps(arr);

    ws.write(res + '\n');

    ws.end();
}
