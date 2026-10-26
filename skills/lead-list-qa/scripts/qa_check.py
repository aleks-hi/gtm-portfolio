#!/usr/bin/env python3
"""Lead list QA: flags common problems in a lead CSV. Never modifies the input."""
import argparse, csv, re, sys
from datetime import date, datetime
from urllib.parse import urlparse

FREE_MAIL = {"gmail.com", "hotmail.com", "outlook.com", "yahoo.com", "icloud.com", "live.com", "gmx.de", "web.de"}
EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[a-z]{2,}$", re.I)
DATE_FORMATS = ("%d.%m.%Y", "%d-%m-%Y", "%Y-%m-%d", "%d/%m/%Y")

GUESS = {
    "name": ["full name", "name"],
    "company": ["company", "organisation", "organization"],
    "email": ["email", "e-mail"],
    "phone": ["phone", "mobile", "telephone"],
    "website": ["website", "domain", "url"],
    "linkedin": ["personal linkedin", "linkedin url", "linkedin"],
    "status": ["lead status", "status"],
    "replied": ["replied", "reply"],
}

def detect(headers, overrides):
    m, low = {}, {h.lower().strip(): h for h in headers}
    for key, cands in GUESS.items():
        if key in overrides:
            m[key] = overrides[key]; continue
        for c in cands:
            hit = next((low[h] for h in low if h == c), None) or next((low[h] for h in low if c in h and "company linkedin" not in h), None)
            if hit: m[key] = hit; break
    m["dates"] = [h for h in headers if re.search(r"date|sent", h, re.I)]
    return m

def norm_li(u):
    u = (u or "").strip().lower().split("?")[0].rstrip("/")
    return re.sub(r"^https?://(www\.)?", "", u)

def domain(u):
    u = (u or "").strip().lower()
    if not u: return ""
    if "://" not in u: u = "http://" + u
    return (urlparse(u).netloc or "").removeprefix("www.")

def parse_date(s):
    for f in DATE_FORMATS:
        try: return datetime.strptime(s.strip(), f).date()
        except ValueError: pass
    return None

def check(rows, m, today):
    flags, seen_li, seen_mail = [], {}, {}
    prev_site, prev_company = "", ""
    def add(i, kind, msg): flags.append({"row": i, "check": kind, "issue": msg})
    for i, r in enumerate(rows, start=2):  # row 1 = header
        g = lambda k: (r.get(m.get(k, ""), "") or "").strip()
        li, mail, site, comp = norm_li(g("linkedin")), g("email").lower(), g("website"), g("company")
        if li:
            if li in seen_li: add(i, "duplicate", f"same LinkedIn as row {seen_li[li]}")
            else: seen_li[li] = i
        if mail:
            if mail in seen_mail: add(i, "duplicate", f"same email as row {seen_mail[mail]}")
            else: seen_mail[mail] = i
            if not EMAIL_RE.match(mail): add(i, "email", f"invalid format: {mail}")
            elif mail.split("@")[1] in FREE_MAIL: add(i, "email", "free-mail address")
            elif site and domain(site) and mail.split("@")[1] != domain(site) and not mail.split("@")[1].endswith("." + domain(site)):
                add(i, "email", f"email domain {mail.split('@')[1]} ≠ website {domain(site)}")
        ph = g("phone")
        if ph:
            digits = re.sub(r"\D", "", ph)
            if not (8 <= len(digits) <= 15): add(i, "phone", f"unlikely length: {ph}")
            elif not ph.strip().startswith("+") and not ph.strip().startswith("00"): add(i, "phone", f"no country code: {ph}")
        for col in m["dates"]:
            v = (r.get(col) or "").strip()
            if not v: continue
            d = parse_date(v)
            if d is None: add(i, "date", f"{col}: unreadable '{v}'")
            elif d > today: add(i, "date", f"{col}: in the future ({v})")
        if site and prev_site and domain(site) == domain(prev_site) and comp and prev_company and comp.lower() != prev_company.lower():
            add(i, "website", f"same website as row above but different company ({prev_company})")
        if site: prev_site, prev_company = site, comp
        rep, st = g("replied").lower(), g("status").lower()
        if rep in ("yes", "y", "true", "1", "ja") and st in ("new", ""):
            add(i, "status", "replied but lead status is still 'New'")
    return flags

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("csv"); ap.add_argument("--out", default="qa_report.csv")
    ap.add_argument("--map", action="append", default=[], help='key=Header, e.g. linkedin="Personal LinkedIn"')
    ap.add_argument("--today", help="override today's date (YYYY-MM-DD) for testing")
    a = ap.parse_args()
    overrides = dict(x.split("=", 1) for x in a.map)
    with open(a.csv, newline="", encoding="utf-8-sig") as f:
        rd = csv.DictReader(f); rows = list(rd); headers = rd.fieldnames or []
    m = detect(headers, overrides)
    today = date.fromisoformat(a.today) if a.today else date.today()
    flags = check(rows, m, today)
    with open(a.out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["row", "check", "issue"]); w.writeheader(); w.writerows(flags)
    rows_flagged = len({x["row"] for x in flags})
    by = {}
    for x in flags: by[x["check"]] = by.get(x["check"], 0) + 1
    print(f"Columns used: { {k: v for k, v in m.items() if v} }")
    print(f"Rows: {len(rows)} · Flagged rows: {rows_flagged} ({rows_flagged*100//max(len(rows),1)}%)")
    print(" · ".join(f"{k}: {v}" for k, v in sorted(by.items())) or "No issues found")
    print(f"Report: {a.out}")

if __name__ == "__main__":
    main()
