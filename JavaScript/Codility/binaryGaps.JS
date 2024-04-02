const prompt = require("prompt-sync")()

const number = parseInt(prompt('Enter a decimal integer between 1-700: '))
const binary_number = number.toString(2)

const num_array = [...binary_number].map(Number)

let binary_gaps = [];
let count = 0;

while (num_array[0] === 0) {
    if (num_array[0] === 0) {
        num_array = num_array.shift()
    }
}

for (const num in num_array) {
    if  (num_array[num] === 1) {
        if (count !== 0) {
            binary_gaps.push(count);
        }
         count = 0;
    }
    
    if (num_array[num] === 0) {
        count += 1;
    }
}


let maxCount = -Infinity;

if (binary_gaps.length > 0) {
    binary_gaps.map((number) => {
        if (number > maxCount) {
            maxCount = number;
        }
    });
} else {
    maxCount = 0;
}

console.log(`binary: ${binary_number}\nmaximum binary gap: ${maxCount}`);


