"""Core functions for ft_package."""


def count_in_list(lst: list, item: any) -> int:
    """
    Counts the number of occurrences of item in lst.

    Args:
        lst: The list to search in.
        item: The item to count.

    Returns:
        The number of times item appears in lst.
    """
    return lst.count(item)
