LaTeX学习手记04
=======================================
正文
---------------------------------------
### **（又回来啦)LaTeX基本使用手记**
#### 实现中英文混排
使用ctex 宏集，在xelatex 来编译。
``` tex
\documentclass[UTF8]{ctexart}
\begin{document}
    你好，world！
\end{document}
```

> 当然，除了使用ctex 宏集，也可以调用xeCJK 宏包。但大多数情况下不推荐这么做。

####  章节和段落
ctexart 和原生文档类article 中定义了五个控制序列来调整行文组织结构：
``` tex
\section{...}
\subsection{...}
\subsubsection{...}
\paragragh{...}
\subparagragh{...}
```

而在book/ ctexbook 中还定义了`\part{...}`，还在report /ctexrep 中定义了`\part{...}`。

#### 插入目录
使用`\tableofcontents`来插入目录。

可以使用`\maketitle`来改变目录和题目之间的顺序。

#### 插入数学公式
使用`\usepackage{amsmath}`来加载相关的宏包，以用来使用AMS 提供的数学功能。

而插入数学公式有两种插入方式：
``` tex
    $ ... $         %插入行内公式
    $$ ... $$       %插入行间公式
```

但是如果需要更多的功能时，使用环境是一个不错的选项：
``` tex
\begin{equation}
    ...
\end{equation}
```

（这样会把相关的公式编号）

更多的LaTeX 数学公式相关信息可以看看参考$^{[1]}$中的关于math 的相关信息。

#### 插入图片和表格
插入图片可以使用`\includepraphics{jpg.jpg}`命令（来自宏包graphicx）。

更多的option 可查阅相关文档$^{[4]}$。

插入表格可以使用最简单的`tabular`环境：
``` tex
\begin{tabular}{|l|c|r|}
    \hline
    名字&       学号&       是否可爱\\
    \hline
    小周&       1&          可爱到爆炸\\
    \hline
\end{tabular}
```

#### 浮动体
对于使用了占据大块空间的插图和表格，例如插图和表格，这种需要经常调整位置的模块，可以使用浮动体--一种可以自动调整位置的环境。
``` tex
\begin {figure}{htbp}
    \centering
    \includegraphics{a.jpg}
    \caption{标题}
    \label{标签}
\enf {figure}
```

#### 版面
设置页边距，可以使用`geometry`包。

#### 眉页眉脚
设置眉页眉脚可以使用`fancyhdr`包。这个和上面的都可以看看参考$^[2]$。

参考
---------------------------------------
- \[1][作者Liam Huang和ta的朋友整理的文档(因为非商用未告知，在这里表示谢意～爱你～(大雾) )](https://liam.page/attachment/attachment/LaTeX-useful-tools/LaTeX_Docs_2014.zip)，[镜像(html文档下打开)](./resources/zip/LaTeX_Docs_2014.zip)，[镜像(md文档下打开)](../resources/zip/LaTeX_Docs_2014.zip)
- \[2][一份其实很短的LaTeX入门文档](https://liam.page/2014/09/08/latex-introduction/)
- \[3][latex2e for authors(官方文档)](https://www.latex-project.org/help/documentation/usrguide.pdf)，[镜像(html文档下打开)](./resources/pdf/usrguide.pdf)，[镜像(md文档下打开)](../resources/pdf/usrguide.pdf)
- \[4][graphicx宏包的文件](http://texdoc.net/texmf-dist/doc/latex/graphics/graphicx.pdf)