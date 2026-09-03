class Solution:
    def convertDateToBinary(self, date: str) -> str:
        list1=date.split("-")
        list2=[]
        for item in list1:
            str2=str(bin(int(item))[2:])
            list2.append(str2)
        return "-".join(list2)