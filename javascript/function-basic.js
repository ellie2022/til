'use strict';

function doSomething(job, param1, param2) {
    console.log(job);
    const result = job(param1, param2);
    console.log(result);
}

function add(a, b) {
    return a + b;
}

function subtract(a, b) {
    return a - b;
}

doSomething(add, 3, 4);
doSomething(subtract, 3, 5);