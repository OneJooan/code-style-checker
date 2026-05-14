# code-style-checker

Lightweight developer tooling designed to detect and auto-fix common formatting inconsistencies across codebases.

Built to simplify repetitive cleanup tasks and improve code consistency in small projects and automation workflows.

## Features

- Detects **tab indentation** (`[TAB]`)
- Detects **trailing spaces** (`[TRAILING SPACE]`)
- Detects **mixed indentation** (spaces + tabs on the same line) (`[MIXED INDENT]`)
- **Auto-fix mode** safely rewrites supported formatting issues in place
- Scans a single file or an entire directory recursively

## Supported File Types

- Python (`.py`)
- JavaScript (`.js`)
- PHP (`.php`)
- Markdown (`.md`)

## Installation

```bash
git clone https://github.com/OneJooan/code-style-checker.git
cd code-style-checker
pip install -e .
```

## Usage

```bash
# Scan current directory
style-checker

# Scan a specific file or directory
style-checker path/to/file.py
style-checker path/to/project/

# Detect and auto-fix issues
style-checker path/to/file.py --fix
```

## Example Output

```
[TAB] examples/example.py:5
[TRAILING SPACE] examples/example.py:8
[MIXED INDENT] examples/example.py:12
[DONE] Issues detected.
```

With `--fix`:

```
[TAB] examples/example.py:5
[TRAILING SPACE] examples/example.py:8
[FIXED] examples/example.py
[DONE] Scan completed with auto-fix enabled.
```

## Quick Start with Make

```bash
make install      # Install the package (editable)
make install-dev  # Install + dev dependencies (pytest)
make test         # Run the test suite
make check        # Scan the project for style issues
make fix          # Scan and auto-fix style issues
make clean        # Remove build/cache artifacts
```

## Running Tests

```bash
# With make
make test

# Manually
pip install pytest
pytest tests/
```

## Project Structure

```
code-style-checker/
├── checker/
│   └── style_checker.py   # Core logic
├── examples/              # Sample files with style issues
├── tests/
│   └── test_checker.py    # pytest test suite
├── Makefile
├── pyproject.toml
├── requirements.txt
└── README.md
```

## License

MIT

## Notes

This tool focuses on lightweight style consistency checks and is not intended to replace full linters or formatters such as:

- flake8
- black
- prettier
- PHP_CodeSniffer