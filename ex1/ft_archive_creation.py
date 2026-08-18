#!/usr/bin/env python3

import sys
import typing


def read_file(filename: str) -> None:
    try:
        print(f"Accessing file '{filename}'")
        f: typing.IO = open(filename)
        text = f.read()
        print("---\n")
        print(text)
        print("\n---")
        f.close()
        print(f"File '{filename}' closed")
    except (FileNotFoundError, PermissionError) as error:
        print(f"Error opening file '{filename}': {error}")
        return

    print("\nTransform data:")
    print("---\n")
    new_text = text.replace("\n", "#\n")
    new_text = new_text + "#"
    print(new_text)
    print("\n---")

    new_name = input("Enter new file name (or empty): ")
    if new_name:
        try:
            print(f"Saving data to '{new_name}'")
            f: typing.IO = open(new_name, "w")
            f.write(new_text)
            print(f"Data saved in file {new_name}")
            f.close()
        except (FileNotFoundError, PermissionError) as error:
            print(f"Error opening file '{new_name}': {error}")
            print("Not saving data")
    else:
        print("Not saving data")


def main() -> None:
    if len(sys.argv) == 1:
        print("Usage: ft_ancient_text.py <file>")
    else:
        print("=== Cyber Archives Recovery & Preservation ===")
        read_file(sys.argv[1])


if __name__ == "__main__":
    main()
