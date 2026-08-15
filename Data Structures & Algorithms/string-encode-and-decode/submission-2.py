class Solution:

    def encode(self, strs: List[str]) -> str:
        coded_str = "".join(strs) + "".join([f",{len(letters)}" for letters in strs]) +f",{len(strs)}"
        return coded_str

    def decode(self, s: str) -> List[str]:
        word_list = []
        encoded_list = s.split(",")
        num_strs = encoded_list[-1] 
        initial = 0
        for i in range(int(num_strs), 0, -1):
            num_of_letters = int(encoded_list[len(encoded_list) - 1 - i])
            word_list.append(s[initial: num_of_letters + initial])
            initial = num_of_letters + initial
        return word_list
