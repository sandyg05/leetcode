## 思路

- 先复制一份数组，然后对数组进行排序
- 比较排序数组和原始数组， 记录左边不相等的位置i 和 右边不相等的位置 j
- 如果 j > i 数组长度为 j - i + 1, 否则为 0.