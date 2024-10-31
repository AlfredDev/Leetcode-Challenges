function removeStars(s: string): string {
    const stack: string[] = [];

    for (let char of s) {
        if(char === '*'){
            stack.pop();
        }
        else{
            stack.push(char);
        }
    }

    return stack.join('');

};

