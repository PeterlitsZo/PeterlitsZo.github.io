LaTeX学习手记02
=======================================
正文
---------------------------------------
#### 坐标轴的变换
坐标轴可以使用option xshift 和yshift 来变换坐标轴。

除此之外关于坐标轴有：rotate（倾斜坐标轴），scale（缩放）。
``` tex
\begin{tikzpicture}[even odd rule, rounded corners=2pt, x=10pt, y=10pt]
    \filldraw[fillddraw=yellow!80!black]    (0,0)   rectangle (1,1)
             [xshift=5pt, yshift=5pt]       (0,0)   rectangle (1,1)
             [rotate=30]                    (-1,-1) rectangle (2,2)
\end{tikzpicture}
```

#### for!（激动）
tikz也有for循环:
``` tex
%\foreach是由pgffor来定义的。
\foreach \x in {1,2,3}  {$x = \x$,}
%输出x = 1,x = 2,x = 3,
```

其中，`1,2,3,4,5,6,7,8,9,10`也等价于`1, ... ,10`

使用更多的值：有时候我们想同时给一个for 式子赋两个值，比如说下一次想使用(0,0.5)处添加一个"\frac{1}{2}"的文本。这两个值息息相关，而\foreach 也提供了相应方法：
``` tex
\foreach \x/\xtext in {-1, -0.5/-\frac{1}{2} , 1}
    \draw (\x cm,1pt) -- (\x cm,-1pt) node[below] {$\xtext$};
```

#### 添加文本
使用node来添加文本。

可以使用`\anchor=<anchor>`来定义标注在对应点的方位。使用north，south，east 和west 或者由两个词汇表示的组合方位。

同时，它们还有等价的option，比如说below，above，left，right。但与上面不同的是，它还可以设置偏移量：`below=1pt`

当添加的文本是与点相关的时候，直接把node 放在点(x,y)后面，当添加的文本与path 中的线相关的时候，可以把线放在-- operate 后面。与线相关时也有相应的option ，比如说是`[very]near strat`、`midway`之类的。

使用pic 来为角添加文本。
``` tex
\begin{tikzpicture}[scale=3]
    \coordinate (A) at (1,0)
    \coordinate (B) at (0,0)
    \coordinate (C) at (30:1cm)

    \draw (A) -- (B) -- (C)
        pic [draw=green!50!black, fill=green!20, angle radius=9mm,
             "$\alpha$"] {angle = A--B--C};
    % 好像还可以添加一个扇形欸... 好厉害。
\end{tikzpicture}
```

参考
---------------------------------------
- [1][官方网址](http://www.texample.net/media/pgf/builds/pgfmanual_3.0.1a.pdf)，[镜像(html文档下打开)](./resources/pdf/pgfmanual.pdf)，[镜像(md文档下打开)](../resources/pdf/pgfmanual.pdf)