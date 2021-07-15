//Jack Blair 
import wixLocation from 'wix-location';
// API Reference: https://www.wix.com/velo/reference/api-overview/introduction

const censor_list = ['ASS', 'CUM', 'FAG', 'GAY', 'HUI', 'JAP', 'SEX', 'TIT', 'XXX']
let alphabet = "abcdefghijklmnopqrstuvwxyz";

/**
 *	Adds an event handler that runs when the element is clicked.
 *	 @param {$w.MouseEvent} event
 */
export function button4_click(event) { //Random Acronym Button
	let letterOne = alphabet[Math.floor(Math.random()*26)];
	let letterTwo = alphabet[Math.floor(Math.random()*26)];
	let letterThree = alphabet[Math.floor(Math.random()*26)];
	let acronym = letterOne + letterTwo + letterThree;

	while(censor_list.includes(acronym)){
		let letterOne = alphabet[Math.floor(Math.random()*26)];
		let letterTwo = alphabet[Math.floor(Math.random()*26)];
		let letterThree = alphabet[Math.floor(Math.random()*26)];
		let acronym = letterOne + letterTwo + letterThree;
	}

	let randomLink = "/threeletteracronyms/" + acronym
	wixLocation.to(randomLink);
}

/**
*	Adds an event handler that runs when the cursor is inside the
 input element and a key is pressed.
*	 @param {$w.KeyboardEvent} event
*/
export function input8_keyPress_1(event) { //Search Bar
	if (event.key === "Enter") {
        const acronym = $w("#input8").value;

        let randomLink = "/threeletteracronyms/" + acronym;

        let possible = true;
        let numbers = "0123456789";
        for(let x = 0; x < 10; x++){
            if(acronym.includes(numbers[x])){
                possible = false;
            }
        }

        if(!censor_list.includes(acronym) && acronym.length == 3 && possible){
            console.log("Going to: ", randomLink);
            wixLocation.to(randomLink);
        }
        else{
            $w("#input8").value = "";
        }
	}
}