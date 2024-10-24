class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        ##Two pointers thecnique
        characters = list(s)
        start, end = 0, len(characters) - 1
        vowels = "aeiouAEIOU"

        while start < end:
            while start < end and vowels.find(characters[start]) == -1:
                start += 1
            
            while start < end and vowels.find(characters[end]) == -1:
                end -= 1
            
            aux = characters[start]
            characters[start] = characters[end]
            characters[end] = aux

            start += 1
            end -= 1
        return "".join(characters)
 

 
s = "IceCreAm"
c = Solution()

print(c.reverseVowels(s))