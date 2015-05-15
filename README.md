# 首先安装python的虚拟环境virtualenv

如果可以使用 shell ，那么可能 Virtualenv 是你在开发环境和生产环境都想使用的 东西。

virtualenv 有什么用？如果你象我一样热爱 Python ，那么除了基于 Flask 的项目外 还会有其他项目用到 Python 。当项目越来越多时就会面对使用不同版本的 Python 的 问题，或者至少会遇到使用不同版本的 Python 库的问题。摆在你面前的是：库常常不能 向后兼容，更不幸的是任何成熟的应用都不是零依赖。如果两个项目依赖出现冲突， 怎么办？

Virtualenv 就是救星！它的基本原理是为每个项目安装一套 Python ，多套 Python 并存。但它不是真正地安装多套独立的 Python 拷贝，而是使用了一种巧妙的方法让不同 的项目处于各自独立的环境中。让我们来看看 virtualenv 是如何运行的！

如果你使用 Mac OS X 或 Linux ，那么可以使用下面两条命令中任意一条:

	$ sudo easy_install virtualenv

或更高级的:

	$ sudo pip install virtualenv

上述命令中的任意一条就可以安装好 virtualenv 。也可以使用软件包管理器，在 Ubuntu 系统中可以试试:

	$ sudo apt-get install python-virtualenv

如果你使用 Windows 且无法使用 easy_install ，那么你必须先安装它，安装方法详见 《 在 Windows 系统中使用 pip 和 distribute 》。安装好以后运行上述命令，但是要去掉 sudo 前缀。

安装完 virtualenv ，打开一个 shell ，创建自己的环境。我通常创建一个包含 venv 文件夹的项目文件夹:

	$ mkdir myproject
	$ cd myproject
	$ virtualenv venv
	New python executable in env/bin/python
	Installing setuptools............done.

现在，每次需要使用项目时，必须先激活相应的环境。在 OS X 和 Linux 系统中运行:

	$ . venv/bin/activate

Windows 用户请运行下面的命令:

	$ venv\scripts\activate

殊途同归，你现在进入你的 virtualenv （注意查看你的 shell 提示符已经改变了）。

# 安装requirement.txt
	pip install -r requirement.txt

# 运行

	python blog.py