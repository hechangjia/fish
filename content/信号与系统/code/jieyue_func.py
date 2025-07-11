import numpy as np
import matplotlib.pyplot as plt
import os

# 配置中文字体和数学排版
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用黑体显示中文
plt.rcParams['axes.unicode_minus'] = False    # 正常显示负号
plt.rcParams['text.usetex'] = False           # 不使用LaTeX引擎
plt.rcParams['mathtext.fontset'] = 'cm'       # 使用Computer Modern数学字体


x = np.linspace(-10, 10, 1000)
y = np.piecewise(x, [x < -2, x > -2], [lambda x: 0, lambda x: 1])

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(x, y, linewidth=2, color='blue')
ax.grid(True, linestyle='--', alpha=0.6)

# 设置坐标轴样式
ax.spines['left'].set_position('zero')    # 将y轴移动到x=0位置
ax.spines['bottom'].set_position('zero')  # 将x轴移动到y=0位置
ax.spines['right'].set_color('none')      # 隐藏右侧边框
ax.spines['top'].set_color('none')         # 隐藏顶部边框

# 添加箭头
ax.plot(1, 0, 'k>', markersize=10, transform=ax.get_yaxis_transform(), clip_on=False)  # x轴箭头
ax.plot(0, 1, 'k^', markersize=10, transform=ax.get_xaxis_transform(), clip_on=False)  # y轴箭头

# 设置坐标轴范围
ax.set_xlim(-8, 8)
ax.set_ylim(-0.1, 1.2)

# 添加标签
ax.set_xlabel('x', fontsize=12, loc='right')
ax.set_ylabel('y', fontsize=12, loc='top')
ax.set_title(r'时延阶跃函数图像,$t_0 = -2$', fontsize=14)

# 调整布局并显示
plt.tight_layout(rect=[0, 0, 1, 0.96])
# 保存到当前脚本所在目录的 subfolder 中
image_save_dir = "../image"  # 相对路径（当前目录下的 output_images 文件夹）
os.makedirs(image_save_dir, exist_ok=True)

plt.savefig(os.path.join(image_save_dir, "时延阶跃函数图像2.png"), 
           dpi=300, 
           bbox_inches='tight')
plt.show()