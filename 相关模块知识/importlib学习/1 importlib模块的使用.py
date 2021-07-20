
"""
Python提供了importlib包作为标准库的一部分。目的就是提供Python中import语句的实现（以及__import__函数）。另外，importlib允许程序员创建他们自定义的对象，可用于引入过程（也称为importer）。



动态引入
检查模块是否可以被引入
引入源文件自身
第三方模块 import_from_github_com

"""

# ###################动态引入
"""
importlib模块支持传入字符串来引入一个模块。
"""
# import importlib
# def dyamic_import(module):
#     return importlib.import_module(module)
#
# if __name__=="__main__":
#     module = dyamic_import('foo')
#     module.main()
#
#     module_two = dyamic_import('foo')
#     module_two.main()


# ###################模块引入检查

"""
importlib模块支持传入字符串来引入一个模块。
"""

# import importlib.util
# import importlib
#
#
# def check_module(module_name):
#     module_spec = importlib.util.find_spec(module_name)
#     if module_spec is None:
#         print("Module :{} not found".format(module_name))
#         return None
#     else:
#         print("Module:{} can be imported!".format(module_name))
#         return module_spec
#
#
# def import_module_from_spec(module_spec):
#     module = importlib.util.module_from_spec(module_spec)
#     module_spec.loader.exec_module(module)
#     return module
#
#
# """
# 这里我们引入importlib模块的子模块util。在check_module函数中，我们调用find_spec函数来检查传入的字符串
# 作为模块是否存在。首先，我们传入一个假的名称，然后我们传入一个Python模块的真实名称。如果你运行这段代码，
# 你将会看到你传入一个没有安装的模块的名称，find_spec函数将会返回None，我们的代码将会打印出这个模块没有找到。
# 如果找到了，我们就会返回模块的说明。我们可以获取到模块的说明，然后使用它来真正的引入模块。或者你可以将字符串
# 传入到import_module函数中，正如我们在2.1节中所学习到的一样。但是我们已经学习到如何使用模块的说明。让我们
# 看一下上述代码中的import_module_from_spec函数。它接受由check_module函数返回的模块说明。我们将其传入
# 到module_from_spec函数，它将会返回引入的模块。Python的官方文档推荐，在引入模块后执行它，所以我们下一步做
# 的就是调用exec_module函数。最后我们返回这个模块，并且运行Python的dir函数来确认这个我们就是我们所期望的。
#
# """
#
# if __name__ == "__main__":
#     module_spec = check_module("fake_module")
#     module_spec = check_module("collections")
#     if (module_spec):
#         module = import_module_from_spec(module_spec)


# ###################从源文件中引入

import importlib.util


def import_source(module_name):
    module_file_path = module_name.__file__
    module_name = module_name.__name__

    module_spec = importlib.util.spec_from_file_location(module_name, module_file_path)
    module = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(module)
    print(dir(module))

    msg = "The {module_name} module has the following methods:{methods}"
    print(msg.format(module_name=module_name, methods=dir(module)))

"""
上述代码中，我们实际引入了logging模块，并将它传入到import_source函数。在这个函数中，我们首先获取到模块的实际路径和名称。
然后我们将这些信息传入到util的spec_from_file_location函数中，这个将会返回模块的说明。一旦我们获取到模块的说明，
我们就可以使用与2.2节相同的importlib机制来实际引入模块。

"""

if __name__ == "__main__":
    import logging

    import_source(logging)