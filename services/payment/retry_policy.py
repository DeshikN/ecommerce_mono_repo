import time
def retry_count(attempts):
    return attempts + 1 if attempts < 3 else attempts
