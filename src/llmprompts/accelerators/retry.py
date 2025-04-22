import time

def retry(func, *args, retries: int = 3, delay: float = 1.0):
    """Retry a function call upon exception."""
    for _ in range(retries):
        try:
            return func(*args)
        except Exception:
            time.sleep(delay)
    raise RuntimeError("Max retries exceeded")
