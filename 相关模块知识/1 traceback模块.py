import traceback

"""
异常的处理分为：异常对象、异常栈
异常对象包括raise，try expect finally等等对异常的处理往往比较简略，很多情况下简单的异常处理已经无法解决问题了
异常栈包括traceback模块，可以打印更加详细的信息
traceback object通常是通过函数sys.exc_info()来获取的
sys.exc_info()函数返回一个元祖，元祖的第一个数据是异常的类型（eg.ZeroDivisionError）,
    第二个数据是异常的value值，第三个就是我们要的traceback object包含出错的行数和位置等
Python的traceback模块提供一整套接口用于提取，格式化和打印python程序的stack traces信息
"""
import sys
import traceback

def func1():
    raise NameError("--func1 exception--")


def main():
    try:
        func1()
    except Exception as e:
        # 方式一
        # print("e:",e)   # e: --func1 exception--
        # 方式二
        exc_type, exc_value, exc_traceback_obj = sys.exc_info()
        print('exc_type', exc_type)
        print('exc_value', exc_value)
        print('exc_traceback_obj', exc_traceback_obj)
        # 输出到文件
        # with open(r'a.txt',mode='w') as f:
        #     traceback.print_tb(exc_traceback_obj, limit=1, file=f)
        traceback.print_tb(exc_traceback_obj)
        """
        traceback.print_tb(tb[, limit[, file]])
        tb: 这个就是traceback object, 是我们通过sys.exc_info获取到的
        limit: 这个是限制stack trace层级的，如果不设或者为None，就会打印所有层级的stack trace
        file: 这个是设置打印的输出流的，可以为文件，也可以是stdout之类的file-like object。如果不设或为None，则输出到sys.stderr。
        """


if __name__ == '__main__':
    main()