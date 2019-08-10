通过Python操作注册表有两种方式：第一种是通过_winreg，第二种是通过win32api模块。

> 注册表基础知识：
> 
> 注册表分为根键（HKEY_*）、子键（键本身也有值）和键值项三部分。
> 
> 其中键值项由三部分组成：名称、类型（REG_*）和数据。

本来我查找的blog是这么说的，结果我一看，好嘛，全是404 Not Found，emmmmmm......（见注二）

看了看，好像是改名字了，从_winreg改成了winreg了。

所以我又屁颠屁颠地去找文档了。（见注三）

最重要的就是方法（function）了，因为注册表本来就是很简单的一个概念呀，就是用来储存设置的（应该可以这么说）：（虽然这个blog主要是给自己看的，但还是说一下：不是完全版的，请自己去看看官方文档）

1. CloseKey(hkey)
   - 关闭之前打开的key，没有它或者类似的语句的话，它也可以被python自动摧毁。
1. CreateKey(key,sub_key)
   - 创建或者打开一个key，返回handle obj。
   - > HKET_* Constants
     >
     > 为了在很多的方法（function）中使用而定义的constants。
     >
     > 包括HKEY_CLASSES_ROOT，HKEY_CURRENT_USER等书面值（constant）。
     >
   - __key__ 是一个已经打开的key或者是一个HKET_* Constants。
   - __sub_key__ 是key的名称。
   - 各种情况：sub_key可以为None（特定情况下），key已经存在了，出错情况下......
1. DeleteKey(key,sub_key)
   - 该方法不能删除带有子键的项。
1. DeleteValue(key,value)
1. EnumKey(key,index)
1. EnumValue(key,index)
   - 5和6差不多，都是用来列举注册表中的key或者value。
1. ExpandEnvironmentStrings(str)
1. QueryInfoKey(key)
   - 返回信息用的。
1. QueryValue(key, sub_key)
1. QueryValueEx(key, value_name)
1. OpenKey(key,sub_key,reserved=0,access=KEY_READ)
1. SetValue(key,sub_key,type,value)
1. SetValueEx(key, value_name, reserved, type, value)

[1] [Python操作注册表](https://www.cnblogs.com/JeffreySun/archive/2010/01/04/1639117.html)

[2] [_winreg官方文档1](http://docs.python.org/library/_winreg.html), [_winreg官方文档2](http://www.python.org/doc/2.6.2/library/_winreg.html)（现在已经无法使用了）

[3] [winreg官方文档_英文版](https://docs.python.org/3/library/winreg.html), [winreg官方文档_中文版](https://docs.python.org/zh-cn/3/library/winreg.html)

[4] [C++注册表编程](https://www.cnblogs.com/john-h/p/5886870.html)