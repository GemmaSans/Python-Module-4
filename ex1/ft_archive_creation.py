#!/usr/bin/env python3

import sys
import typing


def read_file(filename: str) -> typing.Optional[str]:
    try:
        print(f"Accessing file '{filename}'")
        f: typing.IO[str] = open(filename)
    except OSError as error:
        print(f"Error opening file '{filename}': {error}")
        return None
    try:
        text = f.read()
        print("---\n")
        print(text)
        print("\n---")
        return text
    except UnicodeDecodeError as error:
        print(f"Error reading file '{filename}': {error}")
        return None
    finally:
        f.close()
        print(f"File '{filename}' closed.")


def transform_file(text: str) -> None:
    print("\nTransform data:")
    lines = text.splitlines()
    transformed = [line + "#" for line in lines]
    new_text = "\n".join(transformed)
    print("---\n")
    print(new_text)
    print("\n---")

    new_name = input("Enter new file name (or empty): ")
    if not new_name:
        print("Data not saved.")
        return
    try:
        print(f"Saving data to '{new_name}'.")
        f2: typing.IO[str] = open(new_name, "w")
    except OSError as error:
        print(f"Error opening file '{new_name}': {error}")
        print("Data not saved.")
        return
    try:
        f2.write(new_text)
        print(f"Data saved in file '{new_name}'.")
    except OSError as error:
        print(f"Error writing file '{new_name}': {error}")
        print("Data not saved.")
    finally:
        f2.close()


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
    else:
        print("=== Cyber Archives Recovery & Preservation ===")
        text = read_file(sys.argv[1])
        if text is not None:
            transform_file(text)


if __name__ == "__main__":
    main()
