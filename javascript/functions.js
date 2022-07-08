// Things to remember in functions of javascript

// member1 is a const but its member variables can be changed

const member1 = {name: 'tom', age:20, location: 'seoul'};

function changeName(obj, newName='Not defined') {
    obj.name = newName;
}

function changeAge(obj, newAge=null) {
    obj.age = newAge;
}
function changeLocation(obj, newLoc='South Korea') {
    obj.location = newLoc;
}


changeName(member1, 'jane');
changeAge(member1, 30);
changeLocation(member1, "Busan");
console.log(member1);

// (ES6) default parameter : you can set default parameter in case for no parameter input

member2 = {
    name:'April', age:20, location:'Jeju',
}

function showAge(obj, requestFrom = 'M') {
    console.log(`${obj.name}'s age is ${obj.age}. Requested from ${requestFrom}`);
}

changeLocation(member2, 'Namyangju');
showAge(member2);
showAge(member2, "Ellie");

// ES6 Rest parameters
function showAll(...args) {
    for (let i=0; i<args.length;i++) {
        console.log(`from for i loop : ${JSON.stringify(args[i])}`);
    }
    for (const arg of args) {
        console.log(`from for of loog : ${JSON.stringify(arg)}`);
    }
    //args.forEach(arg)=>console.log(arg);
}
showAll(member1, member2);

// arrow function
const printCompany = () => console.log("my company");
printCompany();

const add = (a, b) => a + b;
let result = add(5+9, 8);
console.log(result);

// iife (immideiately invoded function expression)
(function hiii() {
    console.log("hi, iife!");
})();