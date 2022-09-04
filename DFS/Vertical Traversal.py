# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = defaultdict(dict)
        r_min = 0
        self.c_min = float('inf')
        self.r_max = self.c_max = -float('inf')
        def dfs(node, r, c):
            if(not node): return
            self.c_min = min(self.c_min, c)
            self.r_max = max(self.r_max, r)
            self.c_max = max(self.c_max, c)
            if(r in d[c]):
                d[c][r].append(node.val)
            else:
                d[c][r] = [node.val]
            dfs(node.left, r+1, c-1)
            dfs(node.right, r+1, c+1)
            return
        dfs(root, 0, 0)
        # print(d)
        ans = []
        for i in range(self.c_min, self.c_max+1):
            temp = []
            for j in range(r_min, self.r_max+1):
                if(j in d[i]):
                    temp += sorted(d[i][j])
            ans.append(temp)
        return ans