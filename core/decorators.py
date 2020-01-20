def cache_decorator(func):
    cache = {}
    def cachedFunc(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return cachedFunc
