LaTeX学习手记01
================================
前言
--------------------------------
现在看看，感觉md真的还挺不错的，比如说要是用来做博客什么的，看起来也觉得：嗳，这不还可以吗？爱了爱了。

直到我想新建一个使用了大量数学公式，又需要排版的文档。。。我佛了。

啊啊，当然不是说MD不好。比如说现在写blog，真的没有必要用排版什么的，但是数学公式不一样啊。

正文
--------------------------------
### **在vscode中搭配LaTeX环境**
首先在vscode中的扩展商店中安装LaTeX Workshop插件，这样就可以轻松编辑tex源文件了，但不是编译。

然后要下载编译器，资料$^{[1]}$里说其实tex live$^{[2]}$挺好的，emmm，好吧，你说什么就是什么（笑），我什么都不懂欸。

下好了，然后发现它说安装路径只能有三个层级，哇哇哇哇，我想把它放到只装应用程序的文件夹了，但是好像不行欸。有点点难受，以后看看实在不行改改注册表？

现在在等它下载完之前，还需要准备一个浏览PDF的应用程序，我嘛觉得chrome就挺好的的，至少对于我就够用了。所以我就不下了。

在等他们下好之前，我先看看插件的文档先。

好像说下iso要快一点？www我都下了一个半个小时了才知道......而且有好多国内镜像网站都有相应的镜像来着。

### **第一个LeX文档（[官方文档链接](https://www.latex-project.org/help/documentation/)）**
``` tex
% hello.tex
\documentclass[a4paper]{article}
\usepackage{hyperref}
\begin{document}
Hello World!
\end{document}
```
不过不是我的第一个文档。。。

语法有：
|格式|注释|
|:----:|----|
|%|表示注释|
|\documentclass[...]{...}|指明文档类，比如说article、report|
|\usepackage{...}|载入宏包|
|\begin{document}...\end{document}|正文区，也可以用这个来调配环境|
|. . .|. . .|

不过编写中文文档时，最优秀的方法是用ctex文档类来排版中文文档。

### **LikZ使用手记**
LikZ是一个用于绘图的LaTeX宏包。

官方手册3.0.1，我在文末给出，更新于2019/08/11$^{[4]}$。

LikZ包含两层：System Layer和Basic Layer。我们只需要调用其中的System Layer之类的专门抽象化的过程。

第一个tex tizk文档：
``` tex
%pgfmanual.pdf 2.1
%in latex use the environment {tikzpicture}
%in plain tex use \tikzpicture and \endtizkpicture
\usepackage{tikz}                   %load tikz
\begin{document}
    \darw (0,0) .. controls (1,1) and (2,1) .. (2,0)
\end{tikzpicture}
```

但是也存在这种可能性：在tex上新建一个plain tex文件，专注于绘图：
``` tex
\input tikz.tex
\baselineskip=12pt
\hsize=6.3truein
\vsize=8.7truein
\tikzpicture                %in tex, use this instead of begin{}
    \draw (-1.5,0) -- (1.5,0);
    \draw (0,-1.5) -- (0,1.5);
\endtikzpicture
\bye                        %hahaha. bye? looks fun
```
还有conTeXt、采用内建型（inline）等等的解决方案。

#### 线段

TikZ中内建地最基本的就是path语句。使用以点开头，用path extension operations连接（比如说之前用过的--操作符）来新建一个path ,或者说另一个例子：
``` tex
<start piont> .. controls <first control point> and <second control point> .. <end point>
%可以删除and <second control point>，这样子，第一个控制点就会被使用两次。
```

但是使用曲线等过程直接来画圆的话，并不需要这么麻烦。
``` tex
% 基本图形
\tikz \draw (0,0) circle [radius=10pt];
\tikz \draw (0,0) ellipse [x radius=20pt, y radius=10pt];
\tikz \draw[rotate=30] (0,0) ellipse [x radius=20pt, y radius=10pt]
\tikz \draw (-0.5,-0.5) rectangle (-1,-1)
```

#### 网格
示例：
``` tex
\begin{tikzpicture}
    \draw (-1,5,0) -- (1,5,0)
    \draw (0,-1.5) -- (0,1.5)
    \draw (0,0) circle [radius = 1cm]
    \draw [step = 0.5cm] (-1,4)

参考
--------------------------------
- [1][使用VSCode编写LaTeX](https://zhuanlan.zhihu.com/p/38178015)
- [2][TeX Live](https://tug.org/texlive/)
- [3][LaTeX排版全解](https://www.cnblogs.com/jingwhale/p/4250296.html)
- [4][官方网址](http://www.texample.net/media/pgf/builds/pgfmanual_3.0.1a.pdf)，[镜像(html文档下打开)](./resources/pdf/pgfmanual.pdf)，[镜像(md文档下打开)](../resources/pdf/pgfmanual.pdf)
