'use strict'

const arr1 = new Array();
const arr2 = [1,2,3];

const fruits = ['apple', 'banana']
console.log(fruits);

console.log(`array length : ${fruits.length}`);
for (let fruit of fruits) {
    console.log(fruit);
}

fruits.forEach(function(fruit) {
    console.log(fruit)
});

const students = ['Mary','Tom','Brian','Simon'];
for (let student of students) {
    console.log(`from for of : ${student}`);
}

students.forEach((student, index)=>{
    console.log(index);
    console.log(student);
})

console.log (students.push('Anne','Kate'));
console.log(students);
students.pop();

console.log(students);
console.log(students.toString());

students.sort();
console.log(students);
for(let i of students) console.log(i);
console.log(students[2]);

students.splice(3, 0, 'Donna', 'Terry');
console.log(`after splice : ${students}`);

const students1 = ['K1', 'K2', 'Superman'];
const all_students = students.concat(students1);

console.log(all_students);
console.log(all_students.indexOf('Donna'));
console.log(all_students.includes('Ellie'));
all_students.push('Donna');
console.log(all_students.lastIndexOf('Donna'));
