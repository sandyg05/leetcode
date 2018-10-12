## 思路
将二进制转化为10进制相加后再转化为二进制
- python中，n进制转10进制的函数  int(str,n)
- 十进制转十六进制 hex()
- 十进制转八进制  oct()

## 不用bin的思路

- 用一个变量记录carry, 用一个变量记录result, 用一个变量power记录当前数字结果所在位置
- 在超过较短数之前, 当前的结果为 a,b 数中当前位置数相加再加上carry
- 超过较短数之后, 当前的结果为较长数中当前位置数加上carry

- **最高位还要加上 carry**