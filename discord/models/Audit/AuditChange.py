class AuditChange:
    """
    DESCRIPTION ---
        Represents an audit log change, that `01` you see
    
    PARAMS ---
        This class is almost useless, don't use it.
        
        new_value [any]
        - After change
        
        old_value [any]
        - Before change
        
        key [str]
        - What changed
    
    FUNCTIONS ---
        None
    """
    def __init__(self, new_value, old_value, key):
        self.key = key
        obj = None
        self.new = new_value
        self.old = old_value