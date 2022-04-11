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
 * Complete the 'twoStrings' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts following parameters:
 *  1. STRING s1
 *  2. STRING s2
 */

function twoStrings(s1, s2) {
    // Write your code here
    let result = "NO";
    const s1len = s1.length;
    const s2len = s2.length;
    
    if (s1len >= 1
        && s1len <= 100000
        && s2len >= 1
        && s2len <= 100000) {
            
            result = (s1.split('')
                    .filter((e1, key) => s2.indexOf(e1) > -1)
                    .length > 0) ? "YES" : "NO";
                
        }
        return result;
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const q = parseInt(readLine().trim(), 10);

    for (let qItr = 0; qItr < q; qItr++) {
        const s1 = readLine();

        const s2 = readLine();

        const result = twoStrings(s1, s2);

        ws.write(result + '\n');
    }

    ws.end();
}
