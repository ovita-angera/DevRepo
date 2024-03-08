/*
There are four decision constructs in JS
- simple if statement
- if - else statement
- if - else -if 
- switch
*/

// simple if
var number = 5;

if (number < 10) {
    console.log('Accelerate, speed below average')
}

// if - else

if (number < 10) {
    console.log('Accelerate, speed below average')
} else {
    console.log('do not fret, godspeed')
}

//if - else -if
if (number < 5) {
    console.log('Wake up moonchild');
} else if (number == 5) {
    console.log('There, there ... be like water');
} else {
    console.log('Thinking fast and slow')
}

// switch statement
let fruit