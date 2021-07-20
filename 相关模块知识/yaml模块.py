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


import yaml
import os


class Loader(yaml.Loader):

    def __init__(self, stream):
        self._root = os.path.split(stream.name)[0]

        super(Loader, self).__init__(stream)

    def include(self, node):
        filename = os.path.join(self._root, self.construct_scalar(node))
        print('filename', filename)
        with open(filename, 'r') as f:
            return yaml.load(f, Loader)

Loader.add_constructor('!include', Loader.include)


def load_yaml(yaml_file):
    """

    :param yaml_file:
    :return:
    """
    with open(yaml_file, 'r') as f:
        config = yaml.load(f, Loader)
    return config

# y = load_yaml('foo.yaml')
# print(y)