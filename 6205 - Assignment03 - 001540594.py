#01 - Combination Sum
def combinationSum(candidates, target):
    def dfs(candidates, begin, path, res, target):
        if target < 0:
            return
        if target == 0:
            res.append(path)
            return
        for index in range(begin, size):
            dfs(candidates, index, path + [candidates[index]], res, target - candidates[index])
    path = []
    res = []
    size = len(candidates)
    dfs(candidates, 0, path, res, target)
    return res


#02 - Permutations
def permute(nums):
    res = []
    path = []
    visited = []
    def backtrack(nums, path):
        if len(path) == len(nums):
            res.append(path[:])
            return
        for i in range(len(nums)):
            if nums[i] not in path:
                path.append(nums[i])
                backtrack(nums, path)
                path.pop()
    backtrack(nums, path)
    return res


#03 - Letter Combinations of a Phone Number
def letterCombinations(digits):
    if not digits: return []
    dic = ["", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    res = []
    def dfs(index, tmp):
        if index == len(digits):
            res.append(tmp)
            return
        letter = digits[index]
        letters = dic[ord(letter) - 48 - 1]
        for c in letters:
            dfs(index + 1, tmp + c)
    dfs(0, "")
    return res


#04 - Word Search
def exist(board, word):
    row = len(board)
    col = len(board[0])
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    def dfs(i, j, index):
        if board[i][j] != word[index]:
            return False
        if index == len(word) - 1:
            return True
        board[i][j] = "#"
        for x, y in dirs:
            x1 = x + i
            y1 = y + j
            if 0 <= x1 < row and 0 <= y1 < col and dfs(x1, y1, index + 1):
                return True
        board[i][j] = word[index]
    for i in range(row):
        for j in range(col):
            if dfs(i, j, 0): return True
    return False


#05 - Numbers With Same Consecutive Differences
def numsSameConsecDiff(N, K):
    result = []
    def dfs(N, K, cur_num):
        if N == 0:
            result.append(cur_num)
            return
        last_digit = cur_num % 10
        if last_digit + K < 10:
            next_num = 10 * cur_num + last_digit + K
            dfs(N - 1, K, next_num)
        if last_digit - K >= 0 and K != 0:
            next_num = 10 * cur_num + last_digit - K
            dfs(N - 1, K, next_num)
    if N == 1:
        result.append(0)
    for digit in range(1, 10):
        dfs(N - 1, K, digit)
    return result


#06 - Subsets
def subsets(nums):
    res = []
    path = []
    def backtrack(nums, index, path):
        res.append(path[:])
        for i in range(index, len(nums)):
            path.append(nums[i])
            backtrack(nums, i + 1, path)
            path.pop()
    backtrack(nums, 0, [])
    return res


#07 - Generate Parentheses
def generateParenthesis(n):
    def generate(p, left, right, parens=[]):
        if left:         generate(p + '(', left-1, right)
        if right > left: generate(p + ')', left, right-1)
        if not right:    parens += p,
        return parens
    return generate('', n, n)


#08 - All Paths From Source to Target
def allPathsSourceTarget(graph):
    n = len(graph)
    path = [0]
    ans = []
    def backtracking():
        if path[-1] == n - 1:
            ans.append(list(path))
        else:
            for nxt in graph[path[-1]]:
                path.append(nxt)
                backtracking()
                path.pop()
    backtracking()