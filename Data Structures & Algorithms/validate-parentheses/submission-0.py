class Solution:
    def isValid(self, s: str) -> bool:
        parts = {")": "(", "}":"{", "]":"["}
        stack = []

        for ch in s:
            if ch in parts.values():
                stack.append(ch)
            elif ch in parts:
                if not stack or stack[-1] != parts[ch]:
                    return False
                stack.pop()
        return not stack