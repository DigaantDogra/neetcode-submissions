class Solution:

    def encode(self, strs: List[str]) -> str:
        code = ""
        for i in strs:
            for st in i:
                temp = ""
                temp = str(ord(st)) + "*"
                code += temp
            code += "/"
        return code

    def decode(self, s: str) -> List[str]:
        number_st = ""
        strs = []
        st = ""
        for i in s:
            if i == "*":
                number_st = chr(int(number_st))
                st += number_st
                number_st = ""
            elif i == "/":
                strs.append(st)
                st = ""
            else:
                number_st += i
        
        return strs
            