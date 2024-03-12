class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {2:"abc",
                3:"def",
                4:"ghu",
                5:"jkl",
                6:"mno",
                7:"pqrs",
                8:"tuv",
                9:"wxyz"}
        if len(digits) ==0:
            return []
        ans = [""]
        for digi in digits:
            tmp = []
            for ch in dic[int(digi)]:
                for str in ans:
                    tmp.append(str + ch)
            ans = tmp
        return ans