from ..ClsUtil import extra_kw

__all__ = ["AuditChange"]

class AuditChange:
    """
    {{cls}} instance = AuditChange(new_value, old_value, key)

    {{desc}} Represents an audit log change, that `01` you see

    {{note}} This class is almost useless. Don't use it.

    {{param}} new_value [Any]
        Value after the change

    {{param}} old_value [Any]
        Value before the change

    {{param}} key [str]
        The object changed, eg "role"

    {{param}} bot_obj [~/Bot]
        The Bot object, so you can access the bot anywhere
        {{optn}}

    {{prop}} new [Any]
        Value after the change

    {{prop}} old [Any]
        Value before the change

    {{prop}} key [str]
        The object changed

    {{prop}} bot_obj [~/Bot]
        The Bot object, so you can access the bot anywhere
    """
    def __init__(self, *, new_value, old_value, key, bot_obj = None, **kw):
        extra_kw(kw, "AuditChange")
        self.key = key
        self.new = new_value
        self.old = old_value

    def __dict__(self):
        """
        {{bltin}} instance.__dict__()
        {{usage}} dict(instance)

        {{pydesc}} __dict__

        {{rtn}} [str]
        """
        return {"new_value": self.new, "old_value": self.old, "key": self.key}

    def __repr__(self):
        """
        {{bltin}} instance.__repr__()
        {{usage}} repr(instance)

        {{pydesc}} __repr__

        {{rtn}} [str]
        """
        return "<AuditChange of " + self.key + ">"
