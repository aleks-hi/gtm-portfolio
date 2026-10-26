---
name: lead-list-qa
description: Check a lead or contact list (CSV, or exported from Google Sheets or Excel) for problems before it's used for outreach or imported into a CRM. It finds duplicates, dates in the future or in the wrong format, invalid emails and phone numbers, websites that don't match the company, and replied leads still marked "New". Use whenever the user wants to clean, check, validate, dedupe or QA a lead list, call list or prospect sheet, or before importing a list into HubSpot or another CRM.
---

# Lead list QA

Run deterministic checks with `scripts/qa_check.py`, then review the flags with judgement. The script never changes the source file.

## Step 1: Get the file

Accept a CSV, or export the sheet or workbook to CSV. Show the column headers and map them to the checks:

| Check needs | Typical headers |
|---|---|
| name | Name, Full name, First + Last |
| company | Company, Organisation |
| email | Email, E-mail |
| phone | Phone, Mobile, Company phone |
| website | Website, Domain |
| linkedin | LinkedIn, Personal LinkedIn |
| dates | any column with "date" or "sent" in its header |
| status / replied | Lead status, Status, Replied |

If a mapping is unclear, ask once and confirm the answer.

## Step 2: Run the checks

```bash
python scripts/qa_check.py leads.csv --out qa_report.csv
```

Pass `--map key=Header` for any header the script can't detect itself, for example `--map linkedin="Personal LinkedIn"`.

## Step 3: Review, don't auto-fix

For each flag, decide whether it is:
- **Fix:** an obvious error (a year typed as 2072; a website that belongs to the row above)
- **Check:** needs a human (two people with the same name at one company)
- **Ignore:** a false positive (a free-mail address used on purpose)

Never delete rows and never overwrite the source. Return the report plus a short summary:

```
Rows: <n> · Flagged: <n> (<%>)
Duplicates: <n> · Dates: <n> · Email: <n> · Phone: <n> · Website: <n> · Status: <n>
Top 3 fixes: ...
```

## Why these checks

Each check targets an error that is common in hand-built lead lists:
- Duplicates are matched on LinkedIn URL or email, never on name alone, because names are spelled in many variants.
- Date typos (a future year, swapped day and month) break follow-up timing.
- A website or company LinkedIn copied from the row above silently attaches the wrong company.
- "Replied" leads still marked "New" make every report wrong.
