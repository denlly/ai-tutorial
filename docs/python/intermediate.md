# 渐入佳境

## 面向对象

-   类(class)，用来描述相同属性和方法的集合。
-   类变量，又叫做静态变量，是一个不通过实例化就能够获取的变量类型
-   实例变量： 这个变量是通过类的实例化后才能够访问的变量类型
-   数据成员：类变量和实例变量用于处理类以及实例对象的相关数据
-   实例方法：
-   对象：
-   实例化：
-   方法重写（override）
    [TODO]
-   总结：

    1. 类被实例化后成为对象或者实例
    2. 类在实例化之前调用的变量和方法分别叫做类变量（静态变量）和类方法（静态方法）
    3. 类在实例化之后调用的变量和方法分别叫做实例变量和实例方法

类示例

```python
#!/usr/bin/env python
#coding=utf-8

class Student(Object)                              # 声明继承 Object
   def __init__(self, name, score):
      self.__name  = name                            # 绑定私有属性 "__"
      self.__score = score

    def print_score(self)
       print('%s:%s' %(self.name,self.score))

     def get_name(self)                               # 增加属相的访问器
        return self.__name

    def set_name(self, name)                        # [TODO]
        self.__name = name

tom = Student('Tom', 58)
mike =Student('Mike',24)
tom.print_score()
mike.print_score()


# 集成多态

class Animal(object):
    def run(self):
       print('Animal is running...')

class Dog(Animal):
    pass

class Cat(Animal):
    def run(self):
       print('Cat is running...')

animal = Animal()
animal.run()

dog = Dog()
dog.run()                 # get Animal is running... 继承的效果

cat = Cat()
cat.run()                 # get Cat is running...  多态的效果
```

## 错误异常处理

```python
import logging
try:
    pass
except Exception as e:                        #try异常时候执行
    logging.exception(e)                         # 抛出错误日志
else:                                         # 没有发生异常时候执行
    pass
finally:                                      # 不管有没有发生异常都会执行
    pass
```

## 多任务

-   操作系统可以同时执行多任务(进程)
-   多任务的解决方式大致分三种

    1. 多线程模式
    2. 多进程模式
    3. 多进程+多线程
    4. [TODO: 多协程]

### 了解操作进程

    - fork() 可以把进程复制出另一个进程，
    - 复制完成后将父进程要记录下子进程的ID，而子进程要记录父进程ID（getppid）
    - Python 的多线程支持，并不是模拟出来的线程，而是真正的Posix Thread
    - Python 通过GIL锁 实现线程之间的切换执行
    - 进程启动一个线程，启动后第一个被叫做主线程，这个线程又可以启动新的线程
    - Python 解释器设计是可以使用多线程，但是无法有效利用多核
    - 虽然不能利用多核，但是可以通过多进程实现多核任务

简单的多任务

```python
import os

print('process(%s)start.. ' % os.getpid())            # 只能在Unix 系列系统
pid = os.fork()

if pid== 0:
    print('child process ,pid : %s,ppid: %s' %(os.getpid(),os.getppid()))
else
    print('parent process, pid: %s,  child pid %s' %(os.getpid(), pid))
```

跨平台的多任务
[TODO]

```
主任务 ---------------------------------------------|
                  start         join
子任务                 |_____________|

```

## 虚拟环境的配置

-   安装多个 Python 环境
-   解决依赖库冲突
-   隔离，防止污染
-   virtualenv 和 virtualenvwrapper

virtualenv

### 安装 virtualenv

```shell
> pip install virtualenv
> mkdir python_env && cd python_env

> virtualenv -p /Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 venv36

Running virtualenv with interpreter /Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6
Using base prefix '/Library/Frameworks/Python.framework/Versions/3.6'
New python executable in /Users/denlly/Documents/python_projects/python_env/venv36/bin/python3.6
Also creating executable in /Users/denlly/Documents/python_projects/python_env/venv36/bin/python
Installing setuptools, pip, wheel...
done.

> source ./venv36/bin/activate                          #激活虚拟环境脚本
(venv36) ➜  python_env

> deactivate                                          # 退出虚拟环境
```

[TODO: virtualenvwrapper]
