/**
 * @param {string} s
 * @return {string}
 */
var removeStars = function(s) {
    stack = []
    for(let char of s){
        if(char == '*'){
             stack.pop();
        }
        else{
            stack.push(char)
        }
            
    }
    return stack.join('');
};