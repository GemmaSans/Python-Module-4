#!/usr/bin/env python3

import sys
import typing


def read_file(filename: str) -> None:
    try:
        print(f"Accessing file '{filename}'")
        f: typing.IO[str] = open(filename)
    except OSError as error:
        print(f"Error opening file '{filename}': {error}")
        return
    try:
        text = f.read()
        print("---\n")
        print(text)
        print("\n---")
    except UnicodeDecodeError as error:
        print(f"Error reading file '{filename}': {error}")
    finally:
        f.close()
        print(f"File '{filename}' closed.")


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
    else:
        print("=== Cyber Archives Recovery ===")
        read_file(sys.argv[1])


if __name__ == "__main__":
    main()
