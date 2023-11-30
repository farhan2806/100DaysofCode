class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result=""
        while columnNumber>0:
            val=(columnNumber-1)%26
            result = chr(65+val) + result
            columnNumber = (columnNumber-1)//26
        return result


        