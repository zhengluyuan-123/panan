class ResourceInfo:
    _LOCAL_CONFIG_FILE ={}

    def __init__(self, location: str = None):
        self.resource_dir = location

    def get_resource(self) -> str:
        "返回资源路径"
        return self.resource_dir

    def __str__(self):
        return self.get_resource()

    def __hash__(self):
        return hash(self.get_resource())


    @classmethod
    def get(cls,location: str = None):
        key = cls.__module__ + cls.__name__
        return ResourceInfo._LOCAL_CONFIG_FILE.setdefault(key, cls(location))