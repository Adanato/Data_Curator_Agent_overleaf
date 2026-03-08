# CLAUDE.md — Data Curation Agent Research Log

## Project

LaTeX research log for the Data Curation Agent project (ReDS Lab, Virginia Tech, PI: Ruoxi Jia). Weekly meeting entries documenting experiments, baselines, and system design for an agentic data curation pipeline.

## Structure

```
main.tex               — root document, \input per meeting chapter
meeting_template.tex    — skeleton for new meeting notes
slides_template.tex     — skeleton for optional meeting slides
styles/meeting.sty      — custom commands (meetingheader, keyfindings, meetingtasks)
styles/slides.sty       — assertion-evidence Beamer style (aeframe, findingframe, taskframe)
YYYY-MM-DD/main.tex    — each meeting's notes (report format)
YYYY-MM-DD/slides.tex  — optional slide deck for that meeting (Beamer PDF)
references.bib          — bibliography
```

## Creating a New Meeting Entry

1. Create folder: `YYYY-MM-DD/`
2. Copy `meeting_template.tex` → `YYYY-MM-DD/main.tex`
3. Add `\chapter{Mon DD, YYYY}\n\input{YYYY-MM-DD/main}` to `main.tex`

## Creating Slides (Optional)

Only when the advisor requests a slide deck for a specific meeting.

1. Copy `slides_template.tex` → `YYYY-MM-DD/slides.tex`
2. Write notes in `main.tex` first — slides extract from notes, not the other way around
3. Each `\section` in the notes → one `\aeframe{sentence assertion}{visual evidence}` in slides
4. Each `\keyfindings` item → one `\findingframe`
5. `\meetingtasks` → one `\taskframe`
6. Compile: `pdflatex YYYY-MM-DD/slides.tex`

### Slide commands (styles/slides.sty)

```latex
\aeframe{Sentence headline stating the takeaway}{body with figure/table/diagram}
\findingframe{One-sentence finding}{supporting evidence}
\taskframe{\item Task 1 \item Task 2}
```

### Slide rules (Alley — assertion-evidence)

- Every slide headline is a **complete sentence** stating the takeaway — not a topic label
- Slide body is **visual evidence** (figure, table, diagram) — not bullet lists
- If you must use text, max 3 short items. Prefer a visual.
- Read all headlines in sequence — they should tell the story without the bodies

## Writing Style — MANDATORY

Claude Code tends toward verbose, hedging, corporate prose. This project follows two specific frameworks. Apply them without being told.

### Concision Rules

- **Short sentences.** Max 20 words when possible. Cut filler ("it is important to note that", "in order to", "it should be noted", "we can observe that"). Say it directly.
- **Characters as subjects, actions as verbs.** "The agent skips tools" not "Tool skipping behavior was observed." "We measured" not "Measurements were taken."
- **No throat-clearing.** Don't open paragraphs with "In this section we discuss..." — just discuss it.
- **Old before new.** Start sentences with what the reader already knows; end with the new information.
- **One idea per sentence.** If a sentence has two clauses joined by "and", split it.

### Argument Structure (Craft of Research — Booth et al.)

Every meeting section should have an implicit argument:

```
Problem (condition + cost) → Claim → Reasons → Evidence → Acknowledgments
```

- **Problem**: What doesn't work, and why it matters. State the cost.
- **Claim**: One-sentence takeaway. Must pass the opposite test — if the opposite is absurd, the claim is trivially obvious.
- **Reasons**: The analytical "because" — your interpretation, not data.
- **Evidence**: Experimental results, tables, logs. Let data speak.
- **Acknowledgments**: State limitations upfront. An argument without them seems thin.

### Key Findings (keyfindings box)

Each `\item` in `\keyfindings{}` should be a **sentence-assertion** (Alley):
- Complete sentence stating the takeaway, not a topic label
- Bad: "Agent performance comparison"
- Good: "Neither baseline agent performed web research despite having access, so all quality formulas are improvised LLM intuition"

### Figures and Tables

- Every figure/table needs a **sentence caption** that states the finding, not just the content
- Bad: `\caption{Agent runtime comparison}`
- Good: `\caption{Claude spent 4x longer than Codex but used benchmark-aware scoring}`
- Tables: max ~5 columns. If wider, split or move to appendix.

### Discussion and Log Analysis

- Lead with the finding, then the evidence. Not "We ran X and observed Y" but "Y happened. Here's how we know: X."
- Number failure modes and findings explicitly (enumerate). Reviewers and advisors skim — numbered items get read.
- When comparing agents/approaches, use a comparison table. Prose comparisons are hard to parse.

## Custom LaTeX Commands

```latex
\meetingheader{Date}{git-branch}{\meetinglinks{...}}{Summary}{Housekeeping}
\keyfindings{ \item ... }
\meetingtasks{ \item \todo{...} }
\e{emoji_name}            % inline emoji from emojis/ folder
```

## What NOT to Do

- Don't add boilerplate introductions ("In this meeting we will discuss...")
- Don't hedge with "may", "might", "could potentially" — state what happened
- Don't summarize what you're about to say, then say it, then summarize what you said
- Don't use passive voice unless the actor is genuinely unknown
- Don't write paragraphs longer than 5 sentences
- Don't add subsections unless the section exceeds one page
