class Solution:
    def isPalindrome(self, s: str) -> bool:
        contain = []
        for i in s:
            if i.isalnum():
                contain.append(i.lower())
        pre = "".join(contain)
        post = pre[::-1]
        return pre == post
