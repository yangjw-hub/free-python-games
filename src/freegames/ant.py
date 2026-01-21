"""Ant, simple animation demo.

Exercises

1. Wrap ant around screen boundaries.
2. Make the ant leave a trail.
3. Change the ant color based on position.
   Hint: colormode(255); color(0, 100, 200)
"""

from random import *#提供随机数功能
from turtle import *

from freegames import vector

ant = vector(0, 0)
aim = vector(2, 0)


def wrap(value):
    """Wrap value around -200 and 200."""
    if value > 200 :
        value = -200
    elif value < -200 :
        value = 200
    
    return value  # TODO


def draw():
    """Move ant and draw screen."""
    ant.move(aim)
    ant.x = wrap(ant.x)#检查边界
    ant.y = wrap(ant.y)

    aim.move(random() - 0.5)
    aim.rotate(random() * 10 - 5)#随机旋转-5到5度

    clear()# 清除之前的绘制
    goto(ant.x, ant.y)# 移动到蚂蚁位置
    dot(4) # 画一个点（大小为4）

    ontimer(draw, 100)# 100毫秒后再次调用自身（创建动画）


setup(420, 420, 370, 0)# 窗口大小420x420，位置偏移370
hideturtle()# 隐藏乌龟光标
tracer(False)# 关闭动画效果，直接显示
up()# 抬起画笔（移动时不画线）
draw()
done()
