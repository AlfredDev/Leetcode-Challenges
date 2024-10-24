class Solution {
    public String reverseVowels(String s) {
       String vowels = "aeiouAEIOU";
       char[] characters = s.toCharArray();

        int i = 0;
        int j = s.length() - 1;

        while (i < j) {
            while(i < j && vowels.indexOf(characters[i])  == -1){
                i ++;
            }
            
            while(i < j && vowels.indexOf(characters[j]) == -1){
                j--;
            }

            char aux = characters[i] ;
            characters[i] = characters[j] ;
            characters[j] = aux;

            i++;
            j--;

        }
        return new String(characters);
    }
}