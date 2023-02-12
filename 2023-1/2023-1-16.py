class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        arr1,arr2=sentence1.split(" "),sentence2.split(" ")
        if len(arr1)<len(arr2): arr1,arr2=arr2,arr1
        diff=len(arr1)-len(arr2)
        for i in range(0,len(arr1)):
            # print(arr1[0:i]+(arr1[i+diff:]),arr2)
            if arr1[0:i]+(arr1[i+diff:])==arr2:
                return True
        return False