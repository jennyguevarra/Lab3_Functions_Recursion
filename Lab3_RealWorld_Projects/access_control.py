def audit_log(func):
    def wrapper(*args, **kwargs):
        print("Authorization Started")
        result = func(*args, **kwargs)
        print("Authorization Completed")
        return result
    return wrapper

def validate_access(level, control):
    threshold = control * 5
    if level >= threshold:
        return "ACCESS GRANTED"
    return "ACCESS DENIED"