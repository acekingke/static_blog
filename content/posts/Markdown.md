title: Markdown语法
date: 2015-5-13
tags: newbie
summary: Markdown语法


 
分为三个部分

##  区块元素
###  标题

`# 这是一个一级标题`
`## 这是一个二级标题`

```ruby
require 'redcarpet'
markdown = Redcarpet.new("Hello World!")
puts markdown.to_html
```

### 段落和换行
两个空格后回车相当与插入了一个`<br />`可以试试看
### 区块引用
Markdown 标记区块引用是使用类似 email 中用 > 的引用方式。如果你还熟悉在 email 信件中的引言部分，你就知道怎么在 Markdown 文件中建立一个区块引用，那会看起来像是你自己先断好行，然后在每行的最前面加上 >：

> 这是引文1
> 很坑爹的腾讯输入法，不知道为什么不能在sublime上使用

> 也可以像这样，
在一个段落之前上使用，注意>后有空格


### 列表
无序列表：星号，加好减号，注意，要有换行。

* 星号1
* 星号2

+ 加1
+ 加2

- 减号1
- 减号2

有序列表

1. 序号1
2. 序号2

### 代码区块
和程序相关的写作或是标签语言原始码通常会有已经排版好的代码区块，通常这些区块我们并不希望它以一般段落文件的方式去排版，而是照原来的样子显示，Markdown 会用 `<pre> `和 `<code>` 标签来把代码区块包起来。

要在 Markdown 中建立代码区块很简单，只要简单地缩进 4 个空格或是 1 个制表符就可以，例如，下面的输入：

	def fun():
		pass


### 分隔线
你可以在一行中用三个以上的星号、减号、底线来建立一个分隔线，行内不能有其他东西。你也可以在星号或是减号中间插入空格。下面每种写法都可以建立分隔线：
星号分割线

* * *
减号分割线：

---
##  区段元素
### 链接
Markdown 支持两种形式的链接语法： 行内式和参考式两种形式。

不管是哪一种，链接文字都是用 [方括号] 来标记。

要建立一个行内式的链接，只要在方块括号后面紧接着圆括号并插入网址链接即可，如果你还想要加上链接的 title 文字，只要在网址后面，用双引号把 title 文字包起来即可，例如：
This is [an example](http://example.com/ "Title") inline link.

	This is [an example](http://example.com/ "Title") inline link.
	[This link](http://example.net/) has no title attribute.

### 强调
Markdown 使用星号（*）和底线（_）作为标记强调字词的符号，被 * 或 _ 包围的字词会被转成用 `<em>` 标签包围，用两个 * 或 _ 包起来的话，则会被转成 `<strong>`，例如：
```
*single asterisks*

_single underscores_

**double asterisks**

__double underscores__
```
会转成：
```

<em>single asterisks</em>

<em>single underscores</em>

<strong>double asterisks</strong>

<strong>double underscores</strong>
```

**请注意**
实时做实验

### 代码
### 图片
##  其他
### 反斜杠
### 自动链接
