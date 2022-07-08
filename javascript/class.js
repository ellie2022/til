class Person {
    constructor(name, job, age) {
        this.name = name;
        this.job = job;
        this.age = age;
    }

    get age() {
        return this.age_;
    }

    set age(val) {
        this.age_ = val < 0 ? 0 : val;
    }

    get name() {
        return this.name_;
    }

    set name(val) {
        this.name_ = val;
    }
}

const person1 = new Person('jane', 'nurse', 30);
console.log(person1.age);
console.log(person1.name);

person1.age = 20;
person1.job = 'teacher';
console.log(person1.age);
console.log(person1.job);

