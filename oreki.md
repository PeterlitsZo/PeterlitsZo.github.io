v 0.1
~~~~~~~~~~~~~

Oreki v0.1 (cn)
====================================
因为一些原因，makedown 好像不是很适合做为一个轻量级的博客记录标记语言。为了记录博客，同时找点乐子，我借鉴了 HTML 和 markdown 来设计了 Oreki 的语法，希望它是一个轻量级，可扩展性高，历史负担低的标记语言。

Oreki 的意思是折木，是在《冰菓》中出场的男主。冰菓的作品公司是京都动画公司，大家都很了解了，就没什么好讲的了。这个标记语言就是也希望能过一种灰色的生活，不费力，不会出错（no error)，且以己心度日。

以下是 Oreki(v 0.1) 的 EBNF 定义：
``` EBNF
head = version, [sub_version], waveline;
body = {div};
tail = waveline;

version = "v ", digit, ".", digit, [".", digit], newline;
    (* such as "v 0.1" or "v 0.1.1" *)
sub_version = "s "character, {(character| digit| "_")}, newline;
    (* such as "s peterlits" or "s pirgo")
waveline = "~", {"~"};
    (* how to express a waveline in body which is not mean the end of the body?
       just add a space before the wave line :) *)

div = title| paragraph| code| blankline;
blank = " ", {blank}| tab, {blank};
blankline = blank, newline;

title = h1_title, h2_titlr, h3_title, h4_title, h5_title, h6_title;
h1_title = block, "=", {"="}, blankline;
h2_title = block, "-", {"-"}, blankline;
h3_title = "#", block;
h4_title = "#", h3_title;
h5_title = "#", h4_title;
h6_title = "#", h5_title;

block = 
```

首先要说，Oreki 分为三个部分：head，body，和 tail。

body 是在两条波浪线之间的部分，而 head 在波浪线之上，tail在波浪线之下。

head 中最重要的是在一开头就是版本信息。而版本信息确保了 oreki 文档无论在什么时候都能以同样的方式进行解析。
``` EBNF
head = version, [sub_version], waveline;
version = "v ", digit, ".", digit, [".", digit], newline;
    (* such as "v 0.1" or "v 0.1.1" *)
sub_version = "s "character, {(character| digit| "_")}, newline;
    (* such as "s peterlits" or "s pirgo")
waveline = "~", {"~"};
```

如上 EBNF 表达式一样，head 由
~~~~~~~~~~~~~~