title: Python技巧
date: 2015-5-13
tags: [python, 设计模式]
summary: 研究flask的成果

# 工厂方法

## Python的getattr(),setattr(),delattr(),hasattr()

在python文档中有这么一句话:

> getattr(x, 'foobar') is equivalent to x.foobar

因此,可以十分容易的采用getattr函数获取工厂方法

	class draw():
		def draw_circle(self):
			print 'now draw the cirle'
		def draw_rect(self):
			print 'now draw the rectangle'
		def act(self,shape):
			fun = getattr(self, "draw_%s" % shape)
			return fun

	dra = draw()
	dra.act("rect")()
	
# 判断版本

	py = sys.version_info
	py3k = py >= (3, 0, 0)
	py25 = py <  (2, 6, 0)
	py31 = (3, 1, 0) <= py < (3, 2, 0)