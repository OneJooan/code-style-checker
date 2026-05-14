from pathlib import Path
from checker.style_checker import process_path


def create_temp_file(tmp_path, filename, content):

    file_path = tmp_path / filename

    file_path.write_text(content)

    return file_path


def test_detect_tabs(tmp_path, capsys):

    file_content = "def hello():\n\tprint('tab detected')\n"

    test_file = create_temp_file(
        tmp_path,
        "tabs.py",
        file_content
    )

    process_path(test_file)

    captured = capsys.readouterr()

    assert "[TAB]" in captured.out


def test_detect_trailing_spaces(tmp_path, capsys):

    file_content = "print('hello')    \n"

    test_file = create_temp_file(
        tmp_path,
        "trailing.py",
        file_content
    )

    process_path(test_file)

    captured = capsys.readouterr()

    assert "[TRAILING SPACE]" in captured.out


def test_auto_fix_tabs(tmp_path):

    file_content = "def hello():\n\tprint('fix me')\n"

    test_file = create_temp_file(
        tmp_path,
        "fix_tabs.py",
        file_content
    )

    process_path(test_file, auto_fix=True)

    updated_content = test_file.read_text()

    assert "\t" not in updated_content


def test_auto_fix_trailing_spaces(tmp_path):

    file_content = "print('hello')    \n"

    test_file = create_temp_file(
        tmp_path,
        "fix_spaces.py",
        file_content
    )

    process_path(test_file, auto_fix=True)

    updated_content = test_file.read_text()

    assert updated_content == "print('hello')\n"


def test_clean_file(tmp_path, capsys):

    file_content = (
        "def clean():\n"
        "    print('clean file')\n"
    )

    test_file = create_temp_file(
        tmp_path,
        "clean.py",
        file_content
    )

    process_path(test_file)

    captured = capsys.readouterr()

    assert "[TAB]" not in captured.out
    assert "[TRAILING SPACE]" not in captured.out