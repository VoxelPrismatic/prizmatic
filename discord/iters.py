from .models.Error import ClassError
import typing
import re

__all__ = [
    "AllOf",
    "_AllOf",
    "Option",
    "_Option",
    "Any",
    "_Any"
]

class _AllOf:
    """
    {{cls}} instance = _AllOf()

    {{desc}} Makes a list of consecutive items that match a class

    {{warn}} This class is used as an argument type. It is meant to be used as
    `async def command_name(inf, arg1, arg2: AllOf[data_type]): #code...`,
    where `data_type` is the type of data, eg `int` or `str`
    """
    def __init__(self, typ = None):
        self.converter = typ

    def __getitem__(self, typ):
        if type(typ) != type:
            raise ClassError(typ, type, [type])
        return self.__class__(typ = typ)

class _Option:
    """
    {{cls}} instance = _Option

    {{desc}} Has a default value but can be changed, will not throw an error if
    not a valid input

    {{warn}} This class is used as an argument type. It is meant to be used as
    `async def command_name(inf, arg1: Option[data_type]: norm_val): #code...`,
    where `data_type` is the type of data, eg `int` or `str` and `norm_val` is
    the default value
    """
    def __init__(self):
        pass

    def __getitem__(self, typ):
        if type(typ) != type:
            raise ClassError(typ, type, [type])
        return typing.Optional[typ]

class _Any:
    """
    {{cls}} instance = _Any()

    {{desc}} Can be any one of a list of data types

    {{warn}} This class is used as an argument type. It is meant to be used as
    `async def command_name(inf, arg1, arg2: Any[type1, type2, ...]): #code...`,
    where `type#` is the type of data, eg `int` or `str`
    """
    def __init__(self):
        pass

    def __getitem__(self, *, param):
        return typing.Union[param]

Any = _Any()
Option = _Option()
AllOf = _AllOf()
