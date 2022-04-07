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
 * Complete the 'timeConversion' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts STRING s as parameter.
 */

function timeConversion(s) {
    // Write your code here
    let militaryTime = 0, militaryHour = 0, timeFormatPm = {}, timeFormatAm = {};
    timeFormatPm = {
        '01': 13,
        '02': 14,
        '03': 15,
        '04': 16,
        '05': 17,
        '06': 18,
        '07': 19,
        '08': 20,
        '09': 21,
        '10': 22,
        '11': 23,
        '12': 12
    }
    timeFormatAm = {
        '12': '00'
    }

    if ('PM' == s.substring(s.length - 2, s.length)) {
        militaryHour = timeFormatPm[s.substring(0, 2)];
    }
    else if ('AM' == s.substring(s.length - 2, s.length) && 12 == s.substring(0, 2)) {
        militaryHour = timeFormatAm[s.substring(0, 2)];
    } else {
        militaryHour = s.substring(0, 2);
    }
    militaryTime = (militaryHour + s.substring(2, s.length - 2));
    return militaryTime;
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const s = readLine();

    const result = timeConversion(s);

    ws.write(result + '\n');

    ws.end();
}