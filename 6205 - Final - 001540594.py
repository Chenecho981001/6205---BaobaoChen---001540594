#question1
from collections import defaultdict
def question1(strs):
    dic = defaultdict(int)
    for str in strs:
        dic[sorted(str)].append(str)
    return dic.values()
#time com: On
#space com: On


#question2
def question2(grid,x,y):
    col = len(grid)
    row = len(grid[0])
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    ans = 0
    def change(x,y,grid):
        grid[x][y] = "0"
        for x, y in dirs:
            new_x = i + x
            new_y = j + y
            if grid[new_x][new_y] == "1" and new_x in [0,row] and new_y in [0,col]:
                dfs(new_x)(new_y)
    ans = 0
    for i in range(row):
        for j in range(col):
            if grid[i][j] == "1":
                ans += 1
                dfs(i,j,grid)
    return ans
#time com: O(row * col)
#space com: O(row * col)


#question3
def minRemoveToMakeValid(self, s):
    result, stack = [i for i in s], []
    for i in range(len(result)):
        if result[i] == '(':
            stack.append(i)
        elif result[i] == ')':
            if len(stack) != 0:
                stack.pop()
            else:
                result[i] = ''
    if len(stack) != 0:
        for i in stack:
            result[i] = ''
    return ''.join(result)
#time com:on
#space com:on


#question4
def Question4(grid):
    if grid[0][0] == 1:
        return 0
    else:
        m, n = len(grid), len(grid[0])
        path = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if i == 1 and j == 1:
                    path[1][1] = 1
                else:
                    if grid[i - 1][j - 1] == 0:
                        path[i][j] = path[i - 1][j] + path[i][j - 1]
        return path[-1][-1]
#time com:O(m*n)
#space: O(m*n)











