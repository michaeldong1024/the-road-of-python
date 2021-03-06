## 学习方法

```
3w1h：what | why | where | how
```



## 什么是计算机语言
* [编程语言](https://zh.wikipedia.org/wiki/%E7%BC%96%E7%A8%8B%E8%AF%AD%E8%A8%80)   
* [编程](https://zh.wikipedia.org/wiki/%E7%A8%8B%E5%BA%8F%E8%AE%BE%E8%AE%A1)


## 计算机语言的发展
### 发展
```
机器语言(01代码指令)---> 汇编语言(助记词 MOV CMP CF)---> 高级语言(java 、C、python)
```
* [机器语言](https://zh.wikipedia.org/wiki/%E6%9C%BA%E5%99%A8%E8%AF%AD%E8%A8%80)
* [汇编语言](https://zh.wikipedia.org/wiki/%E6%B1%87%E7%BC%96%E8%AF%AD%E8%A8%80)
* [高级语言](https://zh.wikipedia.org/wiki/%E9%AB%98%E7%BA%A7%E8%AF%AD%E8%A8%80)
### 对比
``` 
1.机器语言，与机器直接交互，执行效率最高
2.汇编语言，执行效率较高，没有机器语言效率高，开发效率比机器语言高
3.高级语言，执行效率最低，开发效率最高 （重点）
```



## 高级语言的执行方式

```
1.编译型：类似于百度翻译，执行效率高
2.解释型：类似于同声传译，开发效率高 （python: 后出现的能使用前出现的(资源)，反过来不行）
```
[编译型语言与解释型语言的区别](https://blog.csdn.net/zhu_xun/article/details/16921413)

# Python
[什么是python?](https://zh.wikipedia.org/wiki/Python)
## python交互方式

```
1.实时交互：提前进入python解释器环境
2.文件交互：将文件交给python解释器执行（效率高）
python文件以.py结尾
```
## 变量

```
1. what: 可变的 状态(量是用来描述事物的某种状态)
2. why: 如何用代码来描述事物的某种（可变化的）状态
3. where: ...
4. how：
	- 如何定义变量： 变量名 = 变量值
		-- name = 'Owen'
		-- 在堆区开辟空间存放变量值，在栈区开辟名为变量名的空间存放堆区变量值那个区域的地址
		-- name = 'Egon'
		-- 重新赋值，重新开辟空间存放变量值，跟原本的变量名进行绑定，原来变量名name的值就为Egon
	- 如何使用变量： 变量名
		-- 没有被变量名绑定的变量值就会被系统回收
```



## 变量三要素

```python
1. 变量值：变量名

2. 变量地址：id(变量名)

3. 变量的类型：type(变量名)

注：新建值，系统就会开辟空间存放该值，但存在python的优化机制，当变量值简单时，python会沿用之前的变量值
n1 = 'Owen chen'
n2 = 'Owen chen'
正常情况(一个值开辟一个空间存放)：id(n1) != id(n2)

n1 = 'Owen'
n2 = 'Owen'
优化情况(沿用之前空间值)：id(n1) == id(n2) （了解）

思考
n1 = n2 = 'Owen chen' <=> n1 = 'Owen chen'  n2 = n1
id(n1) == id(n2)
```

## 变量（标识符）命名规范（重点）

```python
1. 可以由数字、字母、下划线组合
2. 不能以数字开头
3. 不能与系统关键字保留字重名
4. 见名知意，建议使用_连接语法（驼峰 owenName OwenName | _连接  owen_name），一般_开头或结尾都有特殊含义
```



## 交互输入

```python
变量名 = input("文本提示")

注：回车后，系统在控制台等待用户输入具体的 变量值
```



## 格式化输出

```python
# 需要从键盘上录入三个变量值
name = input('请输入姓名：')
gender = input("请输入性别：")
age = input("""请输入年龄：""")
# 按照指定的多行文本格式输出
print("""------- name: %s -------
name：%s
gender：%s
age：%s
---------- end ----------""" % (name, name, gender, age))
# 了解：
# %s本质上是为字符串站位，但是可以为所以类型数据进行站位
# %d是数字类型占位符，只能给数字数据站位，否则报错
```

## 数据类型

```python
int
float
str
bool
list
dict
```



## 运算符

```python
1. + - * / % ** //
2. > < >= <= == !=   连比操作
3. and or not  短路现象
```











