class Solution:
    def reverseWords(self, s: str) -> str:
        a = s.split()
        a = a[::-1]
        final = ' '.join(a).strip()
        return f'{final}'
        