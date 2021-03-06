import re
import datetime
import json
from .Error import ObjNotFoundError, ClassError

__all__ = [
    "from_ts",
    "https",
    "id_from_obj",
    "extra_kw"
]

def from_ts(ts) -> datetime.datetime:
    """
    {{sepfn}} from_ts(ts)

    {{desc}} Instead of writing `datetime.datetime.fromtimestamp(timestamp)`,
    you can just write `from_ts(timestamp)`

    {{param}} ts [str, datetime.datetime]
        A valid ISO 8601 timestamp

    {{rtn}} [datetime.datetime] The datetime object
    """
    if type(ts) == str and ts.lower() == "now":
        return datetime.datetime.utcnow()
    if ts is None:
        return None
    if type(ts) == datetime.datetime:
        return ts
    elif re.search(
            r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(.\d+)?\+\d{2}:\d{2}$",
            str(ts)
    ):
        return datetime.datetime.fromisoformat(ts)
    raise TypeError(f"Invalid time format for `{ts}`")

def https(thing):
    """
    {{sepfn}} https(thing)

    {{desc}} If `thing` is a valid attachment URL, it returns `thing`, otherwise
    it returns an empty string

    {{param}} thing [str]
        The URL to check

    {{rtn}} [str]
    """
    if re.search(r"^(https?|attachment)\:\/\/", thing):
        return thing
    return ""

def id_from_obj(obj, ls = [], cl = ""):
    if type(obj) == int:
        pID = obj
    elif type(obj) == str:
        try:
            pID = int(obj)
        except ValueError:
            for o in ls:
                if o.name == obj:
                    pID = obj.id
                    break
            else:
                raise ObjNotFoundError(
                    "An object of type `str`, `int`, or has an `id` attribute"
                    "or is of type " + cl
                )
    elif obj is None:
        pID = None
    else:
        try:
            pID = obj.id
        except AttributeError:
            raise ClassError(obj, int, [str, int, cl])
    return pID

def dump_json(d):
    return json.dumps(d, separators = [",", ":"], ensure_ascii = True)

def extra_kw(kw, cl):
    if kw:
        print(
            f"**WARNING** Class '{cl}' has extra kwargs added by the gateway:"
        )
        print("{")
        for k in kw:
            print("   ", k, ":", kw[k], type(kw[k]), ",\n")
        print("}")
