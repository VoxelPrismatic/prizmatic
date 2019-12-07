import datetime

__all__ = ["from_ts"]

def from_ts(ts):
    return datetime.datetime.fromtimestamp(ts)
