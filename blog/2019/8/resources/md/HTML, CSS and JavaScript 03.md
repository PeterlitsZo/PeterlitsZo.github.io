HTML, CSS and JavaScript 03
===========================================
正文
-------------------------------------------
使用`<a>`来链接到其他 Web 地址上，关于如何寻址文件，有三种方法：
- 相对根地址：在 Web 服务器中，文档根目录就是 Web 内容的顶级目录的目录。使用如`<a herf="/zoo.html">`的形式来找到 Web 根目录下的 zoo.html 文件。
- 相对地址：使用点来表示层级结构。（开始的`./`好像可以省略欸）
- 绝对地址：包括协议域名和相关的层级结构，比如`<a herf="https://peterlitszo.github.io/index.html">`来定义。

在页面内使用标签的时候，用的是锚来指定。

使用 id 来设置唯一的锚点（在当前页面内），比如说：
``` HTML
<a id="top"></a>
<a href="#top">Return to Top</a>
```

如果是其他页面的锚点的话，使用时只要在`#`前加上文件地址就好（三种表示方法）

如果想要链接到电子邮件地址，使用实例如下：
``` HTML
<a href="mailto:yourusername@yourdomain.com">Send me an email message.</a>
```

还可以在链接中添加适当的变量：
``` HTML
<a href="mailto:yourusername@somedomain.com?Book Question&body=When is the next edition coming out?">author@somedomain.com</a>
```

（为了避免垃圾邮件，可以使用字符实体来编码，比如说用`&#97`来代替 `a`）

在新的窗口中打开链接则要使用 `target` 属性。

使用伪类可以用来描述元素的状态，一般最常遇到的是 `<a>` 标签，它有四种伪类：
- a:link 描述以前未被访问的超链接样式。
- a:visited 描述以前访问过并且存在浏览器记忆中的超链接的样式。
- a:hover 描述用户鼠标悬停在其上时的超链接样式。
- a:active 描述一个正在被单击但是尚未释放的链接样式。

需要注意的是，是伪类中的冲突的样式覆盖原来的样式，不然伪类会继承父样式。（笑）

注：制定样式表时可以使用如：
``` css
a:hover, a:active {
    color: #e03a3e;
}
```

这样可以同时注册多个样式。

使用 CSS 时，使用 `background-color` 属性和 `color` 来修改前景和背景颜色属性。

屏幕的解析度（清晰程度）可以使用 `dpi` 作为单位，意思是每英寸像素的数量，一般数值是 72，而图像尺寸通常用像素宽和像素高相乘表示。

一般对于 web 上的压缩图像来说，JPEG 格式工作地最好，一般来说，质量在85的时候会让大小和质量都较好。

对于尺寸，一般的电脑最低是 1024×768 px 的屏幕尺寸，但是把 800×600 作为最低尺寸并不是一个坏主意。（因为用户可能并不会全屏运行）

对于只有有限的颜色，完全可以使用 GIF 格式，它可以用来设计包含纯色背景和颜色较少的设计格式。

PNG 格式可以指定不同的透明度（而 GIF 只有一种透明度————完全透明）

为了导入图片，使用如下的格式：
``` html
<img src="myimage.gif" alt="My Image" />
```

其中 `alt` 指的是代替文本，对于本来就没有什么用的图片可以使用空文本串。

注：picture 标签可以使用不同格式的图片，可以看看～

还可以使用 `width` 和 `height` 来指定图片的长和宽。使用 `text-align` 来设置对齐属性（默认为 left ）但也可以直接使用 img 的 float 属性来更加有针对性的指定图片对于文字的环绕方式（比如说 left 或者 right）。对于图片的垂直对齐方式，可以使用 `vertical-align` 来指定。

注：图片或者一个块级元素也可以使用超链接来链接到外部。

图片还可以拥有一个背景，属性是：
- background-color 图片是透明的或者没有加载出来时可以看到。
- background-image 我？？？？
- ......

对于不规则而且也希望交互区域不规则的图片，可以使用图像映像：

使用 map 来创建图像映射：
``` HTML
<map name="mapname">
    <area shape="rect" coords="1,73,47,163"
        href="https://en.wikipeidia.org/wiki/Alaska"
        alt="Alaska" title="Alaska" />
    <!--the other area tags-->
</map>
```

其中的 area 标签的指示区是一个矩形，除此之外还有圆形和多边形。每个指示区值不同，坐标的意义就有所不同。href 指定区域链接到的位置，alt 允许提供一段与形状相关的代替文本。

为了使用图像映射，必须也要准备一份映射：
``` HTML
<img src="timezonemap.png" usemap="#timezonemap"
    style="border:none; width:997ppx; height:498px"
    alt="World Timezone Map">
```

为了在页面中加入多媒体文件，除了提供链接让人们下载外，还可以使用标签：
``` HTML
<object
    width="320"
    height="240"
    type="video/x-ms-wmv"
    data="pond.wmv">
</object>
```

不同的视频有着不同的文件类型，对应的 type 也不相同。

但在 HTML5 中，还可以使用 `<audio>` 标签来嵌入和播放音频文件————这种方式更加被推荐使用，它只用告诉地址就可以了，而不用告诉浏览其文件的类型。
``` HTML
<audio
    src=".mp3"
    preload="auto"
    ...>

    <p>...</p>
</audio>
```

其中`...`可以有以下属性：
- preload：有三个可能的值，none 指不缓存文件，auto 指缓冲文件，metadata 指缓冲元数据（我也不知道元数据是什么wwww）。
- controls：如果存在就用于音频播放器的控件。
- autoplay：如果存在，则一加载完就播放它。
- loop：如果存在，则继续重复播放文件直到手动停止它。

如果浏览器不支持该标签，就会加载 `<p>` 标签中的内容。

而播放视频文件和 `<audio>` 标签类似，不过使用的是 `<video>`，此外还需要指定宽和高。