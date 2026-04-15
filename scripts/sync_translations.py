#!/usr/bin/env python3
"""
Detect outdated translations compared to the English version.

This script compares modification times between English and a selected
translation tree to identify which files need updating.

Usage:
    python scripts/sync_translations.py
    python scripts/sync_translations.py --lang pt-BR --verbose
"""

import argparse
import re
from datetime import datetime
from pathlib import Path

LANGUAGE_NAMES = {
    "en": "English",
    "vi": "Vietnamese",
    "zh": "Chinese",
    "uk": "Ukrainian",
    "pt-BR": "Brazilian Portuguese",
}


def is_translation_root(name: str) -> bool:
    """Return True for top-level locale-like directories."""
    return bool(re.fullmatch(r"[a-z]{2}(?:-[A-Z]{2})?", name))


def language_label(lang: str) -> str:
    """Return a short label for the selected language."""
    return lang.upper()


def language_name(lang: str) -> str:
    """Return a human-friendly name for the selected language."""
    return LANGUAGE_NAMES.get(lang, lang)


def check_translation_status(
    root_path: Path | None = None, lang: str = "vi", verbose: bool = False
) -> tuple[list[dict], list[dict]]:
    """
    Compare modification times between English and translated files.

    Args:
        root_path: Root directory of the repository (default: script parent parent)
        lang: Translation directory name to compare against
        verbose: Print detailed information

    Returns:
        List of outdated files with metadata
    """
    if root_path is None:
        root_path = Path(__file__).parent.parent

    # Get all English markdown files (excluding locale-like top-level directories)
    en_files = []
    for file_path in root_path.rglob("*.md"):
        if ".claude" in str(file_path):
            continue

        try:
            top_level = file_path.relative_to(root_path).parts[0]
        except IndexError:
            continue

        if is_translation_root(top_level):
            continue

        en_files.append(file_path)

    # Get all translated markdown files for the selected language
    lang_dir = root_path / lang
    lang_files = list(lang_dir.rglob("*.md")) if lang_dir.exists() else []

    # Build modification time mapping
    en_mtime = {f: f.stat().st_mtime for f in en_files}
    lang_mtime = {f: f.stat().st_mtime for f in lang_files}

    outdated = []
    not_translated = []

    for en_file, en_time in sorted(en_mtime.items()):
        # Find corresponding Vietnamese file
        try:
            rel_path = en_file.relative_to(root_path)
        except ValueError:
            # File is not relative to root (shouldn't happen)
            if verbose:
                print(f"⚠️  Skipping non-relative file: {en_file}")
            continue

        lang_file = lang_dir / rel_path

        if lang_file in lang_mtime:
            lang_time = lang_mtime[lang_file]
            if en_time > lang_time:
                outdated.append(
                    {
                        "file": rel_path,
                        "en_mtime": datetime.fromtimestamp(en_time),
                        "lang_mtime": datetime.fromtimestamp(lang_time),
                        "days_diff": (en_time - lang_time) / 86400,  # Convert to days
                    }
                )
        else:
            not_translated.append(
                {
                    "file": rel_path,
                    "status": "NOT_TRANSLATED",
                }
            )

    # Sort outdated by days difference (most outdated first)
    outdated.sort(key=lambda x: x["days_diff"], reverse=True)

    return outdated, not_translated


def format_outdated_table(outdated: list[dict], lang: str) -> str:
    """Format outdated files as a Markdown table."""
    if not outdated:
        return "✅ **No outdated translations found!** All files are up to date.\n"

    table = "### 🕰️ Outdated Translations (Need Update)\n\n"
    table += f"| File | Last EN Update | Last {language_label(lang)} Update | Days Behind |\n"
    table += "|------|----------------|----------------|-------------|\n"

    for item in outdated:
        file_path = str(item["file"])
        en_date = item["en_mtime"].strftime("%Y-%m-%d")
        lang_date = item["lang_mtime"].strftime("%Y-%m-%d")
        days = int(item["days_diff"])

        # Truncate long paths for display
        if len(file_path) > 50:
            file_path = "..." + file_path[-47:]

        table += f"| `{file_path}` | {en_date} | {lang_date} | 🔴 **{days} days** |\n"

    return table


