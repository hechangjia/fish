from manim import *

CN_TEX_TEMPLATE = TexTemplate(
    tex_compiler="xelatex",
    output_format=".xdv",
    preamble=r"""
\usepackage{ctex}
\usepackage{amsmath}
\usepackage{amssymb}
\setmainfont{Microsoft YaHei}
"""
)

class TimeShiftSystems(Scene):
    def construct(self):
        # 坐标轴范围优化（确保时变系统输出可见）
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 4, 1],  # y轴调整为[0,4]以适应幅度
            axis_config={"color": BLUE},
        )
        axes_labels = axes.get_axis_labels(x_label="t", y_label="x(t)")
        
        def gaussian(t, center, width):
            return np.exp(-(t - center)**2 / (2 * width**2))
        
        center = 3
        width = 0.5
        t_shift = ValueTracker(0)

        # 时不变系统定义（保持原延迟）
        def time_invariant_system(t):
            delay = 1
            return gaussian(t - delay, center, width)
        
        # 修改点：降低时变系统影响因子（系数0.5）
        def time_varying_system(t):
            return 0.5 * t * gaussian(t, center, width)  # 原为 t * x(t)
        
        # 信号曲线定义
        input_signal = axes.plot(lambda t: gaussian(t, center, width), color=YELLOW)
        ti_output = axes.plot(time_invariant_system, color=GREEN)
        tv_output = axes.plot(time_varying_system, color=RED)

        # 动态时移信号（同步修改影响因子）
        shifted_input = always_redraw(lambda: axes.plot(
            lambda t: gaussian(t - t_shift.get_value(), center, width), color=YELLOW_D))
        
        shifted_ti_output = always_redraw(lambda: axes.plot(
            lambda t: time_invariant_system(t - t_shift.get_value()), color=GREEN_D))
        
        shifted_tv_output = always_redraw(lambda: axes.plot(
            lambda t: 0.5 * (t + t_shift.get_value()) * gaussian(t, center, width),  # 同步系数0.5
            color=RED_D
        ))

        # 标签定义与位置优化
        title = Tex(
            r"\text{时变系统 vs 时不变系统}", 
            tex_template=CN_TEX_TEMPLATE,
            font_size=36
        ).to_edge(UP)
        
        input_label = Tex(
            r"$x(t) = e^{-\frac{(t-3)^2}{2 \times 0.5^2}}$", 
            color=YELLOW, 
            font_size=24
        ).next_to(input_signal, UP, buff=0.2)
        
        ti_label = Tex(
            r"\text{时不变系统输出: }$y(t) = x(t-2)$", 
            tex_template=CN_TEX_TEMPLATE,
            color=GREEN, 
            font_size=24
        ).next_to(axes.c2p(9.9, 0.8), LEFT)  # 调整到较低位置
        
        tv_label = Tex(
            r"\text{时变系统输出: }$y(t) = 0.5t \cdot x(t)$",  # 公式同步修改
            tex_template=CN_TEX_TEMPLATE,
            color=RED, 
            font_size=24
        ).next_to(axes.c2p(3.15, 2.4), RIGHT)    # 位置适配新幅度

        # 动画流程
        self.add(axes, axes_labels, title)
        self.play(Create(input_signal), Write(input_label))
        self.play(Create(ti_output), Write(ti_label), Create(tv_output), Write(tv_label))
        self.wait(1)
        
        self.add(shifted_input, shifted_ti_output, shifted_tv_output)
        self.play(t_shift.animate.set_value(2), run_time=3, rate_func=linear)
        self.wait(2)