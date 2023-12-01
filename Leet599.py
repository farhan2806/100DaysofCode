class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        a=0
        n=float('inf')
        final=[]
        dic=dict()
        for i in list1:
            dic[i]=list1.index(i)
        
        for j,res in enumerate(list2):
            if res in dic:
                a=j+dic[res] 
                if a<n:
                    n=a
                    final=[res]
                elif a==n:
                    final.append(res)
        return final
        