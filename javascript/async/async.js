'use strict';

// 1. async
// when using Promise
function fetchUser() {
    return new Promise((resolve, reject) => {
        // get name from network request
        resolve('ellie');
    })
    
}
// when using async, which is a syntatic sugar..
async function fetchUser1() {
    // do network request
    return 'async ellie';
}


const user = fetchUser();
user.then(console.log);
console.log(user);

const user1 = fetchUser1();
user1.then(console.log);
console.log(user1);

// 2. await
// async가 붙어있는 함수 안에서만 쓸 수 있다.                                                                                                                                                                                                                                  