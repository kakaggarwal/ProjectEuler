function findWord(words) {
    search = words.join('')

    words.forEach(word => {
        if (search.find(f => f === word[0])) {

        }
    });
}

findWord(["P>E", "E>R", "R>U"]) // PERU
findWord(["I>N", "P>A", "A>I", "S>P"]) // SPAIN