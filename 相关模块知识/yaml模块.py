# import yaml
# class Person(yaml.YAMLObject):
#     yaml_tag = '!person'
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __repr__(self):
#         print("self.__class__.__name__", self.__class__.__name__)
#         return '%s(name=%s, age=%d)' % (self.__class__.__name__, self.name, self.age)
#
# james = Person('James', 20)
#
# f = open(r'config.yaml','w')
# print(yaml.dump(james,f))
#
# print (yaml.dump(james))  # Python对象实例转为yaml
#
# lily = yaml.load('!person {name: Lily, age: 19}')
#
# print ('lily:',lily,lily.name )  # yaml转为Python对象实例



"""

"""
#
#
# import yaml
# import os
#
#
# class Loader(yaml.Loader):
#
#     def __init__(self, stream):
#         self._root = os.path.split(stream.name)[0]
#
#         super(Loader, self).__init__(stream)
#
#     def include(self, node):
#         filename = os.path.join(self._root, self.construct_scalar(node))
#         print('filename', filename)
#         with open(filename, 'r') as f:
#             return yaml.load(f, Loader)
#
# Loader.add_constructor('!include', Loader.include)

#
# def load_yaml(yaml_file):
#     """
#
#     :param yaml_file:
#     :return:
#     """
#     with open(yaml_file, 'r') as f:
#         config = yaml.load(f, Loader)
#     return config
#
# y = load_yaml('foo.yaml')
# print(y)


import yaml


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return 'Person(%s, %s)' % (self.name, self.age)

james = Person('James', 20)
print (yaml.dump(james))  # 没加表示器之前


def person_repr(dumper, data):
    return dumper.represent_mapping(u'!person', {"name": data.name, "age": data.age})  # mapping表示器，用于dict

yaml.add_representer(Person, person_repr)  # 用add_representer方法为对象添加表示器
print (yaml.dump(james))  # 加了表示器之后


def person_cons(loader, node):
    value = loader.construct_mapping(node)  # mapping构造器，用于dict
    name = value['name']
    age = value['age']
    return Person(name, age)

yaml.add_constructor(u'!person', person_cons)  # 用add_constructor方法为指定yaml标签添加构造器
lily = yaml.load('!person {name: Lily, age: 19}')
print (lily)