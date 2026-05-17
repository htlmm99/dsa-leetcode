class Solution:
    def isValid(self, s: str) -> bool:
        st = list()
        mapping = {
            "{": "}",
            "(": ")",
            "[": "]"
        }
        for i in s:
            if i in mapping:
                st.append(i)
            else:
                if st and i == mapping.get(st[-1]):
                    st.pop()
                else:
                    return False 
        
        return len(st) == 0
