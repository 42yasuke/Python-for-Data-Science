def ft_filter(func, iterable):
    """
    filter(function or None, iterable) --> filter object

    Return an iterator yielding those items of iterable
    for which function(item) is true.
    If function is None, return the items that are true.
    """

    if func:
        return (it for it in iterable if func(it))
    return (it for it in iterable if it)
