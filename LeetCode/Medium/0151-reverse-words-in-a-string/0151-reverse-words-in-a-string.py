class Solution:
    def reverseWords(self, s: str) -> str:
        answer = ""
        s = s.split(" ")
        s.reverse()
        for i in s:
            if i != '':
                answer += i
                answer += ' '
        return answer[:-1]