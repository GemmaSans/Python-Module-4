#!/usr/bin/env python3

import sys
import typing


def read_file(filename: str) -> None:
    try:
        print(f"Accessing file '{filename}'")
        f: typing.IO[str] = open(filename)
        text = f.read()
        print("---\n")
        print(text)
        print("---")
        f.close()
        print(f"File '{filename}' closed")
    except (FileNotFoundError, PermissionError) as error:
        sys.stderr.write(f"[STDERR] Error opening file "
                         f"'{filename}': {error}\n")
        return

    print("\nTransform data:")
    print("---\n")
    new_text = text.replace("\n", "#\n")
    print(new_text)
    print("---")

    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    new_name = sys.stdin.readline().strip("\n")
    if new_name:
        try:
            print(f"Saving data to '{new_name}'")
            f2: typing.IO[str] = open(new_name, "w")
            f2.write(new_text)
            print(f"Data saved in file {new_name}")
            f2.close()
        except (FileNotFoundError, PermissionError) as error:
            sys.stderr.write("[STDERR] Error opening file "
                             f"'{new_name}': {error}\n")
            print("Data not saved.")
    else:
        print("Data not saved.")


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
    else:
        print("=== Cyber Archives Recovery & Preservation ===")
        read_file(sys.argv[1])


if __name__ == "__main__":
    main()
