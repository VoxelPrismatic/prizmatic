from ..ClsUtil import from_ts

__all__ = ["Timestamps"]

class Timestamps:
    """
    {{cls}} instance = Timestamps()

    {{note}} This class shouldn't be initialized by hand. Don't do that.

    {{desc}} Represents a Discord "Timestamps" object

    {{param}} start [str, datetime.datetime]
        When the event started. If str, then it must be a valid ISO 8601
        timestamp.

    {{param}} end [str, datetime.datetime]
        When the event ended. If str, then it must be a vaid ISO 8601 timestamp.

    {{prop}} start [datetime.datetime]
        The start time

    {{prop}} end [datetime.datetime]
        The end time
    """
    def __init__(self, start, end):
        self.start = from_ts(start)
        self.end = from_ts(end)

    def __dict__(self):
        return {"start": self.start, "end": self.end}
