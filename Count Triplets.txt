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

// Complete the countTriplets function below.
function countTriplets(arr, r) {
    const hGram = {}
    const hGram2 = {}
    let count = 0
    
    if (arr.length < 3) return 0
    
    for (let i = arr.length - 1; i >=0; i--) {
        let t1 = arr[i]
        let t2 = t1 * r
        let t3 = t2 * r
        count += hGram2[t3] || 0
        
        hGram2[t2] ?
          hGram2[t2] += hGram[t2] || 0 :
            hGram2[t2] = hGram[t2] || 0
        
        hGram[t1] ? hGram[t1]++ : hGram[t1] = 1
    }

    return count
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const nr = readLine().replace(/\s+$/g, '').split(' ');

    const n = parseInt(nr[0], 10);

    const r = parseInt(nr[1], 10);

    const arr = readLine().replace(/\s+$/g, '').split(' ').map(arrTemp => parseInt(arrTemp, 10));

    const ans = countTriplets(arr, r);

    ws.write(ans + '\n');

    ws.end();
}
