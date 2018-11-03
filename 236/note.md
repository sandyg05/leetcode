## 思路


### 迭代
- 定义一个变量 count, 对每个根节点，搜索他的所有子节点，遇到q,p, count 就加1. 如果搜索完成之后，count 为2，说明该根节点是p,q的父节点.
- 利用postorder 遍历整棵树，找到p,q的父节点后，就停止。此时的父节点是p,q 的Lowest Common Ancestor。


### 递归
- Divide & Conquer 的思路
- 如果root为空，则返回空
- 如果root等于其中某个node，则返回root
- 如果上述两种情况都不满足，则divide，左右子树分别调用该方法
- Divide & Conquer中治这一步要考虑清楚，本题三种情况
- 如果left和right都有结果返回，说明root是最小公共祖先
- 如果只有left有返回值，说明left的返回值是最小公共祖先
- 如果只有root.right有返回值，说明root.right的返回值是最小公共祖先

作者：Jason_Yuan
链接：https://www.jianshu.com/p/118dfcb1d606
來源：简书
简书著作权归作者所有，任何形式的转载都请联系作者获得授权并注明出处。

```Python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return 
        if root == p or root == q:
            return root
        
        l = self.lowestCommonAncestor(root.left,p,q)
        r = self.lowestCommonAncestor(root.right,p,q)
        
        if l and r:
            return root
        elif l:
            return l
        else:
            return root
```