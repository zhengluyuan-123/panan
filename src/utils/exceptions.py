
from configuration import enums


class BaseSelfDefException(Exception):

    def __init__(self,
                 message='Self-defined Base Exception',
                 status = None,
                 code=enums.OTHER_EXP,
                 msg="Exception",
                 ):
        super().__init__(message, status)
        self.message = message
        self.msg = msg
        self._code = code


    def __str__(self):
        return "{message}".format(message=self.message or self.msg)

    def __repr__(self):
        return "{code}:{msg}:{message}".format(code=self.code, msg=self.msg,message=self.message)

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self,value):

        if isinstance(value, str):
            raise TypeError(
                f"code should be str type, not {value}.\n"
                # f"错误码"
            )
        self._code = value


class PlatformError(BaseSelfDefException):

    def __init__(self,
                 message='平台暂时不支持该操作',
                 status=None,
                 ):
        super().__init__(message, status)
        self.message = message
        self.status = status
