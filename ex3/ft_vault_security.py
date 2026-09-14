#!/usr/bin/env python3

def secure_archive(filename: str,
                   action: str = "r",
                   content: str = "") -> tuple[bool, str]:
    try:
        with open(filename, action) as file:
            if action == "w":
                try:
                    file.write(content)
                    return (True, "Content successfully written to file")
                except OSError as error:
                    return (False, str(error))
            else:
                try:
                    text = file.read()
                    return (True, text)
                except UnicodeDecodeError as error:
                    return (False, str(error))
    except OSError as error:
        return (False, str(error))


def main() -> None:
    print("=== Cyber Archives Security ===\n")

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))
    print()

    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("no_perm.txt"))
    print()

    print("Using 'secure_archive' to read from a regular file:")
    print(secure_archive("ancient_fragment.txt"))
    print()

    print("Using 'secure_archive' to write previous content to a new file:")
    with open("ancient_fragment.txt", "r") as file:
        content = file.read()
    print(secure_archive("new_file.txt", "w", content))


if __name__ == "__main__":
    main()
