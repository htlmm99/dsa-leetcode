class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for t in tokens:
            if t in ["+", "-", '*', "/"]:
                n1 = st.pop()
                n2 = st.pop()
                if t == "+":
                    n3 = n1+n2
                elif t == "-":
                    n3 = n2 - n1
                elif t == "*":
                    n3 = n2*n1
                elif t == "/":
                    n3 = int(n2/n1)
                st.append(n3)
            else:
                st.append(int(t))
        return st.pop()
