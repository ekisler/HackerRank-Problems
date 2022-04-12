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
 * Complete the 'countInversions' function below.
 *
 * The function is expected to return a LONG_INTEGER.
 * The function accepts INTEGER_ARRAY arr as parameter.
 */

function countInversions(arr) {
    // Write your code here
    let count=0;
mergesort(arr)

function mergesort(myar){
if (myar.length==1) return myar;
let mid= Math.floor(myar.length/2);
const a1= mergesort(myar.slice(0,mid));
const a2= mergesort(myar.slice(mid));
return merge(a1,a2);
}

function merge(a1,a2){
let ptrA=0;
let ptrB=0;
const NewArr=[];
while ((ptrA <a1.length) && (ptrB < a2.length)){
if (a1[ptrA] <= a2[ptrB]){
NewArr.push(a1[ptrA]);
ptrA++
} else {
NewArr.push(a2[ptrB]);
ptrB++
// and here's the extra line to get the count
count=count + (a1.length-ptrA)
}}
for (let i=ptrA; i<a1.length;i++){NewArr.push(a1[i])}
for (let i=ptrB; i<a2.length;i++){NewArr.push(a2[i])}
return NewArr
}
return count;

}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const t = parseInt(readLine().trim(), 10);

    for (let tItr = 0; tItr < t; tItr++) {
        const n = parseInt(readLine().trim(), 10);

        const arr = readLine().replace(/\s+$/g, '').split(' ').map(arrTemp => parseInt(arrTemp, 10));

        const result = countInversions(arr);

        ws.write(result + '\n');
    }

    ws.end();
}