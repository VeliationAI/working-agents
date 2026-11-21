---
kind: chapter
title: Research, support, and a software change
---

You have the five questions, the stranger test, and the tests a tired person can apply. Here are three jobs, each with a full brief. They are different on purpose. One reads and composes. One drafts for a customer. One prepares a change to code.

Do not copy the wording. Notice where each brief spends its lines. The research brief spends them on sources. The support brief spends them on what must never be said. The software brief spends them on what must not be touched.

## Job one: a research brief

Your product manager needs to decide whether to add single sign-on. She does not need a market report. She needs to know what customers have asked for, in their own words, so she can bring it to Thursday's planning meeting.

```
JOB
Find out whether customers have asked for single sign-on (SSO) in the
last six months, and what they said. Finished means: a list of
requests with who asked, when, and the exact words, plus a count.

OUTPUT
A one-page document draft titled "SSO requests, last six months".
Not a recommendation. Not a market overview.

TERMS
- "Request": a message in which a customer asks for SSO, SAML, or
  login through their company identity provider.
- "Customer": an account in the CRM, not a prospect.

TESTS
- Sections: count, requests, gaps.
- Count is a number, and equals the number of rows in the requests
  list.
- Each request has account name, date as YYYY-MM-DD, source link, and
  a direct quote of at most 40 words.
- Quotes are copied, not paraphrased. Open any two sources and check
  the quote appears.
- Only requests from the last six months from today.
- Anything not found or not readable is listed under gaps.

BOUNDARIES
Do not contact customers. Do not summarize sentiment or guess
intent.
Allowed tools: support inbox (read), CRM notes (read), sales call
notes folder (read).
No write actions except saving the draft document.

STOP
Stop when all three sources have been searched with at least two
search phrasings each (SSO, SAML, "single sign").
Stop if a source cannot be opened; list it under gaps.
Stop after 20 steps.

HANDBACK
Document first, then gaps, then list of searches run and results
per source.
```

Look at what the brief refuses to do. "Not a recommendation" protects the product manager's decision. "Quotes are copied, not paraphrased" turns the main risk, a smoothed-over summary, into a testable rule. The count must match the rows, which is a quick presence test a script can run.

The stop rule asks for two phrasings per source. Without it, a loop that searches "SSO" once and finds nothing could report a count of zero, and zero would be believed.

## Job two: a support brief

A customer writes in angry. Their invoice shows a charge after they cancelled. You want a first-draft reply for the support agent to review. The loop will not send anything.

```
JOB
Draft a reply to the customer in ticket {ticket_id} about a charge
after cancellation. Finished means: a draft reply the support agent
can edit and send, plus a short internal note on what the records
show.

OUTPUT
Two items, saved as drafts in the ticket tool.
1. Customer reply, at most 150 words.
2. Internal note, at most 100 words, labeled "Internal. Do not send."

TERMS
- "Cancelled": the subscription status is "cancelled" with a date.

TESTS
- Reply states the cancellation date and the charge date, both
  as written in billing, copied exactly.
- Reply does not promise a refund, a timeline for a refund, or any
  amount. Refund decisions belong to a person.
- Reply does not name any other customer, any internal tool, or any
  competitor.
- Reply apologizes once, in one sentence, and does not blame the
  customer.
- Internal note lists what billing shows: dates, amounts, status.
  Anything not found says "unknown".
- No exclamation marks.

BOUNDARIES
Do not send. Do not change any billing record. Do not issue,
promise, or hint at a credit.
Allowed tools: ticket tool (read, save draft), billing (read).
Stop and ask the support agent if the account is flagged "dispute"
or "legal hold".

STOP
Stop when both drafts are saved.
Stop if billing has no record for this account; say so in the
internal note and write no reply.
Stop after 10 steps.

HANDBACK
Say which two drafts were saved, which facts came from billing, and
what is unknown.
```

The most important line is the one that is not obvious: "does not promise a refund." A fluent, kind reply to an angry customer will, left alone, offer a refund. That is a business decision. It is written into the tests as a failure, which means a tired agent can check for it in seconds.

Note the two outputs. The internal note keeps the loop's reasoning where the support agent can see it and the customer cannot. Note also the flagged-account stop. That is invisible context from the previous chapter, turned into a line.

## Job three: a software change

A developer wants a small bug fixed. A date picker shows the wrong day for users in time zones behind UTC. She wants a proposed change, with a test, that she can review. She does not want the loop to merge anything.

```
JOB
Prepare a fix for issue #{issue_number}: the date picker shows the
previous day for users behind UTC. Finished means: a branch with a
failing test that reproduces the bug, a change that makes it pass, and
the full test suite green.

OUTPUT
A branch named fix/date-picker-timezone and a pull request draft.
The description states cause, change, and how it was verified.

TESTS
- A new test fails on the original code and passes on the new code.
  Show both results.
- The full existing test suite passes. Show the command and result.
- Change touches only files under src/components/datepicker/ and its
  tests. No other file is edited.
- No new dependency is added.
- Diff is under 60 changed lines excluding tests.
- Description states what was NOT verified, such as browsers not run.

BOUNDARIES
Do not merge. Do not push to main. Do not change CI configuration,
lockfiles, or anything under src/billing/.
Allowed tools: read repository, edit files on the branch, run tests,
open a draft pull request.
Ask first before editing a file outside the datepicker folder.

STOP
Stop when the tests pass, or after 3 failed attempts at the same
approach; then report the attempts and stop.
Stop after 25 steps.
If the test cannot reproduce the bug, stop and say so. Do not fix a
bug you could not reproduce.

HANDBACK
Pull request link, the failing-then-passing test output, the full
suite result, and a list of what you did not check.
```

This brief is almost all boundaries. The loop has wide tools: it can edit files and run commands. The page narrows what that means. "Touches only these files" is a test a script applies from the diff. "Do not fix a bug you could not reproduce" blocks the most tempting shortcut, which is a plausible change to code that was never broken in the way described.

The "three failed attempts at the same approach" stop is Book 1's stuck loop, written into the brief. Without it the loop will try a fourth, fifth, and sixth variation, each with more confidence.

## What the three have in common

Each job has a finish line a stranger can check: a count that matches rows, drafts that exist, a test that goes from red to green. Each has a "never" that came from a real risk. Each names its tools at the narrowest level. Each stops on a missing fact rather than guessing, and each handback says what is unknown.

They differ in where the risk is. Research risks smoothing. Support risks overpromising. Software risks overreach. Your brief's heaviest section is the one that guards your job's biggest risk. Find it before you write the rest.

## What to do with this chapter

Pick the job closest to yours. Copy the structure, not the sentences. Write down the single worst thing the loop could do on your job. Then check that the page has a test or a boundary that catches it. If it does not, that is the first line to add.
