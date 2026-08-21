class Solution:
    def isPalindrome(self, s: str) -> bool:
        word_list = [k.lower() for k in s if (ord(k) >= ord('0') and ord(k) <= ord('9')) or (ord(k.lower()) >= ord('a') and ord(k.lower()) <= ord('z'))]
        
        string_1 = "".join(word_list)
        string_2 = "".join(word_list[::-1])
        return string_1 == string_2
