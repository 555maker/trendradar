# coding=utf-8
"""Text conversion helpers for notification output."""

from functools import lru_cache


@lru_cache(maxsize=1)
def _get_opencc_converter():
    try:
        from opencc import OpenCC
    except ImportError:
        return None

    return OpenCC("s2twp")


def to_traditional_chinese(text: str) -> str:
    """Convert Simplified Chinese text to Taiwan Traditional Chinese when available."""
    if not text:
        return text

    converter = _get_opencc_converter()
    if converter is None:
        return text

    return converter.convert(text)
