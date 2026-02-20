#!/usr/bin/env python3
import os
import argparse
from datetime import datetime

# Configuration
TEMPLATE_FILE = "meeting_template.tex"
MAIN_FILE = "main.tex"


def create_meeting(date_str=None):
    # 1. Determine Date and Folder Name
    if date_str:
        try:
            dt = datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            print("Error: Date must be in format 'YYYY-MM-DD' (e.g., '2026-02-13')")
            return
    else:
        dt = datetime.now()

    folder_name = dt.strftime("%Y-%m-%d")
    readable_date = dt.strftime("%b %d, %Y")

    print(f"Creating meeting entry for: {readable_date} (Folder: {folder_name})")

    # 2. Check/Create Directory
    if os.path.exists(folder_name):
        print(f"Warning: Folder '{folder_name}' already exists.")
    else:
        os.makedirs(folder_name)
        print(f"  [+] Created directory: {folder_name}")

    # 3. Create main.tex from Template
    target_file = os.path.join(folder_name, "main.tex")
    if os.path.exists(target_file):
        print(f"  [!] File '{target_file}' already exists. Skipping creation to avoid overwrite.")
    else:
        if not os.path.exists(TEMPLATE_FILE):
            print(f"  [!] Error: Template file '{TEMPLATE_FILE}' not found!")
            return

        with open(TEMPLATE_FILE, "r") as f:
            content = f.read()

        content = content.replace("{Date}", f"{{{readable_date}}}")

        with open(target_file, "w") as f:
            f.write(content)
        print(f"  [+] Created file: {target_file}")

    # 4. Suggest update to root main.tex
    print("\nNext Steps:")
    print(f"1. Open '{target_file}' and fill in details.")
    print(f"2. Add the following to your '{MAIN_FILE}' before \\end{{document}}:")
    print(f"   \\chapter{{{readable_date}}}")
    print(f"   \\input{{{folder_name}/main}}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a new research meeting entry.")
    parser.add_argument(
        "date",
        nargs="?",
        help="Date in 'YYYY-MM-DD' format (e.g. 2026-02-13). Defaults to today.",
    )

    args = parser.parse_args()
    create_meeting(args.date)
