#!/usr/bin/env python3

from pathlib import Path
import argparse

TARGET_EXTENSIONS = [".php", ".py", ".js", ".md"]


def check_file(filepath, auto_fix=False):

    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()

    except Exception as e:
        print(f"[ERROR] Cannot read file: {filepath}")
        print(f"        {e}")
        return False

    issues_found = False
    updated_lines = []

    for line_number, line in enumerate(lines, start=1):

        original_line = line
        modified_line = line

        if "\t" in line:
            print(f"[TAB] {filepath}:{line_number}")
            issues_found = True
            if auto_fix:
                modified_line = modified_line.replace("\t", "    ")

        if modified_line.rstrip("\n").endswith(" "):
            print(f"[TRAILING SPACE] {filepath}:{line_number}")
            issues_found = True
            if auto_fix:
                modified_line = modified_line.rstrip(" \n") + "\n"

        stripped = original_line.lstrip()
        leading_whitespace = original_line[:len(original_line) - len(stripped)]

        if " " in leading_whitespace and "\t" in leading_whitespace:
            print(f"[MIXED INDENT] {filepath}:{line_number}")
            issues_found = True

        updated_lines.append(modified_line)

    if auto_fix and updated_lines != lines:

        try:
            with open(filepath, "w", encoding="utf-8") as f:
                f.writelines(updated_lines)

            print(f"[FIXED] {filepath}")

        except Exception as e:
            print(f"[ERROR] Cannot write file: {filepath}")
            print(f"        {e}")

    return issues_found


def process_path(path, auto_fix=False):

    path = Path(path)

    if not path.exists():
        print(f"[ERROR] Path does not exist: {path}")
        return False

    if path.is_file():
        if path.suffix in TARGET_EXTENSIONS:
            return check_file(path, auto_fix)
        return False

    issues_found = False

    for file in path.rglob("*"):
        if file.is_file() and file.suffix in TARGET_EXTENSIONS:
            if check_file(file, auto_fix):
                issues_found = True

    return issues_found


def main():

    parser = argparse.ArgumentParser(
        description="Lightweight code style checker"
    )

    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="File or directory to scan"
    )

    parser.add_argument(
        "--fix",
        action="store_true",
        help="Automatically fix basic issues"
    )

    args = parser.parse_args()

    issues_found = process_path(args.path, auto_fix=args.fix)

    if not issues_found:
        print("[OK] No style issues detected.")
    elif args.fix:
        print("[DONE] Scan completed with auto-fix enabled.")
    else:
        print("[DONE] Issues detected.")


if __name__ == "__main__":
    main()
