## 思路


### DP
建立一个大小与 nums 长度相等的数组 maxLens，用于记录每个 nums 最长长度，即 maxLens[i] 表示nums 第 0 个到第 i 个元素中以 nums[i]为最大值的最长子序列长度（注意序列的最后一个值为 nums[i]）

状态转移方程:
> maxLens[i] = max(maxLens[j] if maxLens[i] > maxLens[j] ) + 1  for j = 0,1.....i-1
or maxLens[i] = 1



### SORT

在1,3,5,2,8,4,6这个例子中，当到6时，我们一共可以有四种
- 不同长度
- 且保证该升序序列在同长度升序序列中末尾最小的升序序列

"""
1
1,2
1,3,4
1,3,5,6
"""

这些序列都是未来有可能成为最长序列的候选人。这样，每来一个新的数，我们便按照以下规则更新这些序列

- 如果nums[i]比所有序列的末尾都大，或等于最大末尾，说明有一个新的不同长度序列产生，我们把最长的序列复制一个，并加上这个nums[i]。
- 如果nums[i]比所有序列的末尾都小，说明长度为1的序列可以更新了，更新为这个更小的末尾。
- 如果在中间，则更新那个末尾数字刚刚大于等于自己的那个序列，说明那个长度的序列可以更新了。

比如这时，如果再来一个9，那就是第三种情况，更新序列为
"""
1
1,2
1,3,4
1,3,5,6
1,3,5,6,9
"""

如果再来一个3，那就是第二种情况，更新序列为
"""
1
1,2
1,3,3
1,3,5,6
"""

如果再来一个0，那就是第一种情况，更新序列为
"""
0
1,2
1,3,3
1,3,5,6
"""