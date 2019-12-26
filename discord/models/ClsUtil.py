import datetime
import re

__all__ = ["from_ts"]

def from_ts(ts) -> datetime.datetime:
    """
    {{sepfn}} datetime_object = from_ts(ts)

    {{desc}} Instead of writing `datetime.datetime.fromtimestamp(timestamp)`,
    you can just write `from_ts(timestamp)`

    {{param}} ts [str]
        A valid ISO 8601 timestamp

    {{rtn}} [datetime.datetime] The datetime
    """
    if type(ts) == datetime.datetime:
        return ts
    elif re.search(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}+\d{2}:\d{2}"):
        return datetime.datetime.fromtimestamp(ts)
    raise TypeError(f"Invalid time format for `{ts}`")
