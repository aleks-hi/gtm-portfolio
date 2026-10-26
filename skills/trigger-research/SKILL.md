---
name: trigger-research
description: Research a B2B prospect (person + company), find a current, sourced reason to reach out, and draft a short personal outreach message that passes a QA check before a human sends it. Use whenever the user asks to research a lead, prospect or account, find a trigger or buying signal, prep outreach, or write a first, second or third LinkedIn or email message to a named person or company, even if they don't say "trigger".
---

# Trigger research → message → QA

Turn one prospect into a sourced trigger, a draft message and a pass/fail QA result. A human always sends the message; this skill never sends anything.

## Input

Ask only for what's missing:
- **Person:** name, role, company (a LinkedIn URL is enough)
- **What we sell:** one line, plus the problem it solves
- **Touch:** 1st, 2nd or 3rd message (default: 1st)
- **Channel and language:** LinkedIn or email; the prospect's working language
- For a 2nd or 3rd message: the earlier messages

## Step 1: Research

Search for events from the **last 90 days**. Check these sources in order, and stop once two usable triggers are found:

1. The company's own news, blog or press page
2. Its careers page and job postings
3. The person's recent LinkedIn activity or a role change
4. Funding, acquisition, partnership or expansion news
5. Product launches or major releases

For every finding, record the **date, source URL and one factual sentence**. Never record something you couldn't open and check yourself.

## Step 2: Pick the trigger

Score each finding:

| Criterion | Points |
|---|---|
| Within 30 days | 2 (31–90 days: 1) |
| Links directly to the problem we solve | 2 |
| About the person, not only the company | 1 |
| Source is the company or the person | 1 |

Use the highest score. If nothing scores 3 or more, **stop and return "No usable trigger"** with what was found. A weak trigger produces a generic message, and that lead belongs in a standard sequence instead.

## Step 3: Situation in one line

Describe where the company is right now in one line: early product, growing, scaling or consolidating, with the evidence. This line is for the caller, not for the message.

## Step 4: Draft

Follow `references/writing-rules.md`. By touch:
- **1st:** open with the trigger → connect it to a likely problem → one easy question
- **2nd:** a new angle (a different trigger, or a consequence of the first one); never "just following up"
- **3rd:** 2 sentences at most, low pressure, easy to close the loop

## Step 5: QA (mandatory)

Check the draft against every item in this list. If any check fails, rewrite and check again. After two failed rewrites, return the draft with the failures listed.

- [ ] Every fact in the message appears in the research table with a source
- [ ] 4 sentences or fewer (3rd touch: 2 or fewer)
- [ ] Opens with the prospect, not with "I" or "we"
- [ ] Exactly one question, at the end
- [ ] No banned phrases (see the writing rules)
- [ ] No hours, rates, prices or competitor names
- [ ] Written in the prospect's working language
- [ ] Reads naturally aloud: no list-like sentences, no stacked adjectives

## Output

```
## <Person>, <Role> at <Company>

**Trigger:** <one sentence> (<date>, <source URL>)
**Situation:** <one line> (for the caller)

**Draft (<touch>, <channel>):**
<message>

**QA:** PASS | FAIL: <failed checks>

**Research log**
| Date | Finding | Source | Score |
```

Write the draft unsigned.
