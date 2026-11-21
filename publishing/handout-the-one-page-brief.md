---
kind: handout
title: The one-page agent brief
---

Fill this in before you open a tool, hire a vendor, or let a system send anything. If a line is hard to fill, the job is not ready to delegate.

An AI agent is a model in a loop. The loop has a goal, a way to see the situation, a way to act, and a way to decide whether the goal is met. A chatbot answers and stops. A workflow follows steps you fixed in advance. Use an agent when the next step depends on what the case contains.

## Copy this page

```
JOB
What finished work looks like, in one or two sentences.

OUTPUT
The artifact. Length, format, and where it should land.
A draft, a file, or a ticket. Name the destination.

TESTS
- Sections or fields that must be present
- Format rules, such as dates written YYYY-MM-DD
- Every factual claim has a source, or is marked unknown

BOUNDARIES
Do not: ...
Allowed tools: ...
Write actions that need approval before they run: ...

STOP
Stop when the tests pass.
Stop when a required fact cannot be retrieved.
Stop after this many steps: __
Do not guess in order to fill a gap.

HANDBACK
Return the result, the checks, the unknowns, and the sources.
```

## A filled example

```
JOB
Prepare me for a 30-minute renewal call with Acme on Thursday.

OUTPUT
A briefing of at most two pages, as a document draft. Not an email.

TESTS
- Sections: what they bought, open support issues from the last
  90 days, unpaid invoices, three questions for me to ask.
- Dates written as YYYY-MM-DD.
- Every fact has a source line, or the value unknown.
- No competitor is named.

BOUNDARIES
Do not contact Acme or anyone outside the company.
Allowed tools: customer records (read), support inbox (read),
billing (read).
No write actions.

STOP
Stop after those three sources have been checked, or after 12 steps.
Incomplete is acceptable. Invented is not.

HANDBACK
Brief first, then unknowns, then sources.
```

## How to use it this week

1. Pick a recurring brief you already write by hand.
2. Fill the page with that job. Leave the write tools off.
3. Run it once. Grade the handback against the tests, not against how fluent it sounds.
4. Add a test for every place you had to reopen a source yourself.
5. Keep sending, paying, deleting, and deploying on the person side until the drafts have been dull and correct.

The full argument is the free book The Agent Loop, Working Agents, Book 1. Same words in PDF and audio.
