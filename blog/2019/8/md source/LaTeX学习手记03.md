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



参考
---------------------------------------
- [1][官方网址](http://www.texample.net/media/pgf/builds/pgfmanual_3.0.1a.pdf)，[镜像(html文档下打开)](./resources/pdf/pgfmanual.pdf)，[镜像(md文档下打开)](../resources/pdf/pgfmanual.pdf)