def format_not_translated_table(not_translated: list[dict]) -> str:
    """Format not translated files as a Markdown table."""
    if not not_translated:
        return "\n✅ **All files have been translated!**\n"

    table = "\n### 📝 Not Translated Yet\n\n"
    table += "| File | Status |\n"
    table += "|------|--------|\n"

    for item in not_translated:
        file_path = str(item["file"])

        # Truncate long paths for display
        if len(file_path) > 60:
            file_path = "..." + file_path[-57:]

        table += f"| `{file_path}` | ⏳ **Not translated** |\n"

    return table


def format_summary(outdated: list[dict], not_translated: list[dict]) -> str:
    """Format summary statistics."""
    total_outdated = len(outdated)
    total_not_translated = len(not_translated)
    total_files = total_outdated + total_not_translated

    summary = "## 📊 Summary\n\n"
    summary += f"- **Total files needing attention:** {total_files}\n"
    summary += f"- **Outdated translations:** {total_outdated}\n"
    summary += f"- **Not translated yet:** {total_not_translated}\n"

    if total_outdated > 0:
        most_outdated = max(outdated, key=lambda x: x["days_diff"])
        summary += f"- **Most outdated file:** {most_outdated['file']} ({int(most_outdated['days_diff'])} days behind)\n"

    summary += "\n---\n\n"

    return summary


def update_translation_queue(
    root_path: Path, lang: str, outdated: list[dict], not_translated: list[dict]
) -> None:
    """
    Update the selected translation queue with current status.

    Note: This is a placeholder for future implementation.
    Currently, the queue is manually maintained.
    """
    pass


def main():
    parser = argparse.ArgumentParser(
        description="Check translation status against English version"
    )
    parser.add_argument(
        "--lang",
        type=str,
        default="vi",
        help="Translation directory to inspect (default: vi)",
    )
    parser.add_argument(
        "--verbose", "-v", action="store_true", help="Print detailed information"
    )
    parser.add_argument(
        "--root",
        "-r",
        type=Path,
        default=None,
        help="Root directory of repository (default: auto-detect)",
    )
    parser.add_argument(
        "--update-queue",
        action="store_true",
        help="Update TRANSLATION_QUEUE.md with current status (experimental)",
    )

    args = parser.parse_args()

    # Detect root path if not provided
    root_path = args.root or Path(__file__).parent.parent

    if args.verbose:
        print(f"🔍 Checking translations in: {root_path / args.lang}")
        print()

    # Check translation status
    outdated, not_translated = check_translation_status(
        root_path, lang=args.lang, verbose=args.verbose
    )

    # Print summary to console
    print("=" * 60)
    print(f"🌏 {language_name(args.lang)} Translation Status Report")
    print("=" * 60)
    print()

    total_outdated = len(outdated)
    total_not_translated = len(not_translated)

    if total_outdated == 0 and total_not_translated == 0:
        print("✅ **Congratulations!** All files are up to date.")
        print()
        return

    print(
        f"📊 Found {total_outdated} outdated + {total_not_translated} not translated files"
    )
    print()

    if args.verbose and outdated:
        print("🕰️  OUTDATED FILES (need update):")
        print("-" * 60)
        for i, item in enumerate(outdated, 1):
            print(f"{i}. {item['file']}")
            print(f"   EN: {item['en_mtime'].strftime('%Y-%m-%d %H:%M')}")
            print(
                f"   {language_label(args.lang)}: {item['lang_mtime'].strftime('%Y-%m-%d %H:%M')}"
            )
            print(f"   Behind by: {int(item['days_diff'])} days")
            print()

    if args.verbose and not_translated:
        print("📝 NOT TRANSLATED FILES:")
        print("-" * 60)
        for i, item in enumerate(not_translated[:20], 1):  # Limit to 20
            print(f"{i}. {item['file']}")

        if len(not_translated) > 20:
            print(f"... and {len(not_translated) - 20} more files")
        print()

    # Print Markdown-formatted report
    print("=" * 60)
    print("📄 Markdown Report (copy to TRANSLATION_QUEUE.md)")
    print("=" * 60)
    print()

    report = format_summary(outdated, not_translated)
    report += format_outdated_table(outdated, args.lang)
    report += format_not_translated_table(not_translated)

    print(report)

    # Optionally update TRANSLATION_QUEUE.md
    if args.update_queue and args.verbose:
        print("⚠️  --update-queue is experimental and not yet implemented")
        print("   Please manually update TRANSLATION_QUEUE.md")


if __name__ == "__main__":
    main()
