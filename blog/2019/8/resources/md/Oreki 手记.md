Oreki 手记
==================================
正文
----------------------------------
因为感觉 markdown 很轻量级，但是对于专门用来做博客而言，却少了点什么，所以就在 markdown 的语法上面想构建一个自己的轻量级标记文本语言，而且可以转换成 HTML 文本。

为了实现这个，还专门在 github 上找了 markdown 的 python 实现方法。但是不行呀，看不懂，哭了。

今天在 Python Cookbook 上的 2.19 节 编写一个简单的递归下降解析器，就屁颠屁颠来做笔记了啦。

首先它说要用 `BNF` 或者 `EBNF` 的格式来表达语法，来看看什么是这个 `BNF`：

首先在 `thefreedictionary` 上面看看，感觉应该指的是 `Backus Naus Form`，但是好像不是很懂怎么用，又去看了看 `wiki`$^{[2]}$。

首先它有两种写法：一种是 `backus-naus form`，而另一种是 `backus normal form`，是一种和上下文无关的（或者说，和程序语言特性无关的）语法形式。通常用来描述语言语法形式，文档格式，或者结构格式。它用于需要精准描述的语言中。

BNF 的补充和扩展有：EBNF 和 ABNF 。

作为 Backus 的建议，（Backus 是谁哦？？？）这个方案用尖括号括住的形式用来表示一个类：
> As proposed by Backus, the formula defined "classes" whose names are enclosed in angle brackets. For example, \<ab>. 

其中的名字代表了最基本的符号。

Peter（不是我啦。。。）给出了 BNF 的描述：
> Sequences of characters enclosed in the brackets <> represent metalinguistic variables whose values are sequences of symbols. The marks "::=" and "|" (the latter with the meaning of "or") are metalinguistic connectives. Any mark in a formula, which is not a variable or a connective, denotes itself. Juxtaposition of marks or variables in a formula signifies juxtaposition of the sequence denoted.

一系列被尖括号括住的字符代表了最基础的一系列的语言元素，而标记 `::=` 和 `|` 就链接了基本语素。如果不是一个类或者说是链接标记的话，那么它就代表了它自己。并列的元素按顺序来代表（怪怪的。。。）

差不多是这样，英文实在是对我不太友好。

举个例子，简单的算数运算表达式：
``` text
    BNF  ------------------------
    expr ::= expr + term
        | expr - term
        | term
    term ::= term * factor
        | term / factor
        | factor
    factor ::= (expt)
        | NUM
    EBNF ------------------------（这个好像不是标准的）
    expt ::= term { (+|-) term }*
    term ::= factor { (*|/) factor }*
    factor ::= (expt)
        | NUM
```

关于 `BNF` 的语法结构：
``` text
    <syntax>         ::= <rule> | <rule> <syntax>
    <rule>           ::= <opt-whitespace> "<" <rule-name> ">" <opt-whitespace> "::=" <opt-whitespace> <expression> <line-end>
    <opt-whitespace> ::= " " <opt-whitespace> | ""
    <expression>     ::= <list> | <list> <opt-whitespace> "|" <opt-whitespace> <expression>
    <line-end>       ::= <opt-whitespace> <EOL> | <line-end> <line-end>
    <list>           ::= <term> | <term> <opt-whitespace> <list>
    <term>           ::= <literal> | "<" <rule-name> ">"
    <literal>        ::= '"' <text1> '"' | "'" <text2> "'"
    <text1>          ::= "" | <character1> <text1>
    <text2>          ::= '' | <character2> <text2>
    <character>      ::= <letter> | <digit> | <symbol>
    <letter>         ::= "A" | "B" | "C" | "D" | "E" | "F" | "G" | "H" | "I" | "J" | "K" | "L" | "M" | "N" | "O" | "P" | "Q" | "R" | "S" | "T" | "U" | "V" | "W" | "X" | "Y" | "Z" | "a" | "b" | "c" | "d" | "e" | "f" | "g" | "h" | "i" | "j" | "k" | "l" | "m" | "n" | "o" | "p" | "q" | "r" | "s" | "t" | "u" | "v" | "w" | "x" | "y" | "z"
    <digit>          ::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
    <symbol>         ::=  "|" | " " | "!" | "#" | "$" | "%" | "&" | "(" | ")" | "*" | "+" | "," | "-" | "." | "/" | ":" | ";" | ">" | "=" | "<" | "?" | "@" | "[" | "\" | "]" | "^" | "_" | "`" | "{" | "}" | "~"
    <character1>     ::= <character> | "'"
    <character2>     ::= <character> | '"'
    <rule-name>      ::= <letter> | <rule-name> <rule-char>
    <rule-char>      ::= <letter> | <digit> | "-"
```

而关于 `EBNF` 的语法结构如下：
``` EBNF
    letter = "A" | "B" | "C" | "D" | "E" | "F" | "G"
        | "H" | "I" | "J" | "K" | "L" | "M" | "N"
        | "O" | "P" | "Q" | "R" | "S" | "T" | "U"
        | "V" | "W" | "X" | "Y" | "Z" | "a" | "b"
        | "c" | "d" | "e" | "f" | "g" | "h" | "i"
        | "j" | "k" | "l" | "m" | "n" | "o" | "p"
        | "q" | "r" | "s" | "t" | "u" | "v" | "w"
        | "x" | "y" | "z" ;
    digit = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" ;
    symbol = "[" | "]" | "{" | "}" | "(" | ")" | "<" | ">"
        | "'" | '"' | "=" | "|" | "." | "," | ";" ;
    character = letter | digit | symbol | "_" ;
    
    identifier = letter , { letter | digit | "_" } ;
    terminal = "'" , character , { character } , "'" 
            | '"' , character , { character } , '"' ;
    
    lhs = identifier ;
    rhs = identifier
        | terminal
        | "[" , rhs , "]"
        | "{" , rhs , "}"
        | "(" , rhs , ")"
        | rhs , "|" , rhs
        | rhs , "," , rhs ;

    rule = lhs , "=" , rhs , ";" ;
    grammar = { rule } ;
```

还是挺棒的，但是不是我自己想出来的，还是有一点点难受 >_< ！

对于大型工程（大雾），一般需要将模块按层次组织成包，创建一个软件包结构只需要在每个目录中有一个 `__init__.py` 就可以了！

`__init__.py` 文件的目的本来就是包含可选的初始化代码，当代码遇到不同层次的代码时会首先触动运行（比如可以自动加载子模块）

参考
-----------------------------------
- \[1]Python Cookbook
- \[2][wiki of bnf](https://en.wikipedia.org/wiki/Backus%E2%80%93Naur_Form)