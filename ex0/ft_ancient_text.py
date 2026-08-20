#!/usr/bin/env python3

import sys
import typing


def read_file(filename: str) -> None:
    try:
        print(f"Accessing file '{filename}'")
        f: typing.IO = open(filename)
        print("---\n")
        print(f.read())
        print("---")
        f.close()
        print(f"File '{filename}' closed")
    except (FileNotFoundError, PermissionError) as error:
        print(f"Error opening file '{filename}': {error}")


def main() -> None:
    if len(sys.argv) == 1:
        print("Usage: ft_ancient_text.py <file>")
    else:
        print("=== Cyber Archives Recovery ===")
        read_file(sys.argv[1])


if __name__ == "__main__":
    main()
