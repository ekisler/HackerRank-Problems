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

// Complete the freqQuery function below.
function freqQuery(queries) {
  var answer = new Array(),
        data = new Array(),
        frequency = new Array();

    for (var i = 0; i < queries.length; i++){
        var test = queries[i][0];
        if (test == 1) { // first test
            var place = data.indexOf(queries[i][1]);
            if (place == -1){
                data.push(queries[i][1]);
                frequency.push(1);
            } else {
                frequency[place]++;
            }

        } else if (test == 2) { // second test
            var place = data.indexOf(queries[i][1]);
            if ((place != -1) && (frequency[place] > 0)) {
                frequency[place]--;
            }

        } else if (test == 3) { // third test
            if (frequency.indexOf(queries[i][1]) == -1) {
                answer.push(0);
            } else {
                answer.push(1);
            }
        }
    }

    return answer;   


}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const q = parseInt(readLine().trim(), 10);

    let queries = Array(q);

    for (let i = 0; i < q; i++) {
        queries[i] = readLine().replace(/\s+$/g, '').split(' ').map(queriesTemp => parseInt(queriesTemp, 10));
    }

    const ans = freqQuery(queries);

    ws.write(ans.join('\n') + '\n');

    ws.end();
}
