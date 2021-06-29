function chessBoardCellColor(cell1, cell2) {
    const dist = (cell2.charCodeAt(0) - cell1.charCodeAt(0)) + (cell2[1] - cell1[1]);

    if (dist % 2 === 0) {
        return true;
    }

    return false;
}

console.log(chessBoardCellColor("A1", "C3")); // true
console.log(chessBoardCellColor("A1", "H3")); // false
console.log(chessBoardCellColor("A1", "A2")); // false
console.log(chessBoardCellColor("A1", "B1")); // false
console.log(chessBoardCellColor("H1", "C8")); // true
console.log(chessBoardCellColor("A1", "B4")); // true
