# code-style-checker

A lightweight CLI tool for detecting and auto-fixing basic code style issues in Python, JavaScript, PHP, and Markdown files.

## Features

- Detects **tab indentation** (`[TAB]`)
- Detects **trailing spaces** (`[TRAILING SPACE]`)
- Detects **mixed indentation** (spaces + tabs on the same line) (`[MIXED INDENT]`)
- **Auto-fix mode** rewrites files in place
- Scans a single file or an entire directory recursively

## Supported File Types

`.py` · `.js` · `.php` · `.md`

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
