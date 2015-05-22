title: hy语言
date: 2015-5-21
tags: [hy python]
summary: hy language

# 为什么用hy语言

说句实在话，我对lisp语言感兴趣，主要还是我自己的项目中用C语言实现的xml格式的正则式工具。
虽然用xml基本上满足正则式的表达，但是我仍然不满意，因为具体的动作还得用C语言实现，xml仅仅
作为数据表达，而不能进行动作。

然而，lisp类语言进入我的眼帘，虽然之前也玩过一阵子lisp，但是觉得这种语言除了繁琐之外还是繁琐，
没有发现有任何优势存在。说句实话，将传统的语言翻译成lisp，只会更繁琐，没有优势。

知道近来出现的clojure语言，给lisp带来了新机，clojure是基于java的，你完全可以用java写某些类库，方法。
然后用clojure去调用它。java中经常使用xml配置，来实现扩展。但是用clojure代替xml更简洁！而且clojure本身
就是一种可以运行的语言，除了表达之外，还有意向不到的功能。

有人说javascript本身就是一种lisp，这个我认同。javascript的函数参数的任何一个地方，都可以定义一个函数。
你经常看到
	
	（function(){
		xxxx
	})()

之类的匿名函数，这本身就是lisp的一个思路：
	
	(+ 1 2)
这是一个简单的1 + 2 ,你完全可以将1替换一个新的表达式 (* 2 3)
	
	(+ (* 2 3) 2)

是否有点感觉？你看看javascript语法：

	function add (a ,b) {return a+b;}
我们可以这样写

	add ((function(m, n){return m*n;})(2,3), 2);
或者

	(function(a,b ){return a+b;})(
	(function(m, n){return m*n;})(2,3),2);

是不是看到lisp语言场出现一堆圆括号？

javscript也好，clojure语言也好，与传统的lisp相比，并没有排斥过程语言，因为很多情况下，使用过程语言更简洁。
而传统lisp经常死掉后有重生，个人觉得，主要还是全盘使用lisp，不是一个好方法。javascript可以认为是C与lisp双
特性的语言。clojure则是lisp与java双特性


很好，java有了clojure，python也出现了类似clojure的东西，就是hy，就是lisp与python双特性。

# 示例

假设我们要给一家宠物店做app，用来计算每个客户购买货物的总价

第一个版本:

	(defn total [price amount] 
	 (* price amount))

于是给给客户第一个版本：可以如此使用 

	(total 12.0 2)

但是客户很不满意，设定为Dog 为12.0 元Cat为 10元，希望不去记忆单价，直接提供 (buy 动物名 个数)返回总价

于是我们记下了规则，但是程序员不太喜欢改他的total函数，因为大部分的程序员很懒。
于是我们就有了第二版

	(defn price_list [name] (get 
			{"Dog" 12.0 "Cat" 10.0 "Teddy" 30} 
		name))

	(defn buy [name amount]
	(total 
		(price_list name)
		amount) )
这样使用:

	(buy "Dog" 2)
或者
	
	(apply 
	(fn [name amount]
		(total (price_list name)
			amount))
			["Dog" 2]) 
 

这个过程,不是像原来的方式那样去修改total函数的代码,显然代码重用够可以。

显然,五月一日到来,客户突然说要打折促销, 打折方法，是超过100元打9折
于是就有第三个版本

	(defn discount [t]
		(if (> t 100) 
			(* 0.9 t)	
			t))

	(discount (buy "Dog" 12) )

或者不习惯这写法, 可以

	(-> (buy "Dog" 12 ) discount)

有一天，客户收到一张订货单，上面有Dog 3只，Cat 2只， 客户希望我们提供一个版本，能计算
货单总价

	(def order_list {"Dog" 3 "Cat" 2})

	(defn order [o_list]
		(setv sum 0)
		(for [(, i j) (dict.items o_list)]
			(setv sum (+ sum (buy i j))))
		sum )

你会发现，这个代码还不如用python来得快，而且非常费解，这个就是lisp的弱势，此时，您大可以用python，我本人不太赞成单纯用lisp
因为有很多情况下，过程型的东西会更好

假设我们把上面代码写入到一个文件中，buy_pet.hy
内容如下：

	(defn total [price amount] 
	 (* price amount))

	(defn price_list [name] (get 
			{"Dog" 12.0 "Cat" 10.0 "Teddy" 30} 
		name))

	(defn buy [name amount]
	(total 
		(price_list name)
		amount) )

	(defn discount [t]
		(if (> t 100) 
			(* 0.9 t)	
			t))

	(def order_list {"Dog" 3 "Cat" 2})

	
新建文件work.py

	import hy
	from buy_pet import *
	def order(order_list):
		sum = 0
		for (i, j) in dict.items(order_list):
			sum+=buy(i, j)
		return sum
	if __name__ == '__main__':
		print order(order_list)

使用方法
在hy

	(import [work [*]])
	(order order_list)
在python中
首先 `import hy`, 然后import所需要的hy模块，然后直接调用即可

# 总结

lisp语言其实是一种思路,有点类似编译器的设计方法,首先,你的找到最小的不可变的语义。某种语言的编译器,首先要找到最小的词,这些词就是最小的不可变的
单位。编译器处理的程序就是由这些词组成。解析这些词的组合，就能实现复杂的功能。lisp设计时候，也需要找到最小的不可分的操作，我们姑且称为原子动作，然后复杂的功能由这些动作组成。

比如，宠物店的原子动作就是计价。需求变化后，仍然要考虑那些是可分不变的。然后复杂的功能则由这些基本功能组合而成，这也是lisp擅长的东西。而采用直接在机架函数修改来实现需求变化，不是一个好办法。

比如，突然有一个小孩来到宠物店，他说我要买像老虎的宠物。实际上只需要

	(defun pet_like_tiger []
		"Cat")

	(buy (pet_like_tiger) 2)

看起来像不像自然语言? 像是在说，买像老虎的宠物两只。
