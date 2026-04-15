"""Tests for the translation sync helper."""

from __future__ import annotations

import os
from pathlib import Path

from sync_translations import check_translation_status, language_name


def write_markdown(path: Path, content: str, mtime: int) -> None:
    """Write a markdown file and pin its modification time."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    os.utime(path, (mtime, mtime))


def test_check_translation_status_supports_pt_br(tmp_path: Path) -> None:
    """Ensure pt-BR is compared against English and ignores other locales."""
    write_markdown(tmp_path / "README.md", "# English", 200)
    write_markdown(tmp_path / "01-topic" / "README.md", "# Topic", 200)
    write_markdown(tmp_path / "01-topic" / "details.md", "# Details", 200)

    write_markdown(tmp_path / "pt-BR" / "README.md", "# Português", 200)
    write_markdown(tmp_path / "pt-BR" / "01-topic" / "README.md", "# Tópico", 200)
    write_markdown(tmp_path / "pt-BR" / "01-topic" / "details.md", "# Detalhes", 50)

    # Other locale trees should not be treated as English source files.
    write_markdown(tmp_path / "vi" / "README.md", "# Tiếng Việt", 100)

    outdated, not_translated = check_translation_status(tmp_path, lang="pt-BR")

    assert [item["file"] for item in outdated] == [Path("01-topic/details.md")]
    assert not_translated == []


def test_language_name_known_locale() -> None:
    """Ensure friendly names are available for reporting."""
    assert language_name("pt-BR") == "Brazilian Portuguese"
