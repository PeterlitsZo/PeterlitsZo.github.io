VS code 扩展
=====================================
因为一直在用yzane 的Markdown PDF 插件，但是有些地方有点把事情都办完了，导致定制性不高。所以在github 上clone 了它的源代码$^{[1]}$，并在微软的官方文档$^{[2]}$上看看插件是怎么调用API 的。

在老套的hello world$^[3]$ 之前，首先要安装`node.js` 和`git` 之后再安装`yeoman` 和`VS Code Extension Genertor`。

在安装`node.js` 时废了好久的时间。我下载的是已经编译好滴文件包。在`bin`二进制文件夹中，但是它不是全局的（可以使用`echo $PATH` 来查看全局环境），然后用`ln -s` 来把它链接到相关文件中，值得一提的是，好像使用这个必须使用绝对位置，而不能使用相对位置？

反正安装完后，发现官网介绍说node.js 和js 有点关系，这个还是有点意思的。

其中node.js 中还像python 一样有一个包管理器，在这里是npm，通过它下载后面两个包。

结果在安装后面两个包的时候又废了一些时间，原因是因为......相关的命令（比如说 yo）没有在PATH 里。

除了把相关程序链接到PATH 指定的文件夹中，还可以直接把它们所在的文件夹放在PATH 中，根据网络上说，可以（我对liunx 系统不是很熟啦）在`/etc/profile` 中最后一行中添加`export PATH="new path:$PATH"`（path 最后好像不用打斜杠欸），之后再使用`source /etc/profile`运行即可。

然后使用`yo code`来建立基本框架。

在vs code 中用`F5`打开就可以啦～启动调试模式后用`Ctrl+Shift+P`打开命令行，输入Hello World，就启动了插件的一个功能了，屏幕下方会出现“Hello World”。

可以看到，VS code 的主结构是`extension.js`，也可以学到第一个语句：在信息框里的输出信息。
``` js
vscode.window.showInformationMessage('Hello World!');
```

和在web 界面中使用的js 语句很像。

编辑改写后使用Reload（我没有，我关掉重开的，也可以），重新加载后不得不觉得，太棒了脚本语言！

之后讲解了怎么debug，主要是断点和运行时检查值。我之前从来没有在IDE 中用过（vscode集成的功能太多了，就把它看成是IDE也没有关系）

又学到了在console 中输出的方法：使用`console.log('')；`。

参考
--------------------------------------
- \[1][markdown-pdf 项目地址](https://github.com/yzane/vscode-markdown-pdf)
- \[2][VS code api](https://code.visualstudio.com/api)
- \[3][第一个扩展程序](https://code.visualstudio.com/api/get-started/your-first-extension)