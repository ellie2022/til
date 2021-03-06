'use strict';

// js object for async operations

// State : pending(on doing) -> fulfilled or rejected(when finished)
// Producer vs Consumer

// 1. Producer
const promise = new Promise((resolve, reject) => {
    // for doing heavy work(network, file reading)
    console.log('doing something...');  // the executor runs automatically
    setTimeout(() => {
        //resolve('ellie');
        reject(new Error('no network'));
    }, 2000);
});

// 2. Consumer
promise
    .then((value) => {
        console.log(value);
    })
    .catch(error => {
        console.log(error);
    })
    .finally(() => {
        console.log('finally');
    })

// 3. promise chaining
const fetchNumber = new Promise((resolve, reject) => {
    setTimeout(() => resolve(1), 1000);
})
fetchNumber
.then(num => num * 2)
.then(num => num * 3)
.then(num => {
    return new Promise((resolve, reject) => {
        setTimeout(() => resolve(num -1), 1000);
    });
})
.then(num => console.log(num));

// 4. Error Handling
const getHen = () => 
    new Promise((resolve, reject) => {
        setTimeout(() => resolve('🐔'), 1000);
    });
const getEgg = hen => 
    new Promise((resolve, reject) => {
        //setTimeout(() => resolve(`${hen} => 🥚`), 1000);
        setTimeout(() => reject(), 1000);
    });
const cook = egg =>
    new Promise((resolve, reject) => {
        setTimeout(() => resolve(`${egg} => 🍳`));
    });

/* getHen()
    .then(hen => getEgg(hen))
    .then(egg => cook(egg))
    .then(meal => console.log(meal));
*/
getHen()
.then(getEgg)
.catch(error => {
    return '🍞'
})
.then(cook)
.then(console.log)
.catch(console.log);

