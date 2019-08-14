LaTeX学习手记02
=======================================
正文
---------------------------------------
#### 弧的path结构
一个例子：
``` tex
arc[start angle = 10, end angle = 80, radius = 10pt]
```

注意：弧path 前的path末点是圆弧的起点，而非圆点（与之相对的是圆path ，它对应的是圆点），可能这样就能构造出一个完整的path 了吧。

跟圆一样，它也有相应的椭圆形式：
``` tex
    \tikz \draw (0,0)
        arc [start angle =  0, end angle = 315
             x radius = 1.75cm, y radius = 1cm]；
```

#### 缩放
在begin 的后面可以使用形如
``` tex
    [scale = 3]
```

来缩放整个tikzpicture。

#### clip（裁剪）
clip 的语法形式很类似draw。

比如说我想只看tikzpicture 中的(-0.1 , -0.2) rectangle (1.1 , 0.75)中的部分（因为这才是我真正感兴趣的东西）。
``` tex
    \clip (-0.1 , -0.2) rectangle (1.1 , 0.75)；
```

同理，clip也可以一边画一边裁剪：
``` tex
    \clip[draw] (0.5 ， 0.5) circle (0.6cm)；
```

实现机制是这样子的：

tikz中最基本的命令就是\path，所以说\draw 相当于\path[draw]，而\clip 相当于\path[clip]，同理，\clip[draw] 就会被相应的变换成\path[draw, clip]。

#### 两种曲线：抛物线（parabole）和正弦波（sin）
一般来说，三个点确定一个抛物线，但是抛物线最简单的形式是：
``` tex
    \tikz \draw (0,0) rectangle (1,1) (0,0) parabole (1,1)；
```

这是因为它默认是画抛物线的一半（就像是平抛运动一样），但是完整形式并不是没有：
``` tex
    \tikz \draw [x=1pt, y=1pt] (0,0) parabole bend (4,16) (6,12)；
```

而sin 和cos 的path 长度是其对应的[0 , $\pi$/2]的区间上曲线。比如说一个完整的sin曲线为：
``` tex
    \tikz \draw[x=1.57ex , y=1ex] (0,0) sin (1,1) cos (2,0) sin (3,-1) cos (4,0);
```

#### 填充！
使用fill命令可以使用一个对应颜色填充一个path：
``` tex
    \fill [green!20!white] (0,0) -- (3mm,0mm) arc 
    [start angle=0, end angle=30, radius=3mm] --(0,0);
```

其中green!20!white 指20% 的green 和80% 的white 混合而成。这是Uwe Kern 的xcolor 包定义的，更多的可以去看看相关的文档。

而相关的，对于涉及一个封闭图形，更加推荐`-- cycle`结尾来构造一个封闭图形，以避免大部分错误。

也可以使用\filldraw来填充并绘制图形：
```
    \filldraw[fill=green!20!white, draw=green!50!black] (0,0)
    -- (3mm, 0mm) arc[strat angle=0, end angle=30, radius=3mm]
    -- cycle;
```

#### 渐变（哈哈哈哈，这个我觉得最没有用来啦）
对于渐变，主要有两种命令：\shade 和\shadedraw。
``` tex
    \tikz \shade (0,0) rectangle (2,1) (3,0.5) circle (.5cm);
```

一般默认的是从灰色变成白色，从上面渐变到下面。

它的参数有很多，定义了不同的渐变模式：
``` tex
\begin{tikzpicture}[rounded corners, ultra thick]
    \shade[top color=yellow, bottom color=black] (0,0) rectangle +(2,1);
    \shade[left color=yellow, right color=black] (3,0) rectangle +(2,1);
    \shadedraw[inner color=yellow, outer color=black, draw=yellow] (6,0) 
        rectangle +(2,1);
    \shade[ball color=green] (9,0.5) circle (0.5cm);
\end{tikzpicture}
```

#### 坐标的表示方法
一般来说，(1,2)表示一个x-vector（默认为1cm）和两个y-vector（当然也默认为1cm啦）相加而成。

除此以外，也有用极坐标来表示坐标的，如：`(30:1cm)`

也有用增量来表示的：

- `+(x, y)`表示在原点上增加相应向量，但path的末点未发生变化。
- 与之相对的是`++(x, y)`，其改变了path的末点。

也有用交点来表示的：
- `(30:1cm |- 0,0)`表示经过(30:1cm)的竖直线和经过了(0,0)的水平线相交的点。（那这么说，(2,1 -| 1,2)是不是也成立呢？)

可以注意到，path 其实一般来说包含两个意思，第一个是tikz 中最基本的方法，另外一层意思是表示一个图像集合、路径。

而tikz 是可以定义两个path的交点的。

注：哎呀妈呀，刚刚才发现，\end{tikzpicture}后面是有符号"."的。。。

使用两个path相交而成的交点，有以下步骤：
``` tex
\path [name path=upward line] (1,0) -- (1,1)
\path [name path=sloped line] (0,0) -- (30:1.5cm)

\draw [name intersections={of=upward line and sloped line, by = x}]
    [very thick, orange] (1,0) -- (x)
```

name 都是定义起来方便后面引用的，而定义path 和定义交点 intersections的语法不一样。这个注意就好。

哦哦对了，三角函数是可以表示值的，`{sin(30)}`，这个是要用大括号来框住的。

#### 箭头
可以添加命令的option，比如说-> 或者<-、<-> 来画出带有箭头的线。
``` tex
\draw [<->](0,0) arc [strat angle=180, end angle=30, radius=10pt];
```

而且箭头的样式也是可变的：

在tikzpicture 的begin 上，添加选项`[>=<kind of end arrw tip>]`来选择箭头样式，比如说：Stealth之类的。

也有更多不一样的箭头，比如说是`<<-`等等。

#### 组合
为了统一管理样式，可以在本身的tikzpicture 中再模块化，使用：
``` tex
\begin{scope}[thin]
    \...;
\end{scope}
```

注：一个显而易见但细想又显得十分有趣的事是，clip 命令也是受scope 模块组限制的。

注：关于命令的选项，因为所有的tikz 的大部分命令都会转变成path 命令。而option 有冲突时，此时样式是由最后的option 决定的。

参考
---------------------------------------
- [1][官方网址](http://www.texample.net/media/pgf/builds/pgfmanual_3.0.1a.pdf)，[镜像(html文档下打开)](./resources/pdf/pgfmanual.pdf)，[镜像(md文档下打开)](../resources/pdf/pgfmanual.pdf)