title: 工作笔记
date: 2015-5-13
tags: 工作
summary: H口左转

## 中国民航信息

* 获取8张表的结果
* 评估性能测试风险

**工作成果**

* 发现bug:
在linux下执行

   ``./disql SYSDBA/SYSDBA@localhost:5438 `opt/dmdbms/bin/a.sql  ``

发现进入交互模式，a.sql并没有执行，导致./disql命令行不能执行sql文本，只能先登录，在执行sql脚本，民航用户表示非常不方便，望解决。

* 存储过程
UTL_FILE中没有UTL_FILE.INVALID_PATH异常不存在,虽然可以绕过,但是用户还是希望将这个问题解决

* 索引重建

民航从生产库抽取数据到历史库，需要重建索引。目前oracle支持rebuild online，DM7不支持。民航信息系统客户认为，不支持online，锁表而严重影响业务，
民航信息系统无论白天和黑夜均存在业务，希望支持rebuild online