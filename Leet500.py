class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        row1="qwertyuiopQWERTYUIOP"
        row2="asdfghjklASDFGHJKL"
        row3="zxcvbnmZXCVBNM"
        l=[]

        for i in range(len(words)):
            in1=0
            in2=0
            in3=0
            for j in range(len(words[i])):
                if words[i][j] in row1:
                    in1=in1+1
                elif words[i][j] in row2:
                    in2=in2+1
                elif words[i][j] in row3:
                    in3=in3+1

            if in1==len(words[i]) or in2==len(words[i]) or in3==len(words[i]):
                l.append(words[i])
        return l