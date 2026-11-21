---
kind: chapter
title: A brief for a job you repeat every week
---

Every Friday at four, someone on your team spends ninety minutes writing the weekly operations note. They pull numbers from three dashboards, skim the incident channel, and write a page for leadership. It is dull, it is necessary, and it is the best first candidate for a loop you will ever find.

It is also the job where a brief earns its keep. A job you do once can survive a sloppy page. A job you do fifty-two times a year cannot, because the sloppiness repeats, and because nobody rereads a thing that has been fine for six weeks.

## What changes when a job repeats

A one-off brief describes a result. A weekly brief describes a result and a way to notice drift.

Three new problems appear.

**The inputs change.** Last week's numbers are not this week's. The brief must say where to look, not what the answer was.

**The context ages.** A standing note that was true in March may be wrong in June. The brief that worked then will quietly start producing a note with stale assumptions.

**The reader stops checking.** By the sixth good draft, the person approving it skims. This is human, and it is the real risk. A loop that is wrong on week twelve will be wrong in front of someone who trusts it.

The weekly brief is built to resist all three.

## Separate what is fixed from what varies

Write the brief in two parts. The fixed part stays the same every week. The variable part is filled in each run.

```
FIXED (edit rarely, review monthly)
JOB, OUTPUT, TESTS, BOUNDARIES, STOP, HANDBACK

VARIABLE (filled in each week)
- Week: 2026-11-16 to 2026-11-22
- Anything unusual this week: product launch Tuesday; billing
  outage Wednesday
- Anything to leave out: none
```

The variable block is short, and a person fills it in. It is where the human who knows about the launch tells the loop, in one line, what the dashboard cannot. The fixed part lives in a file, with a date at the top, that nobody edits casually.

## A filled weekly brief

```
JOB
Write the weekly operations note for leadership, covering the
previous Monday to Sunday. Finished means: a one-page note with
numbers and incidents, each traceable to its source.

OUTPUT
A document draft in the shared folder named "Ops note YYYY-MM-DD",
dated by the Friday. At most 450 words. Not an email.

TESTS
- Sections, in this order: headlines, numbers, incidents, next week.
- Numbers section has exactly these five metrics: signups, active
  accounts, support tickets opened, median first response time,
  uptime. Each with this week's value and last week's value.
- Each number has the dashboard name it came from.
- If a metric moved more than 15 percent from last week, the note
  says so in words, and says "cause unknown" if no cause is in the
  sources.
- Incidents lists every incident in the incident channel marked
  Sev1 or Sev2 during the week, with date as YYYY-MM-DD, duration,
  and a link.
- Anything not retrieved is listed under unknown. A missing
  number is written "not retrieved", never estimated.

BOUNDARIES
Do not post, email, or share the note. Do not edit any dashboard.
Do not speculate on causes beyond what the incident write-ups say.
Allowed tools: three dashboards (read), incident channel (read),
last week's note (read), save draft.

STOP
Stop when the draft is saved.
Stop if two or more dashboards cannot be read; save nothing and
report.
Stop after 15 steps.

HANDBACK
Draft link, the five metrics with sources, list of incidents,
unknowns.

APPLIED BY
A script checks sections, the five metric names, and word count.
The editor on duty opens two dashboards and confirms two numbers.
```

Look at what the brief does that a one-off might not. "Last week's note" is an allowed tool. It gives the loop a comparison point and a format to match, which keeps the note consistent from week to week without a long style description.

The 15 percent line forces the loop to flag movement rather than bury it. "Cause unknown" is a legal answer. That sentence will save someone from an invented explanation going to leadership.

## Make drift visible

Put a small check in the handback that exists only to catch change.

- **A diff against last week.** Ask the loop to say what is different in structure from last week's note. If the answer is "nothing", fine. If it is "I added a section on churn", you have caught the loop deciding something.
- **A source count.** "Sources read: 5 of 5 expected." When it says 4 of 5, the drop is in front of the reader, rather than hidden in smooth prose.
- **A date line.** "Data as of 2026-11-20 14:10." The reader knows how fresh the facts are.

These lines are boring, and that is their value. A boring line in the same place every week is something a skimming reader will actually see change.

## Review the brief on a schedule

The brief is a living page. Put a date on it, and put a review in the calendar.

- **After the first four runs**, read the four handbacks together. What did the editor fix by hand each week? Each repeated fix is a missing test.
- **Monthly**, reread the fixed part. Are the five metrics still the right five? Is a dashboard renamed? Has a source moved?
- **After any incident**, add the test that would have caught it. Write the date and one line of why, in a changelog at the bottom of the file.

```
CHANGELOG
2026-11-20  Added "not retrieved" rule after a missing uptime figure
            was estimated in the 2026-11-06 note.
2026-10-30  Raised metric movement flag from 10 to 15 percent.
```

The changelog is how the brief outlives the person who wrote it. In six months, someone will wonder why the rule exists. The line tells them.

Rotate the reviewer now and then, too. A fresh reader notices what the regular one has stopped seeing. Once a quarter, have someone redo one number from scratch. It takes fifteen minutes and tells you whether the trust is earned.

## What to do with this chapter

Choose one job you do on a rhythm. Write its brief in two parts, fixed and variable. Run it for four weeks in draft only, with a person approving each output.

After week four, read the four handbacks side by side, list every manual fix, and add tests for the repeated ones. Date the page, and put the next review in your calendar before you close the file.
