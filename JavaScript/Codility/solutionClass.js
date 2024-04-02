// define a class to solve the binary gap problem 
class BinaryGap {
    constructor (entry) {
        this.entry = entry 
        this.number_array = [];
        this.binary_gaps = [];
        this.count = 0;
    }

    convert_to_binary = () => {
        this.entry = this.entry.toString(2);
    }

    convert_to_array = () => {
        this.number_array = [...this.entry].map(Number)
    }

    find_binary_gap = () => {
        while (this.number_array[0] === 0) {
            if (this.number_array[0] === 0) {
                this.number_array = this.number_array.shift()
            }
        }

        for (const num in this.number_array) {
            if  (this.number_array[num] === 1) {
                if (this.count !== 0) {
                    this.binary_gaps.push(this.count);
                }
                this.count = 0;
            }
            
            if (this.number_array[num] === 0) {
                this.count += 1;
            }
        }
        
        let maxCount = -Infinity;
        
        if (this.binary_gaps.length > 0) {
            this.binary_gaps.map((number) => {
                if (number > maxCount) {
                    maxCount = number;
                }
            });
        } else {
            maxCount = 0;
        }

        return `maximum binary gap: ${maxCount}`;
    }
}

// declare an instance of the class with a number
const prompt = require("prompt-sync")()
const input = parseInt(prompt('Enter a decimal integer between 1-700: '))

const testInstance = BinaryGap(input)

testInstance.convert_to_binary()
