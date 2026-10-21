class Solution:

    def encode(self, strs: List[str]) -> str:
        encodeStr = ""

        for element in strs:
            num = len(element)
            encodeStr = encodeStr + str(num)+"*"+str(element)
        
        return encodeStr

    def decode(self, s: str) -> List[str]:
        i = 0
        strs = []

        while i<len(s):
            delimiter_pos = s.find('*', i)
            num = int(s[i:delimiter_pos])
            i = delimiter_pos + 1
            decodeStr = s[i:i + num]
            strs.append(decodeStr)
            i += num

        return strs