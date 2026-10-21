class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        td_str = []

        for i in range(0,len(strs)):
            if td_str:
                str_hash = dict(Counter(strs[i]))
                for j in range(len(td_str)):
                    compair_hash = dict(Counter(td_str[j][0]))

                    if str_hash == compair_hash:
                        td_str[j].append(strs[i])
                        break
                    if j+1 == (len(td_str)):
                        td_str.append([strs[i]])
            else:
                td_str.append([strs[i]])
        
        return td_str