## 思路
- 如果用n个指针同时移动，时间复杂度为O(nk),空间复杂度为O(1)
- 如果不断 merge两个list, 时间复杂度为O(nk), 空间复杂度为O(1)

- 可以把所有的结点先保存，然后 sort, 再前后连接，时间复杂度为O(nlogn),空间复杂度为O(nk)