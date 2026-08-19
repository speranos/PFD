def ft_filter(function, iterable):
    """
    A custom implementation of Python's built-in filter().

    Args:
        function: A function that returns True/False, or None.
        iterable: An iterable to filter.

    Returns:
        An iterator containing elements for which function(item) is True.
    """
    if not hasattr(iterable, '__iter__'):
        raise TypeError(f"'{type(iterable).__name__}' object is not iterable")

    if function is None:
        function = bool

    return (item for item in iterable if function(item))



def main():
    pass


if __name__ == "__main__":
    main()
