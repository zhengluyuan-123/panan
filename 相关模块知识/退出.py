import os
import sys

"""
os._exit() 和 sys.exit()
os._exit() vs sys.exit()
概述
python的程序有两中退出方式：os._exit()， sys.exit()。本文介绍这两种方式的区别和选择。
os._exit()会直接将python程序终止，之后的所有代码都不会继续执行。
sys.exit()会引发一个异常：SystemExit，如果这个异常没有被捕获，那么python解释器将会退出。如果有捕获此异常的代码，那么这些代码还是会执行。
捕获这个异常可以做一些额外的清理工作。0为正常退出，其他数值（1-127）为不正常，可抛异常事件供捕获。
"""

try:
    sys.exit(-1)
except SystemExit as e:
    print('e', e)
    # print('die')

finally:
    print('cleanup')


try:
    os._exit(0)
except:
    print('die')
print('os.exit')#不打印直接退出了

"""
综上，sys.exit()的退出比较优雅，调用后会引发SystemExit异常，可以捕获此异常做清理工作。
os._exit()直接将python解释器退出，
余下的语句不会执行。
一般情况下使用sys.exit()即可，一般在fork出来的子进程中使用os._exit()
一般来说os._exit() 用于在线程中退出
sys.exit() 用于在主线程中退出。
"""