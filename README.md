# Data Curation Agent Research Log

This repository contains the ongoing research log, meeting notes, and experimental findings for the Data Curation Agent project. The document is built using **LaTeX** and features a custom styling package for consistent, high-quality presentation.

## Features

-   **Automated Meeting Logs**: Create new entries easily using `create_meeting.py`.
-   **Custom LaTeX Styling**: tailored `styles/meeting.sty` with:
    -   Professional "Cool Slate" Task Boxes.
    -   "Success Green" Key Findings Sections.
    -   5-Argument Meeting Headers (Date, Commit, Link, Summary, Housekeeping).
-   **Custom Section/Subsection Styles**: Blue-themed headers via `styles/section.sty`.
-   **Research Boxes**: Motivation, findings, and note boxes via `styles/colored_box.sty`.

## Quick Start

### Prerequisites
-   LaTeX (TeX Live or similar) with `latexmk`.

### Automation
Start a new week's log entry:
```bash
python create_meeting.py Feb_14
```

### Build Commands
```bash
make pdf    # Compile the main LaTeX document (main.pdf)
make clean  # Remove build artifacts
```
