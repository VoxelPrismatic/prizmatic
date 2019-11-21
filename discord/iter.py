from .models.Error import ClassError
import typing
import re

class _AllOf:
    """
    DESCRIPTION ---
        Makes a list of consecutive items that match a class
    
    PARAMS ---
       typ [class]
       - The class in question
    
    USAGE ---
        This is not a regular class. It must be used as follows:
        
            def function(arg1: AllOf[class]):
                ...
            
            def fun(arg0, arg1: AllOf[class], ...):
                ...
        
        This is a parameter class that forms a list of all consecutive
        arguments that match its class parameter. It is mainly used with
        commands for arguments and things.
    """
    def __init__(self, typ = None):
        self.converter = typ
    
    def __getitem__(self, typ):
        if type(typ) != type:
            raise ClassError(typ, type, [type])
        return self.__class__(typ = typ)
    
class _Option:
    """
    DESCRIPTION ---
        Has a default value but can be changed
        
    PARAMS ---
        typ [class]
        - The class
    
    USAGE ---
        This is not a regular class. It must be used as follows:
        
            def function(arg1: Option[class] = default_value):
                ...
            
            def fun(arg0, arg1: Option[class] = default_value, ...):
                ...
        
        This is a parameter class that forms an optional argument and will not
        break when an invalid param is passed [when the command is called]. It is
        mainly used with commands for arguments and things.
    """
    def __init__(self):
        pass
    
    def __getitem__(self, typ):
        if type(typ) != type:
            raise ClassError(typ, type, [type])
        return typing.Optional[typ]
        
class _Any:
    """
    DESCRIPTION ---
        Can be any of these values
        
    PARAMS ---
        *typ [class]
        - The classes, as a list
    
    USAGE ---
        This is not a regular class. It must be used as follows:
        
            def function(arg1: Any[class1, class2, ...]):
                ...
            
            def fun(arg0, arg1: Any[class1, class2, ...] = default_value, ...):
                ...
        
        This is a parameter class that forms an argument that can have multiple
        forms and will not break as often on a command call. It is mainly used 
        with commands for arguments and things.
    """
    def __init__(self):
        pass
    
    def __getitem__(self, *, param):
        return typing.Union[param]

class _Equation:
    """
    DESCRIPTION ---
        Allows for equations
    
    PARAMS ---
        *fns [str]
        - Allowed functions, at least one must be specified
    
    USAGE ---
        This is not a regular class. It must be used as follows:
        
            def function(arg1: Equation[operator]):
                ...
            
            def fun(arg0, arg1: Any[op1, op2, ...] = default_value, ...):
                ...
        
        Operators can be '+', '-', or any operator or function because it is a 
        string. It is mainly used with commands for arguments and things.
    """
    def __init__(self):
        pass
    
    def __getitem__(self, *, param):
        return re.compile("^(\d+ *(" + "|".join("\\".join(list(p)) for p in param) + ") *\d+)+$")
    