# 初出茅庐

## 基本使用

-   直接进入 Python 环境

```python
>>> 3+3
6
>>> 3*3
9
```

-   执行 _.py_ 文件

创建一个 helloworld.py 文件

```python
#!/usr/bin/python3
print('hello world');
```

```shell
python3 helloworld.py
```

### 注释

```python
# 单行注释

'''
多行
注释
'''
OR
"""
多行
注释
"""
```

### 缩进

```python
if True:                          // True 首字母大写
    print("true");                // 注意print前的缩进大小 一般是4个空格
else
    print("false");
```

## 数据类型

[TODO:缺少 string 和其他集合]

-   Number 数字型
-   String 字符型
-   List 列表型
-   Tuple 元组
-   Sets 集合
-   Dictionary 字典

```python
a = 10
b = 2.3
c = True     #或 False
d = 3 + 4j

print(a)    #10
print(b)    #2.3
print(c)    #True
print(d)    #(3+4j)

print(type(a))    #<class 'int'>
print(type(b))    #<class 'float'>
print(type(c))    #<class 'bool'>
print(type(d))    #<class 'complex'>
```

## 变量

```python
# bad
1a = 2
.a = 3

# good
a1 = 2
a = 3
_a = 4
a_ = 5

# 多变量赋值
a = b = c = d = 2

a, b, c ,d = 1, 2, 3, "abc"

#删除变量
del a
del d

```

## 运算符

如下的运算符其他语言的大概类似

-   算数

    -   +
    -   -
    -   \*
    -   / (int 变量会隐式转换成 float),
    -   %
    -   \*\*(幂运算)
    -   // (整除)

```python
c = 2
c /= 13
print(c)    # 0.15384615384615385
type(c)     # <class 'float'>
```

-   比较运算符

    -   ==
    -   !=
    -   \> =
    -   <=
    -   <
    -   \>

-   赋值运算符

    -   =
    -   +=
    -   -=
    -   \*=
    -   /=(int 变量会隐式转换成 float),
    -   %=
    -   \*\*=
    -   //=

-   逻辑运算符

    -   and
    -   or
    -   not

-   位运算符

    -   & 按位或
    -   | 按位与
    -   ^ 按位取反
    -   ~ [todo]
    -   <<
    -   \>\>

-   成员运算符

    -   in
    -   not in

-   身份运算符 ()

    -   is
    -   not is

-   运算符优先级

    1. 括号
    1. 指数
    1. 位运算
    1. 取模取整
    1. 加减法

## 字符串

```python
a = 'abcdef'
b = 'ABCD'
c= """
多行
字符串
"""

print(a+b+c)    # 拼接字符串

str1 = "abcdef"
print(str1[:3]+ "123"+ str1[3:])    #abc123efg

print('abc%ddef' %(123))     #abc123def

print('%x', %(100))      # 64 将100 变成16进制的数字
print('%x' %(11))         #  b

print("name: %s, age:%d " %("Tom", 20))      #name: Tom, age:20
```

## 函数

-   格式

```python
def 函数名(参数...)
    函数体

函数名(参数...)   # 调用方式
```

-   范例

```python
# 普通写法
def hello(a, b)
    print("你好 %s,年龄 %d", %(a, b)

# 带有默认值的写法
def hello(a = "tom", b= 12)
    print("你好 %s,年龄 %d", %(a, b)

```

## 变量作用域

-   L(local) 局部作用域
-   E(Enclosing)闭包函数外的函数中
-   G(Global) 全局作用域
-   B(Built-in) 内建作用域

```python
x = int(32)    #内建作用域
g_a = 0          #全局作用域

def funcOut():
    o_b = 1                # 闭包函数外的函数中
    def funcIn():
        i_b = 3            # 局部作用域
```

> pass 是空函数占位符

## 模块

> 定义了一个函数变量的 **.py** 文件
>
> 关键字是 "import"
>
> dir(module_name) 例如 dir(sys) : 获取 module_name 的成员和内置成员

[TODO:引用机制]

## 条件控制语句

```python
if A==1:
    print("1")
elif A>1:
    print("2")
else:
    pass

#  嵌套
if A==1:
    if B ==2:
        print("1")
    else:
        pass
else:
    pass
```

## while 循环语句

```python
# 1~100 相加
n = 100
sum = 0
count = 1
while count <= n
    sum = sum + conter
    count += 1

print("sum%d" %(sum))

#---------------------------
counter = 0
while  counter< 3:
    print("counter",counter)
    counter +=1
else:                                    # 不满足 counter<3 的条件时候执行
    print("else counter",counter)
```

## for 循环语句

```
for a in [1,2,3,4,5,6]:
    print("a = ", a)
else:
    print("else")
```

> 关键字 break && continue

## 内置数据结构

-   List (item 可读可写可重复)

```python
list1 = ['abc',12,True, 3.14]     # 写在方括号之间，逗号隔开
list2 = ['list2']
print(list1 + list2)               # 通过  ” + “  号两个数组拼接
list[0] = 'def'                    # 修改第一个元素
list[1:3] = [123, False]           # 修改下标是1到3（不含）的元素
```

> [var1,var2,var3]

-   Tuple 不可改变的 List

> (var1,var2,var3)

```
tupleA = ('abc',12,True, 3.14)   # 使用小括号并用逗号分隔
print(tuple)
print(tuple[2])                    # 下标是2的元素
print(tuple[1,3])                 # 修改下标是1到3（不含）的元素
print(tuple * 3)                   # 输出三遍

```

-   Sets 可以理解成 item 不可重复的无序列表

> {var1,var2,var3}

```python
set1 = { "Tim", "marry","Tim"}
print(set1) # 最后的 Tim 被删除

if "Tim" in set1:
    print("在呢")
else:
    print("不在")

```

集合运算

```python
print(setA - setB)    # 差集 （setA中去除掉setA 和 setB共有的）
print(setA | setB)    # 并集
print(setA & setB)   # 交集
print(setA ^ setB)   # 并集去掉交集
```

-   Dictionary

> { key1 : var1, key2: var2, key3: var3}

```python
dict  = {}
dict ['key1'] = 1
dict [100] = 2

print(dict)
print('key1') = 1
print(dict[100])
```
