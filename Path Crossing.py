class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x = 0
        y = 0
        h = set()
        h.add((0, 0))

        for i in path:
            if i == 'N':
                y += 1
            elif i == 'S':
                y -= 1
            elif i == 'E':
                x += 1
            else:
                x -= 1
            if (x, y) in h:
                return True
            h.add((x, y))

        return False


x = Solution()
print(x.isPathCrossing('NES'))