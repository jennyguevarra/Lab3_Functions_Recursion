def monitor(func):
    def wrapper(*args, **kwargs):
        print("Processing Started")
        # Ginagawang list para pwede nating gamitin ang sum() at len() sa main.py
        result = list(func(*args, **kwargs))
        print("Processing Completed")
        return result
    return wrapper

@monitor
def play_count_stream(limit):
    """Yield squared even numbers up to the limit."""
    for i in range(limit):
        if i % 2 == 0:
            yield i ** 2