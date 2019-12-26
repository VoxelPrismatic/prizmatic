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

    {{prop}} new [Any]
        Value after the change

    {{prop}} old [Any]
        Value before the change

    {{prop}} key [str]
        The object changed
    """
    def __init__(self, new_value, old_value, key):
        self.key = key
        self.new = new_value
        self.old = old_value

    def __dict__(self):
        """
        {{fn}} dict(instance)

        {{desc}} Returns the send-ready object

        {{rtn}} [dict] The send-ready object
        """
        return {"new_value": self.new, "old_value": self.old, "key": self.key}

    def __repr__(self):
        """
        {{fn}} repr(instance)

        {{desc}} Returns the proper name, used for printing

        {{rtn}} [str] The proper name
        """
        return "<AuditChange of " + self.key + ">"
