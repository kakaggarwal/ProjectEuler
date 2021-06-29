function circleOfNumbers(n, firstNumber) {
    const halfValue = n / 2;

    if (firstNumber >= halfValue) {
        return firstNumber - halfValue;
    } else {
        return firstNumber + halfValue;
    }
}
