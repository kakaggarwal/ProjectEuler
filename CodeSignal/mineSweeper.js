function minesweeper(matrix) {
    let result = new Array(matrix.length);

    for (let i = 0; i < matrix.length; i++) {
        result[i] = new Array(matrix[i].length);

        for (let j = 0; j < matrix[i].length; j++) {
            result[i][j] =
                (matrix[i - 1]?.[j - 1] || 0) + (matrix[i - 1]?.[j] || 0) + (matrix[i - 1]?.[j + 1] || 0) +
                (matrix[i]?.[j - 1] || 0) + (matrix[i]?.[j + 1] || 0) +
                (matrix[i + 1]?.[j - 1] || 0) + (matrix[i + 1]?.[j] || 0) + (matrix[i + 1]?.[j + 1] || 0);

            console.log(matrix[i - 1]?.[j - 1] || 0, matrix[i - 1]?.[j] || 0, matrix[i - 1]?.[j + 1] || 0,
                matrix[i]?.[j - 1] || 0, matrix[i]?.[j + 1] || 0,
                matrix[i + 1]?.[j - 1] || 0, matrix[i + 1]?.[j] || 0, matrix[i + 1]?.[j + 1] || 0,
                `result: ${result[i][j]}, i: ${i}, j: ${j}`);
        }
    }

    return result;
}

minesweeper([[true, false, false], [false, true, false], [false, false, false]]);