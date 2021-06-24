function evenDigitsOnly(n) {
    for (const num of n.toString().split('').map(m => +m)) {
        if (num % 2 !== 0) {
            return false;
        }
    }

    return true;
}


console.log(evenDigitsOnly(248622)); // true

console.log(evenDigitsOnly(642386)); // false