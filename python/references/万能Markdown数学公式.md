[toc]

## 万能Markdown数学公式

[安装typora软件](https://www.typora.io/)

### 1、首先设置（windows）：

* 文件 ---> 偏好设置 ---> Markdown ---> 勾选Markdown扩展语法


* 设置完成，Mac系统，也找到对应的设置，进行设置



### 2、markdown格式

在markdown中展示数学公式，使用一对`$$`，或者四个`$$$$`

效果如下：

* `${\frac{-b \pm \sqrt{b^2-4ac}}{2a}}$`  ---> <font size = 4> $\frac{-b \pm \sqrt{b^2-4ac}}{2a}$</font>
* `$$-b \pm \sqrt{b^2-4ac} \over 2a$$`      ---> <font size = 4>$-b \pm \sqrt{b^2-4ac} \over 2a$</font>

这数学公式效果是不是<font color = 'red'>**非常炫酷**</font>啊，下面跟着我一起来学习吧！我主要使用一对$进行公式书写~





### 3、上下标

`^` 表示上标, `_` 表示下标。如果上下标的内容多于一个字符，需要用 `{}` 将这些内容括成一个整体。上下标可以嵌套，也可以同时使用。

上标语法：

```
$x^{y^z}=(1+e^x)^{-2xy^w}$
```

* 显示：

  $x^{y^z}=(1+e^x)^{-2xy^w}$

公式有点小，进行放大，并改变颜色：

```
<font size = 6 color = 'red'>$x^{y^z}=(1+e^x)^{-2xy^w}$</font>
```

* 显示：

  <font size = 6 color = 'red'>$x^{y^z}=(1+e^x)^{-2xy^w}$</font>

你仔细观察**字母e**有点斜，可以使用`{\rm e}` 来矫正

```
<font size = 6 color = 'green'>$x^{y^z}=(1+{\rm e}^x)^{-2xy^w}$</font>
```

* 显示：

  <font size = 6 color = 'green'>$x^{y^z}=(1+{\rm e}^x)^{-2xy^w}$</font>

先写下标再写上标：

```
<font size = 6 color = 'purple'>$C_n^2$</font>
```

* 显示：

  <font size = 6 color = 'purple'>$C_n^2$</font>

另外，如果要在左右两边都有上下标，可以用 `\sideset` 命令第一个花括号表示左边，第二个表示右边。

```
<font size = 6 color = 'blue'>$\sideset{^a_b}{^c_d}A$</font>
```

* 显示：

  <font size = 6 color = 'blue'>$\sideset{^a_b}{^c_d}A$</font>

### 4、分式与根号

`\frac{}{}` 表示分式，第一个花括号内容为分子，第二个花括号内容为分母

示例：

```
<font size = 6 color = 'red'>$f(x,y) = \frac{x + y}{3x^2 + 4y^{2.5}}$</font>
```

显示：

<font size = 6 color = 'red'>$f(x,y) = \frac{x + y}{3x^2 + 4y^{2.5}}$</font>



`\sqrt{}`表示开根号，`\sqrt[]{}`中括号表示开几次方，后面花括号为开方内容

```
<font size = 6 color = 'red'>$f(x,y) = \frac{\sqrt[3]{x^2 + y^3}}{3x^2 +4y^{2.5}}$</font>
```

显示：

<font size = 6 color = 'red'>$f(x,y) = \frac{\sqrt[3]{x^2 + y^3}}{3x^2 + 4y^{2.5}}$</font>

### 5、累加与累乘

使用 `\sum` 来输入一个累加。与之类似，使用 `\prod` `来输入累乘。

示例：

```
<font size = 6 color = 'red'>$\sum\limits_{i = 1}^nf(x_i)$</font>
```

显示：

<font size = 6 color = 'red'>$\sum\limits_{i = 1}^nf(x_i)$</font>

示例：

```
<font size = 6 color = 'red'>$\prod\limits_{i = 1}^n(x_i-1)(x_i + 2)$</font>
```

显示：

<font size = 6 color = 'red'>$\prod\limits_{i = 1}^n(x_i-1)(x_i + 2)$</font>

### 6、括号

`()`、`[]` 和 `|` 表示符号本身，使用 `\{\}` 来表示 `{}` 。当要显示大号的括号时，要用 `\left` 和 `\right` 命令

示例：

```
<font size = 6 color = 'red'>$f(x,y,z) = 2y^3z \left( 7+\frac{5x+8}{4+y^3} \right)$</font>
```

显示：

<font size = 6 color = 'red'>$f(x,y,z) = 2y^3z \left( 7+\frac{5x+8}{4+y^3} \right)$</font>



<font size = 6 color = 'red'>$f(x,y,z) = 2y^3z ( 7+\frac{5x+8}{4+y^3} )$</font>



<font size = 6 color = 'red'>$f(x,y,z) = 2y^3z \{ 7+\frac{5x+8}{4+y^3} \}$</font>



示例：

```
<font size = 6 color = 'red'>$\frac{du}{dx}|_{x = 0}$</font>
```

显示：

<font size = 6 color = 'red'>$\frac{du}{dx}|_{x = 0}$</font>



### 7、省略号

数学公式中常见的省略号有两种，`\ldots` 表示与文本底线对齐的省略号，`\cdots` 表示与文本中线对齐的省略号。

示例：

```
<font size = 6 color = 'red'>$f(x_1,x_2,\cdots,x_n) = x_1^2 + x_2^2 + \cdots + x_n^2$</font>
```

显示：

<font size = 6 color = 'red'>$f(x_1,x_2,\cdots,x_n) = x_1^2 + x_2^2 + \cdots + x_n^2$</font>



示例：

```
<font size = 6 color = 'red'>$f(x_1,x_2,\ldots,x_n) = x_1^2 + x_2^2 + \ldots + x_n^2$</font>
```

显示：

<font size = 6 color = 'red'>$f(x_1,x_2,\ldots,x_n) = x_1^2 + x_2^2 + \ldots + x_n^2$</font>



### 8、矢量

使用 `\vec{矢量}` 来自动产生一个矢量。也可以使用 `\overrightarrow` 等自定义字母上方的符号。`\cdot` 表示一个点，在公式中往往表示向量乘法。

示例：

```
<font size = 6 color = 'red'>$\vec{a} \cdot \vec{b}$</font>
```

显示：

<font size = 6 color = 'red'>$\vec{a} \cdot \vec{b}$</font>

左箭头，两边箭头，右箭头示例，其中`\quad` 表示四个空格：

```
<font size = 6 color = 'red'>$\overleftarrow{xy} \quad  \overleftrightarrow{xy} \quad \overrightarrow{xy}$</font>
```

显示：

<font size = 6 color = 'red'>$\overleftarrow{xy} \quad  \overleftrightarrow{xy} \quad \overrightarrow{xy}$</font>



### 9、积分

使用 `\int` 来输入一个积分。

示例：

```
<font size = 6 color = 'red'>$\int_0^1 {x^2} {\rm d}x$</font>
```

显示：

<font size = 6 color = 'red'>$\int_0^1 {x^2} {\rm d}x$</font>



<font size = 6 color = 'red'>$\int_0^1 {x^2} dx$</font>



### 10、极限运算

使用 `\lim` 来输入一个极限。`\to` 表示从箭头 ，`\infty` 表示无穷大，`\limits`表示置于正下方。

示例：

```
<font size = 6 color = 'red'>$\lim\limits_{n \to +\infty} \frac{1}{n(n+1)}$</font>
```

显示：

<font size = 6 color = 'red'>$\lim\limits_{n \to +\infty} \frac{1}{n(n+1)}$</font>





### 11、常用希腊字母

常用希腊字母：

|    小写    |   markdown   |    大写    |   markdown   |
| :--------: | :----------: | :--------: | :----------: |
|  $\Alpha$  |  `$\Alpha$`  |  $\alpha$  |  `$\alpha$`  |
|  $\Delta$  |  `$\Delta$`  |  $\delta$  |  `$\delta$`  |
| $\Lambda$  | `$\Lambda$`  | $\lambda$  | `$\lambda$`  |
|   $\Eta$   |   `$\Eta$`   |   $\eta$   |   `$\eta$`   |
| $\Epsilon$ | `$\Epsilon$` | $\epsilon$ | `$\epsilon$` |
|  $\Theta$  |  `$\Theta$`  |  $\theta$  |  `$\theta$`  |
|  $\Beta$   |  `$\Beta$`   |  $\beta$   |  `$\beta$`   |
|   $\Pi$    |   `$\Pi$`    |   $\pi$    |   `$\pi$`    |
|   $\Phi$   |   `$\Phi$`   |   $\phi$   |   `$\phi$`   |
|   $\Psi$   |   `$\Psi$`   |   $\psi$   |   `$\psi$`   |
|  $\Omega$  |  `$\Omega$`  |  $\omega$  |  `$\omega$`  |
|     ……     |      ……      |     ……     |      ……      |

更多希腊字母，参考百度百科：

[希腊字母](https://baike.baidu.com/item/%E5%B8%8C%E8%85%8A%E5%AD%97%E6%AF%8D)

### 12、方程组

表达式一：需要cases环境，起始、结束处以{cases}声明

```
<font size = 6 color = 'red'>
$\begin{cases}
a_1x+b_1y+c_1z=d_1\\
a_2x+b_2y+c_2z=d_2\\
a_3x+b_3y+c_3z=d_3\\
\end{cases}$</font>
```



显示：

<font size = 6 color = 'red'>
$\begin{cases}
a_1x+b_1y+c_1z=d_1\\
a_2x+b_2y+c_2z=d_2\\
a_3x+b_3y+c_3z=d_3\\
\end{cases}$</font>

表达方式二: 使用`\begin{array}\\ 表达式一\\表达式二... \end{array}`

```
<font size = 6 color = 'red'>
$\left\{\begin{array} \\
a_1x+b_1y+c_1z=d_1\\
a_2x+b_2y+c_2z=d_2\\
a_3x+b_3y+c_3z=d_3\\
\end{array}\right.$</font>
```

显示：（左边\left表示显示大的花括号，右边\right.表示不显示右边，\left和\right必须成对出现~）

<font size = 6 color = 'red'>
$\left\{\begin{array} \\
a_1x+b_1y+c_1z=d_1\\
a_2x+b_2y+c_2z=d_2\\
a_3x+b_3y+c_3z=d_3\\
\end{array}\right.$</font>

表达式三：需要align环境，起始、结束处以{align}声明，align表示对齐（也可以使用aligned，公式中的&表示对齐）

```
<font size = 6 color = 'red'>$f(x,y,z) = \left \{\begin{align} &3x + 5y +  z \quad &, x < 0  \\ &7x - 2y + 4z\quad&, x > 0 \\ &-6x + 3y + 2z \quad &,x = 0\end{align}\right.$</font>
```

显示：

<font size = 6 color = 'red'>$f(x,y,z) = \left \{\begin{align} &3x + 5y +  z \quad              &, x < 0  \\ &7x - 2y + 4z\quad&, x > 0 \\ &-6x + 3y + 2z \quad &,x = 0\end{align}\right.$</font>





复杂公式推导示例：（四个`\\\\`表示两次换行）

```
<font size = 6 color = 'red'>$\begin{aligned}l(\theta) &= \sum\limits_{i = 1}^n\log p(y^{(i)}|x^{(i)};\theta) \\ \\&=\sum\limits_{i = 1}^n\log\prod\limits_{j = 1}^k\phi_j^{I\{{y^{(i)} = j\}}}\\\\&= \sum\limits_{i = 1}^n\log\prod\limits_{j = 1}^k(\frac{e^{\theta_j^Tx^{(i)}}}{\sum\limits_{l = 1}^ke^{\theta_l^Tx^{(i)}}})^{I\{{y^{(i)} = j\}}}\end{aligned}$</font>
```

显示：

<font size = 6 color = 'red'>$\begin{aligned}l(\theta) &= \sum\limits_{i = 1}^n\log p(y^{(i)}|x^{(i)};\theta)\\ \\&=\sum\limits_{i = 1}^n\log\prod\limits_{j = 1}^k\phi_j^{I\{{y^{(i)} = j\}}}\\\\&= \sum\limits_{i = 1}^n\log\prod\limits_{j = 1}^k(\frac{e^{\theta_j^Tx^{(i)}}}{\sum\limits_{l = 1}^ke^{\theta_l^Tx^{(i)}}})^{I\{{y^{(i)} = j\}}}\end{aligned}$</font>

### 13、矩阵

使用 `\begin{matrix} ... \end{matrix}` 生成，每一行以 `\\` 结尾表示换行，各元素间以 `&` 隔开，右边的序号用 `\tag{n}` 表示。

```
<font size = 6 color = 'red'>$\begin{matrix}1 & 2 & 3\\4 & 5 & 6\\7 & 8 & 9 \end{matrix}\tag{1}$</font>
```



显示：

<font size = 6 color = 'red'>$\begin{matrix}1 & 2 & 3\\4 & 5 & 6\\7 & 8 & 9 \end{matrix}\tag{1}$</font>



带大括号

```
<font size = 6 color = 'red'>$\left\{\begin{matrix}1 & 2 & 3\\4 & 5 & 6\\7 & 8 & 9 \end{matrix}\right\}\tag{2}$</font>
```

或者：

```
<font size = 6 color = 'red'>$\begin{Bmatrix}1 & 2 & 3\\4 & 5 & 6\\7 & 8 & 9\end{Bmatrix}\tag{2}$</font>
```

显示：

<font size = 6 color = 'red'>$\left\{\begin{matrix}1 & 2 & 3\\4 & 5 & 6\\7 & 8 & 9 \end{matrix}\right\}\tag{2}$</font>



带中括号

```
<font size = 6 color = 'red'>$\left[\begin{matrix}1 & 2 & 3\\4 & 5 & 6\\7 & 8 & 9\end{matrix}\right]\tag{3}$</font>
```

或者：

```
<font size = 6 color = 'red'>$\begin{bmatrix}1 & 2 & 3\\4 & 5 & 6\\7 & 8 & 9\end{bmatrix}\tag{3}$</font>
```

显示：

<font size = 6 color = 'red'>$\left[\begin{matrix}1 & 2 & 3\\4 & 5 & 6\\7 & 8 & 9 \end{matrix}\right]\tag{3}$</font>



包含省略号，矩阵：（行省略号`\cdots`，列省略号`\vdots`，斜向省略号（左上至右下）`\ddots`）

```
<font size = 6 color = 'red'>$ \left\{ \begin{matrix}1 & 2 & \cdots & 5 \\ 6      & 7        & \cdots & 10       \\ \vdots & \vdots   & \ddots & \vdots   \\ \alpha & \alpha+1 & \cdots & \alpha+4\end{matrix} \right\}\tag{4} $</font>
```



显示：

<font size = 6 color = 'red'>$ \left\{ \begin{matrix}1 & 2 & \cdots & 5 \\ 6      & 7        & \cdots & 10       \\ \vdots & \vdots   & \ddots & \vdots   \\ \alpha & \alpha+1 & \cdots & \alpha+4\end{matrix} \right\}\tag{4} $</font>



### 14、常用符号

|   名称   |  markdown  |     预览     |
| :------: | :--------: | :----------: |
|   乘法   |   \times   |   $\times$   |
|   除法   |    \div    |    $\div$    |
|  正负号  |    \pm     |    $\pm$     |
|   大于   |   直接写   |     $>$      |
|   小于   |   直接写   |     $<$      |
| 大于等于 |    \ge     |    $\ge$     |
| 小于等于 |    \le     |    $\le$     |
|  正无穷  |   \infty   |   $\infty$   |
|  负无穷  |  -\infty   |  $-\infty$   |
| 带帽符号 |  \hat{y}   |  $\hat{y}$   |
|  不等于  |   \not=    |   $\not=$    |
|  不等于  |    \neq    |    $\neq$    |
|  约等于  |  \approx   |  $\approx$   |
|   因为   |  \because  |  $\because$  |
|   所以   | \therefore | $\therefore$ |
|    ……    |     ……     |      ……      |
