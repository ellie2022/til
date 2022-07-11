//q1
const fruits = ['apple', 'banana', 'orange'];
const fruitstr = fruits.toString(); //my work
console.log(fruitstr);
const result1 = fruits.join(', ')  // suggested
console.log(result1);

//q2
const fruits1 = 'apple, melon, banana, cherry';
const fruits2 = new Array();
fruits2.push('apple');
fruits2.push('melon');
fruits2.push('banana');
fruits2.push('cherry');
console.log(fruits2);
//suggested
const result2 = fruits1.split(',');
console.log(result2);


//q3
const array=[1,2,3,4,5];
array.sort((a,b)=>b-a);
console.log(array);
array.sort((a,b)=>a-b);
console.log(array);
// suggested
const result3 = array.reverse();
console.log(result3);
console.log(array);


//q4
const array1=[1,2,3,4,5];
//array1.splice(0,2);
console.log(array1);
//suggested
const result4 = array1.slice(2);
console.log(result4);

class Student {
    constructor (name, age, enrolled, score) {
        this.name = name;
        this.age = age;
        this.enrolled = enrolled;
        this.score = score;
    }
}
const students = [
    new Student('A', 29, true, 45),
    new Student('B', 28, false, 80),
    new Student('C', 30, true, 90),
    new Student('D', 40, false, 66),
    new Student('E', 18, true, 88),
    
]
//q5 
let rightStudent = new Student(null,null,null,null);
for (let student of students) {
    if (student.score === 90) {
        rightStudent = student;
        break;
    }
}
console.log(rightStudent);
// suggested
const result5 = students.find((student) => student.score === 90);
console.log(result5);


// q6
const enrolled = new Array();
for (let student of students) {
    if (student.enrolled) {
        enrolled.push(student);
        console.log(student);
    }
}
console.log(enrolled.length);
for(let i of enrolled) {
    console.log(i);
}
// suggested
const result6 = students.filter((student)=>student.enrolled);
console.log(result6);

//q7
let scores = new Array();
for (let student of students) {
    scores.push(student.score);
}
console.log(scores);
//suggested
const result7 = students.map((student)=>student.score);
console.log(result7);

//q8 
let under50 = false;
for(let student of students) {
    if (student.score < 50) {
        under50 = true;
        break;
    }
}
console.clear();
console.log(under50);
//suggested
const result8 = students.some((student) => student.score<50);
console.log(result8);

// q9
let total = 0;
for (let student of students) {
    total += student.score;
}
const average = total/students.length;
console.log(average);
//suggested
const result9 = students.reduce((prev, curr) => prev + curr.score, 0);
console.log(result9/students.length);

//q10
let scorestr='';
for (let student of students) {
    scorestr += student.score + '\, ';
}
console.log(scorestr);
console.clear();
//suggested
const result10 = students
    .map((student) => student.score)
    .filter((score) => score >= 50)
    .join();
    console.log(result10);

//qb
let scores1 = new Array();
for (let student of students) {
    scores1.push(student.score);

}
scores1.sort((a,b)=>a-b);
console.log(scores1);