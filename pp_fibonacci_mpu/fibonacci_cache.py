from functools import wraps


def memoize(func):
    """
    This wrapper function caches the results of the function.
    Cache is a dictionary with {func(*args) : function result}
    """
    cache = dict()

    @wraps(func)
    def memoized_func(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return memoized_func
