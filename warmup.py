from __future__ import annotations

from typing import Iterable, TypeVar, Union

T = TypeVar("T")


def binomial(n: int, k: int) -> int:
    """Binomial coefficient, nCr, aka the "choose" function

    :param n: Size of set to choose from.
    :param k: Size of chosen subset.
    :return combinations: Number of possible combinations
    """
    if not 0 <= k <= n:
        return 0
    p = 1
    for i in range(1, min(k, n - k) + 1):
        p *= n
        p //= i
        n -= 1
    return p


def generate_permutations(items: Union[list[T], tuple[T]]) -> Iterable[tuple[T]]:
    """Generates all permutations of the input list or tuple.

    :param items: A list or tuple of n elements.
    :return permutations: An iterable of all n! possible permutations of the input.
    """

    # TODO
    pass


def generate_subsets(items: Union[list[T], tuple[T]], k: int) -> Iterable[tuple[T]]:
    """Generates all k-sized subsets of the input list or tuple.

    :param items: A list or tuple of n elements.
    :param k: Size of subsets.
    :return subsets: An iterable of all (n choose k) subsets of the input with cardinality k.
    """
    n = len(items)
    if not 0 <= k <= n:
        raise ValueError(f"Must have 0<=k<=n, got k={k} and n={n}")

    # TODO
    pass


def generate_powerset(items: Union[list[T], tuple[T]]) -> Iterable[tuple[T]]:
    """Generates the powerset of the input list.

    :param items: A list of n elements.
    :return powerset: An iterable of all 2^n possible subsets of the input.
    """

    # TODO
    pass