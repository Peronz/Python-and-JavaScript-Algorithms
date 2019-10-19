
letters = []

word = 'bob'

drow = ''

for(let i = 0; i < word.length; i++){
	letters.push(word[i]);
}

for(let i = 0; i<letters.length; i++){
	drow += letters.pop();
}

if (word === drow){
	return true
} else {
	return false
}

