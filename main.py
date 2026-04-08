from __future__ import annotations


def get_domain(mapping: dict) -> set:
    """Return the domain X (all inputs of the function)."""
    # === TODO ===
    # Your code here
    return set(mapping.keys())
    # === END TODO ===


def get_range(mapping: dict) -> set:
    """Return the range — the set of outputs actually mapped to."""
    # === TODO ===
    # Your code here
    return set(mapping.values())
    # === END TODO ===


def is_well_defined(mapping: dict, target: set) -> bool:
    """Return True if every output value is in the target set."""
    # === TODO ===
    # Your code here
    #if range of mapping is subset of target return rtue
    return True if get_range(mapping) <= target else False
    # === END TODO ===


def is_injective(mapping: dict) -> bool:
    """Return True if f is one-to-one (no two inputs map to same output)."""
    # === TODO ===
    # Your code here
    #if any output is duplicated itll be removed when get_rage produces
    #the outputd as a set, which would make the len shorter
    return True if len(get_range(mapping)) == len(mapping) else False
    # === END TODO ===


def is_surjective(mapping: dict, target: set) -> bool:
    """Return True if f is onto (range == target)."""
    # === TODO ===
    # Your code here
    return True if get_range(mapping) == target else False
    # === END TODO ===


def is_bijective(mapping: dict, target: set) -> bool:
    """Return True if f is both injective and surjective."""
    # === TODO ===
    # Your code here
    return True if is_surjective(mapping, target) and is_injective(mapping) else False
    # === END TODO ===
