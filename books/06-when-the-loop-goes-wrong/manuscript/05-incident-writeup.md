---
kind: chapter
title: Writing up an incident so the next brief contains the test
---

A bad run is over. The customer has been answered. The draft has been fixed. People are going back to their other work.

This is the moment when the lesson is most likely to be lost. Everyone knows what happened today. In three months, nobody will remember, and the same failure will return in a slightly different costume.

The write-up is how you keep the lesson. It is a short document with one purpose: to make sure the next brief contains the test that would have caught this.

## What counts as an incident

An incident is any run where the loop did something you did not want, and a person or a check noticed. Not only the dramatic ones.

Count the following.

- A wrong output that reached someone outside the team.
- A wrong output that a reviewer caught before it left. This is a near miss, and it is worth more than the real incident, because it was free.
- A write action that was outside the brief.
- A run that hit a step or cost limit without finishing.
- A handback that a reviewer could not trust without redoing the work.

Log the near misses. If you only write up the failures that hurt, you will learn only from the ones that got through. A near miss shows you what the review step is quietly absorbing. When a reviewer says "I fix that every week," you have found a missing test.

## The write-up is one page

If it is longer, nobody reads it, and nobody writes the next one. Use a fixed template so each one takes under an hour.

```
INCIDENT 2026-11-17-A

WHAT HAPPENED
One or two sentences. What the output was, and what it should
have been.

IMPACT
Who saw it, and what it cost. Include "caught in review" if so.

TRACE
Run id and where the trace is stored.
First wrong step, by step number.
Second wrong step, if there is one.

WHY THE LOOP COULD DO IT
What in the sources, tools, brief, or check made this possible.
Not "the model made a mistake." Name the thing in the system.

WHY NOTHING CAUGHT IT
Which check passed, and why that test was too weak, or what
test did not exist.

WHAT WE CHANGED
Each change, with its rung from the ladder: source, tool, check,
handback, brief, prompt.

THE TEST
The exact test line that would have caught this. Written so a
stranger could apply it. Pasted into the brief, and into the
exam card.

EXAM
Task card added: number and name.
Exam result before and after.

FOLLOW-UP
Owner, date, and what you will look at on that date.
```

Two sections carry most of the weight. "Why the loop could do it" and "The test."

## A filled example

```
INCIDENT 2026-11-17-A

WHAT HAPPENED
A draft reply to ticket T-5521 offered a full refund for a unit
delivered 45 days earlier. Current policy allows replacement or
repair within 30 days, and a refund only if no replacement is
available. Replacement stock was available.

IMPACT
Draft approved by the reviewer and sent. The customer replied
asking for the refund. Support honored it to avoid a dispute.
Cost: one refund, about 40 minutes of staff time.

TRACE
Run 2026-11-17-0932, stored under traces/2026-11/.
First wrong step: 5. Retrieval returned both the current and
the superseded version of section 4.2, with no effective dates
shown to the loop.
Second wrong step: 9. The check passed because the refund claim
appeared in a retrieved passage. It was the superseded one.

WHY THE LOOP COULD DO IT
The policy index still held the superseded text. The retrieval
tool returned passages without version metadata. The brief said
"the current policy" but gave no way to tell which passage was
current.

WHY NOTHING CAUGHT IT
Test 3 in the brief: "every claim appears in a retrieved passage."
It tested that a source existed and not that it was current. The
reviewer approved on the quality of the writing and the presence
of a section number.

WHAT WE CHANGED
Source: superseded policy text moved out of the index. (rung 1)
Tool: search_policy returns effective date with each passage.
  (rung 2)
Check: program test added, refund-claim-is-current. (rung 3)
Handback: cited section and effective date shown on line 1.
  (rung 4)
Brief: no change.
Prompt: no change.
A tweak, "NEVER offer a refund," was tried and reverted after it
broke two exam tasks.

THE TEST
Every refund or replacement claim in the draft must match the
latest effective version of the section it cites. If two versions
have the same effective date, stop and ask.

EXAM
Task 06 refund-after-window added. Tasks 11 and 12 added as
regression guards.
Before: 7 of 10 pass every run. After: 10 of 12.

FOLLOW-UP
Priya. 2026-12-01. Check the near-miss log for any other
superseded sections in the index. Audit the index for versions.
```

Read what the write-up does not say. It does not say the model hallucinated. In this run it did not. It quoted a passage that had been retrieved. The failure belonged to the index, the tool, and the check. A write-up that names the model as the cause gives you nothing to change.

## Blameless and specific

Write the incident about the system. "The reviewer approved a draft that quoted the wrong version" is a description of a process that depended on a tired person noticing a date. The fix is to put the date where the person cannot miss it, and to let a program check the rest. The reviewer did what the process invited.

Specific beats general. "The brief was unclear" is not a finding. "The brief said 'current policy' and the retrieval returned passages with no dates" is a finding.

## The test is the product

An incident write-up that ends with "we will be more careful" has failed. Care does not scale, and it does not survive a staffing change.

The write-up is finished only when the test exists in two places.

In the brief. The test line goes into the TESTS section of the one-page brief, in words a stranger can apply. If it is a program test, the brief names it and the harness runs it.

In the exam. A task card that reproduces the failure goes into the folder, with frozen inputs. It runs every time anything changes.

If the test lives in the write-up only, it will be read once. If it lives in the brief and the exam, it will be applied every run. Do not close the incident until both are done. A short checklist at the bottom of the template helps.

```
CLOSE CHECK
[ ] The test is in the brief, in the TESTS section.
[ ] A task card reproduces the failure, with frozen inputs.
[ ] The exam was run before and after the change.
[ ] The change is in the changelog with the incident id.
[ ] Someone who was not on the incident has read the write-up.
```

The last box matters. A write-up that has only been read by its author has not been tested. A colleague who can follow it and say "I see what the test is" is your grader.

## Timing and cadence

Write the draft within two working days. Details fade, and traces can be rotated out of storage. If your harness deletes traces after thirty days, copy the relevant trace into the incident folder on day one.

Review the log once a month, for thirty minutes.

- How many incidents and near misses this month?
- Which rung of the ladder did the fixes sit on? If most of them are in the prompt, your team is reaching for the wrong tool.
- Which tests fired in the exam and in production?
- Is any failure repeating? A repeat is a sign that the test was written but not applied, or that it was too narrow.
- What did reviewers fix by hand that never became an incident?

The last question finds the near misses nobody logged.

## Tell the people affected

If a customer or a colleague outside the team received a wrong output, tell them what was wrong and what you changed, in plain language. Keep it short. "A reply on 17 November quoted a superseded refund rule. We have corrected the reference material and added a check. If you were affected beyond the refund already issued, reply here."

You do not owe them a post-mortem. You owe them a clear statement and a way to reach a person. Book 8 returns to this under support.

## Try it this week

Write up the most recent bad run, near misses included, on one page. Use the template. Fill in "Why the loop could do it" without the word model. Paste the test line into the brief and write the task card. If you manage to do all of that in an hour, you have a process. If you do not, find out which section took the longest. That section is the part of your system you understand least.
