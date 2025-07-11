---
title: "测试"
description: "这是hugo主题blowfish的测试文档"
tags:
  - test
  - 测试
  - hugo
categories:
  - demo
  - blowfish
showhero: true
---



# 数学

{{< katex >}}
\(f(a,b,c) = (a^2+b^2+c^2)^3\)




$$
\int_a^bf(x)dx
$$



% KaTeX block notation
$$
\varphi = 1+\frac{1} {1+\frac{1} {1+\frac{1} {1+\cdots} } }
$$

\(\varphi = \dfrac{1+\sqrt5}{2}= 1.6180339887…\)





\[\varphi = 1+\frac{1} {1+\frac{1} {1+\frac{1} {1+\cdots} } }\]

# 图片



![test](img/Manim.png)





# 图标简码



{{< icon "github" >}}



{{< icon "favicon" >}}



{{< icon "gitlab" >}}



{{< icon "x-twitter" >}}



# 测试Mermaid



```mermaid
flowchart LR
A --> |你好|B
```

{{< mermaid >}}
graph LR;
A[Lemons]-->|你好|B[Lemonade];
B-->C[Profit]
{{< /mermaid >}}



# 测试Callout



{{< alert >}}
**警告！**此操作具有破坏性！
{{< /alert >}}





{{< alert icon="fire" cardColor="#e63946" iconColor="#1d3557" textColor="#f1faee" >}}
This is an error!
{{< /alert >}}



# 链接



{{< article link="/posts/gallery/" >}}





# 图库



{{< carousel images="{https://cdn.pixabay.com/photo/2016/12/11/12/02/mountains-1899264_960_720.jpg, gallery/03.jpg, gallery/01.jpg, gallery/02.jpg, gallery/04.jpg}" >}}





# 图表



{{< chart >}}
type: 'bar',
data: {
  labels: ['Tomato', 'Blueberry', 'Banana', 'Lime', 'Orange'],
  datasets: [{
    label: '# of votes',
    data: [12, 19, 3, 5, 3],
  }]
}
{{< /chart >}}



{{< github repo="hechangjia/hechangjia" >}}



{{< swatches "#64748b" "#3b82f6" "#06b6d4" >}}



{{< timeline >}}

{{< timelineItem icon="github" header="header" badge="badge test" subheader="subheader" >}}
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus non magna ex. Donec sollicitudin ut lorem quis lobortis. Nam ac ipsum libero. Sed a ex eget ipsum tincidunt venenatis quis sed nisl. Pellentesque sed urna vel odio consequat tincidunt id ut purus. Nam sollicitudin est sed dui interdum rhoncus. 
{{< /timelineItem >}}


{{< timelineItem icon="code" header="Another Awesome Header" badge="date - present" subheader="Awesome Subheader" >}}
With html code
<ul>
  <li>Coffee</li>
  <li>Tea</li>
  <li>Milk</li>
</ul>
{{< /timelineItem >}}


{{< timelineItem icon="code" header="Another Awesome Header">}}
{{< github repo="hechangjia/hechangjia" >}}
{{< /timelineItem >}}

{{< /timeline >}}



# 打字效果



{{< typeit >}}
你好,世界!我是贺昌嘉. 
{{< /typeit >}}



{{< typeit 
  tag=h3
  speed=50
  breakLines=false
  loop=true
>}}
Lorem ipsum dolor sit amet, 
consectetur adipiscing elit. 
{{< /typeit >}}


# 嵌入视频
{{< youtubeLite id="SgXhGb-7QbU" label="Blowfish-tools demo" >}}





