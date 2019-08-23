HTML, CSS and JavaScript 02
==========================================
正文
------------------------------------------
### JavaScript 初步
第二章的一开始对应的原文就是原书的第四节了。JavaScript。

之前的无论是HTML 还是CSS 都不是程序设计语言和脚本语言。这让一般的HTML 页面不能进行交互（哈哈哈哈，我可能对一般有什么误解）。而JavaScript 作为一个易与HTML 页面结合的一种脚本语言就成了实现交互式的首选。

#### 添加 JavaScript 脚本
在Web 中，使用`<script>` 来把JS 脚本添加到Web 页面中。比如：
``` HTML
<script type="text/javascript">
    <!-- 这是注释吧～
    和C/C++ 的/* 和 */
    好像哦......
    都是多行注释呢
    好像也支持C++式的
    注释嘛-->
</script>
```

js 脚本可以放在不同的地方：
- 在页面主体内：脚本的输出会成为页面的一部分。
- 在`<head>` 标签之间：注意，不应该让头部的`<head>` 标签中的脚本创建输出。`<head>` 区域通常包括函数和信息（而不是内容）。
- 在HTML 标签内（注意，标签之间和标签之内是不一样的）：这会成为事件处理程序。
- 在单独的文件中：使用.js 后缀的文件来包含一个JavaScript 脚本。

``` HTML
<script type="text/javascript" src="filename.js"></script>
```

如上就是引入一个外部的JS 脚本的方法。（外部的js 文件除了可以增加它的模块化程度，也可以减少显示页面所花的时间。)

#### 最基本的 JavaScript 脚本
JavaScript 可以做很多有用的事情，比如说放置一个按钮。
``` HTML
<button type="button"
        onclick= "alert('You clicked the botton')">
        Click Me!
</button>
```

虽然不是很清楚，但是原文中的意思好像是`onclick` 的后面是JS 脚本。————也就是说它在标签里面，成为了一个事件处理程序。

#### JavaScript 变量和基本命令
在一个js 文档中，可以为之设置变量。（看了看，好像是面向对象的......想在脚本语言难不成都是面向对象的？）
``` js
now = new Date();
localtime = now.toString();
utctime = now.toGMSTString();
```

真有意思，oop 真的是一个很棒的特性。

最常用的命令就是在文档中输出的方法，`document.write`，比如说：
``` js
document.write("<p><strong>Local time:</strong> " + localtime + "</p>");
document.write("<p><strong>UTC time:</strong> " + utctime + "</p>");
```

#### JavaScript 脚本的调试
如果写的代码 js 可能有错误，而且又需要错误信息，那么可以打开浏览器的 `JavaScript Conaole` 命令，它会指出具体的错误。如果只是代码的行为不恰当，那么可以使用 `source` 选项卡，来仔细地调试————包括暂停、恢复运行和单步调试、设置断点。
- 断点：在该点处停止运行。
- Step Over：代码将推进一行。
- Step Into：代码将推进一行，不过如果代码在调用另一个函数，则会进入那个行数的第一行。
- Step Out：当前行数结束执行，带入调用行数的下一个代码行。

#### 扩展：HTML 和 CSS 的调试
如果想要调试 html 和 css，可以打开 `Developer Tools` 命令来检查元素（`Elements`），有错的代码会被浏览器自动改写成符合它自己标准的HTML 文件。可以通过它来调试HTML 和CSS 。

### 字符
#### 特殊字符
对于 Web 页面的特殊字符，可以使用`&#num;`或者`&letter;`来代替。（不过要我说......使用 utf8 格式的网页应该不用这么麻烦的把？）

一些不至于使用 CSS 来显式指定文本格式的格式化字体，有以下标签更加符合 HTML 的新潮流。
- `<sup>`：上标文本。
- `<sub>`：下标文本。
- `<em>`：强调文本。
- `<strong>`：醒目的文本。
- `<pre>`：等宽文本，保留空格和换行符。

#### 文本格式
而如果要使用 CSS 来指定文本格式，最主要的样式名称为：
- font-size
- font-family
- color

#### 引用 web 资源上的字体
为了使用在 web 界面上的文字，可以使用 src 属性定义一个新字体（而不至于依赖用户本地的字体库：
``` css
@font-face {
    font-family: 'some_name_goes_here';
    src: url('some_location_of_the_font_file');
}
```

#### 扩展
还可以使用 `text-align` 来定义对齐方式。

### 列表
HTML 列表有 三种形式：有序列表，无序列表和定义列表。
- 有序列表开始于`<ol>`，结束于`</ol>`，列表项封闭在`<li>`标签中。
- 无序列表的标签是`<ul>`，列表项和有序列表一样。
- 定义列表开始于`<dl>`，其中`<dt>`对每个列表项，`<dd>`针对的是定义项。

值得一提的是，列表支持相互嵌套。

### 表格
使用`<table>`来创建表格，而`<tr>`用于创建表格行，`<td>`用来创建表格中的数据。对于表格中的标题行来说，使用`<th>`标签来标记。

对于存在一列中又细分成了两行：
<table>
    <thead>
        <tr>
            <th colspan="2" style="text-align: center"> ----- Title ----- </th>
            <th style="text-align: center"> Description </th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td> Peterlits的冒险记 </td>
            <td> 送给各位猪头少年的指南 </td>
            <td> 专家评论：难以描述的感动 </td>
        </tr>
        <tr>
            <td> 关于她 </td>
            <td> 关于七子和不该抛弃的信念 </td>
            <td> 专家无法评论，并表示我太难了 </td>
        </tr>
    </tbody>
</table>

比如说上面的 Title 下面就有两行，是使用`<th>`中的属性`colspan`来定义的（看了看，好像这个应该叫作跨越，即强制一个单元格跨越表格的多行或多列的效果）：
``` HTML
    <th colspan="2"> ----- Title ----- </th>
```

关于文本在表中的位置，可以使用 `vertical-align` 来指定，比如说 `top`，`middle`，`bottom` 等等的属性。

总结
-------------------------------------------
这一次主要介绍了 JS 和一些特殊的 HTML 格式————比如说，表格，或者说，列表。当然，还谈到了关于文本格式的问题。

现在第六章已经看完了从第四章一直到第七章～我就悄悄给我一个鼓励吧！`(*^__^*)` 嘻嘻……

参考
-------------------------------------------
- \[1][CSS完整参考指南](http://www.w3.org/Style/CSS/)（虽然是官网，但是好像现在还没有找到标准文档）
- \[2]HTML、CSS 和 JavaScript 入门经典