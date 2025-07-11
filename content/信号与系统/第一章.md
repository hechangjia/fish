---

title: 信号与系统第一章
author: 贺昌嘉
tags: 
  - 总结
  - 笔记
created date: 2025年5月17日22:36:39
completed date: 

---

```markmap
---
markmap:
  zoom: false
  pan: false
  height: 300px
  backgroundColor: "#f8f8f8"
---

# 信号与系统的基本介绍
# 信号的定义与分类
## 信号的定义
## 信号的分类
# 系统的定义与分类
## 系统的定义
## 系统的分类
# 热手习题
```

![框架](/image/第一章_1747654023686.svg)

# 信号与系统的基本介绍

```kanban
Briefly Abstract
# Briefly Abstract

## 信号
- 定义 (<span style="text-emphasis:filled red;">信号</span>与<span style="text-emphasis:filled red;">函数</span>在这门课中常常通用.)
- 分类 (确定信号 | 随机信号\n连续时间信号 | 离散时间信号\n周期信号 | 非周期信号\n能量信号 | 功率信号)

## 系统
- 定义 (系统是由若干<span style="text-emphasis:filled red;">互相关联</span>的单元组成的具有一定功能的<span style="text-emphasis:filled red;">有机整体.</span>)
- 分类 (连续时间系统 | 离散时间系统\n线性系统 | 非线性系统\n时不变系统 | 时变系统\n因果系统 | 非因果系系统)

## Conclusion

```

[TOC]

---

# 信号的定义与分类

## 信号的定义

  在日常生活中,我们往往会接收到外界的各种<span style="text-emphasis:filled red;">信号</span>.它们有时是我们看到的景象,是光信号;有时是手机之间的通信,存在着电磁信号;最常见的可能是电的使用,是电信号.

  这门课的学习中,信号不再是一个看不见摸不着的东西,而是转化为<span style="color:#FF3399; letter-spacing:3pt;">函数</span>,一个我们可以利用数学去分析的内容.而一般来说,这个函数的自变量通常是时间 $t$,因此就是研究函数 $f(t)$.

  而函数$f(t)$,我们又可以从两个不同角度来描述:

1. 时域角度:研究自变量 $t$,包括周期,振幅等内容.
2. 频域角度:由于时间$t$和频率$f$之间的关系,通过$Fourier变换,Laplace变换$,可以实现从时域到频域的变换以及反变换.

## 信号的分类

对信号的分类,我们可以从对函数$f(t)$的研究入手.

1. 确定信号 | 随机信号:[^与老师的一个小讨论]

   - 确定信号:$f(t)$有解析式
   - 随机信号:$f(t)$无法写出解析式.

2. 连续时间信号 | 离散时间信号

   - 连续时间信号: 自变量为连续时间变量$t$.[^math]
   - 离散时间信号: 自变量为时间序列${t_k}$,函数值只有在离散时刻$t_k$上存在,可以将离散时间变量视作对连续时间变量的理想抽样.

3. 周期信号 | 非周期信号

   - 周期信号: 形如, 
     $$
     f(t) = f(t + T), -\infty < t < \infty
     $$

     $$
     f(t_k) = f(t_k + N);-\infty < t < \infty,K 与 N均为整数. 
     $$

4. 能量信号 | 功率信号

   划分标准: 平方可积性,根据信号$f(t)$在时间区域$(-\infty ,\infty)$上能量和功率是否为有限值来判断.

   表达式:
   $$
   E = \lim_{T \to \infty} \int_{-T}^{T}|f(t)|^2dt
   $$

   $$
   P = \lim_{T \to \infty} \frac{1}{2T}\int_{-T}^{T}|f(t)|^2dt
   $$

   - 能量信号; 当$E$为有限值时,是能量信号.此时功率$P$必不可能为有限值,有反证法易证.

   - 功率信号: 当$P$为有限值时,是功率信号,此时能量$E$必为无限值.

   - 当$E,P$均为无限值时,信号$f(t)$既不是能量信号,也不是功率信号;但绝不可能既是能量信号又是功率信号.
   - 当$f(t)$为直流信号(常数)或者周期信号时,$f(t)$为功率信号.且容易计算相关功率.

[^math]: 由高数的知识我们可以知道,当存在有限个第一类间断点的时候,依然成立.

---



# 系统的定义与分类

## 系统的定义

> [!Important]
>
> #### 官方表述
>
> 系统是由若干<span style="text-emphasis:filled red;">互相关联</span>的单元组成的具有一定功能的<span style="text-emphasis:filled red;">有机整体.</span>

- 系统是可以嵌套的,一个大系统可以嵌套若干级小系统;最基本的子系统称之为<span style="color:#CC0066;">单元</span>
- 研究系统时,通常视为一个黑盒子,不关心其内部到底是怎样运作的,而关心对输入的<span style="text-emphasis:filled red;">激励</span>与得到输出的<span style="text-emphasis:filled red;">响应</span>之间的关系:即$y(t)$与$x(t)$之间的函数关系.
- 常见的系统数学模型有:
  - 微分方程
  - 差分方程

## 系统的分类

1. 连续时间系统 | 离散时间系统

   - 连续时间系统: 激励$x(t)$与响应$y(t)$均为连续时间信号,对应系统的模型为微分方程.
   - 离散时间信号: 激励$x(t)$与响应$y(t)$均为离散时间信号,对应系统的模型为差分方程.

2. 线性系统 | 非线性系统

   - 线性特性:

     - 齐次性: 
       $$
       对 x(t)\Rightarrow y(t);
       $$

       $$
       有k*x(t)\Rightarrow k* y(t)
       $$

     - 可加性:
       $$
       对x_1(t)\Rightarrow y_1(t),x_2(t)\Rightarrow y_2(t)
       $$

       $$
       有x_1(t)+x_2(t)\Rightarrow y_1(t)+y_2(t)
       $$

   - 线性系统:满足以下三个条件:

     1. 可分解性:系统的响应可以分为零输入响应$y_{zi}(t)$与零状态响应$y_{zs}(t)$
     2. 零输入响应$y_{zi}(t)$满足线性特性.
     3. 零状态响应$y_{zs}(t)$满足线性特性.

3. 时不变系统 | 时变系统

   1. 时不变系统,若激励$x(t)$延时一段时间$t_d$成为$x(t-t_d)$,则响应$y(t)$对应延时$t_d$成为$y(t-t_d)$,
      $$
      对 x(t)\Rightarrow y(t);
      $$

      $$
      在时不变系统中有: x(t-t_d)\Rightarrow y(t-t_d);
      $$

      演示视频:[video](https://raw.githubusercontent.com/hechangjia/Picture_Deposit/master/Win10/TimeShiftSystems.mp4)

      <video controls width="80%">
        <source src="./video/TimeShiftSystems.mp4" type="video/mp4">
      </video>

4. 因果系统 | 非因果系系统

   - 现实存在的系统都是因果系统.响应不会超前于激励.





---







# 热手习题[^1]





















[^与老师的一个小讨论]: <img src="https://raw.githubusercontent.com/hechangjia/Picture_Deposit/master/Win10/%E9%9A%8F%E6%9C%BA%E4%BF%A1%E5%8F%B7.jpg" style="zoom:25%;" />
[^1]: 主要来自书本习题.

















