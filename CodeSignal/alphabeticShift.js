function alphabeticShift(inputString) {
    let result = '';

    for (const char of inputString) {
        let charCode = char.charCodeAt(0);

        if (charCode === 122) {
            charCode = 97;
        } else {
            charCode++;
        }

        result += String.fromCharCode(charCode);
    }

    return result;
}

console.log(alphabeticShift("crazy"));