// 1. object to json
// stringify(obj)
let json = JSON.stringify(true);
console.log(json);

json = JSON.stringify(['apple', 'banan']);
console.log(json);

const rabbit = {
    name:   'tori',
    color:  'white',
    size:   null,
    birthDate:  new Date(),
    jump: () => {
        console.log(`${this.name} can jump!`);
    },
    weight: 10,
}
rabbit.birthDate = '2022-01-01 10:05:25';
console.log(rabbit);

json = JSON.stringify(rabbit, ["name", "color"]);
console.log(json);

json = JSON.stringify(rabbit, (key, value) => {
    console.log(`key: ${key}, value: ${value}`);
    return key === 'name' ? 'melani' : value;
});
console.log(json);

// 2. json to object
// parse(json)
//console.clear();
json = JSON.stringify(rabbit);
let obj = JSON.parse(json);
console.log(obj);

obj = JSON.parse(json, (key, value) => {
    console.log(`key: ${key}, value: ${value}`);
    return key === 'birthDate' ? new Date(value) : value;
})
rabbit.jump();
//obj.jump();

console.log(rabbit.birthDate);
console.log(obj.birthDate);