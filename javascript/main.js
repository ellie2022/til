// added in ECMAScript 5
'use strict';
    console.log("Hello World!");
    console.warn("Watch out!");
    console.error("Oops!!");
    document.write("Hello!");
    const char = 'c';
    const brendan = "brendan";
    const greeting = 'hello ' + brendan;
    console.log(`value: ${greeting}, type: ${typeof greeting}`);
    const helloBob = `hi ${brendan}! `;
    console.log(`value: ${helloBob}, type: ${typeof helloBob}`);
    console.log('value: ' + helloBob + ' type: '+ typeof helloBob);

 // operators for equality comparison   
    console.log(`looseEqualCompare '5'==5: ${looseEqualCompare()}`);
    console.log(`looseDifferCompare '5'!=5: ${looseDifferCompare()}`);
    console.log(`strictEqualCompare '5'===5: ${strictEqualCompare()}`);
    console.log(`strictDifferCompare '5'!==5: ${strictDifferCompare()}`);


        
    function looseEqualCompare() {
        return ('5'==5) ;
    }

    function looseDifferCompare() {
        return ('5'!=5);
    }

    function strictEqualCompare() {
        return ('5'===5) ;
    }

    function strictDifferCompare() {
    return ('5'!==5);
    }

  