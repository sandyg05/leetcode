## 用2个Stack，复杂度O(N)

链表方案最大的开销在于暴力搜索最大值需要遍历整个链表。优化的一个方向就是看能不能不遍历整个链表就找到最大值。一个可行的办法就是利用一个额外的Stack，专门记录当前最大值。还是考虑数组[2, 1, 9, 3, 5]， 在numStack每插入一个新元素，就在maxStack插入当前最大值，

```
num stack = [2, 1, 9, 3, 5]
max stack = [2, 2, 9, 9, 9]  <- 每次插入新元素都记录当前全局最大值
```

这样做的好处是，当我知道了当前最大值为9，我只需要移除找到第一个9即可，不需要再遍历余下的数字。


```
        已知当前最大值为"9"，只需要移除第一个"9"。余下的数字可以不用遍历。
                   |
num stack = [2, 1, 9        弹出元素 -> 3, 5]
max stack = [2, 2, 9
```
移除9之后，只需要把之前弹出元素[3,5]重新压入栈，同时更新maxStack即可，

```
num stack = [2, 1, 3, 5]
max stack = [2, 2, 3, 5]
                      |
                当前最大值为'5'
```