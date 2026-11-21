---
kind: chapter
title: A one-page memory policy
---

A new teammate joins the support team on Monday. By Wednesday they have added a note to the team's agent: "Customers on the Legacy plan always get a callback." It sounds helpful. Nobody approved it, nobody knows it is there, and by Friday the agent has promised callbacks to forty customers the team cannot call.

The cause was not a careless person. The team had no page that said who may add a note, where it goes, and when it is reviewed. So the new teammate did the obvious thing, and the system accepted it.

A **memory policy** is that page. It is short enough that people read it, specific enough that a new person can follow it on their first day, and honest enough that it describes what you really do. It does not describe an ideal. A policy nobody follows is worse than none, because it tells auditors and teammates that something is controlled when it is not.

This chapter gives you the page. It has a blank template, then a filled example, then notes on keeping it alive.

## What the page must answer

Eight questions, one line each where you can.

1. **Shelves.** Which shelves does this agent use, and where does each live?
2. **Writers.** Who may write to each shelf, and what may the agent write itself?
3. **Contents.** What belongs on each shelf, and what must never be there?
4. **Precedence.** When two items conflict, which wins?
5. **Clocks.** How long does each shelf keep things, and what makes it true?
6. **Review.** Who reviews what, and how often?
7. **Fresh starts.** When is a thread restarted, and what carries over?
8. **Deletion.** Who handles a request to delete, and what must it reach?

If your page does not answer one of those, someone will answer it by accident.

## The blank page

Copy this. Fill it in with the team that runs the agent, in one sitting, with the person who owns your records rules in the room or on a message thread. Then put it where the team will see it.

```
MEMORY POLICY
Agent / system: ______________________
Owner: ____________   Backup owner: ____________
Version: ____   Date: ____________   Next review: ____________

1. SHELVES AND WHERE THEY LIVE
Brief:           ______________________
Trace:           ______________________
Case file:       ______________________
Standing notes:  ______________________
Archive/index:   ______________________

2. WHO MAY WRITE
Brief:           ______________________
Trace:           ______________________
Case file:       ______________________
Standing notes:  ______________________
Archive/index:   ______________________
The agent may write by itself: ____________________
The agent may propose, a person approves: ____________
The agent may never write: ________________________

3. WHAT NEVER GOES IN MEMORY
(for example: payment details, health information,
secrets, credentials, personal data on the standing-notes shelf)
- ______________________
- ______________________

4. PRECEDENCE WHEN ITEMS CONFLICT
1. Hard boundaries
2. Today's brief
3. Case file decisions
4. Standing notes
5. Archive (informs, never overrides)
Changes to this order: ______________________
Overridden notes are reported in the handback: yes / no

5. CLOCKS
Trace:           kept ____ days; cleared by ____________
Case file:       kept ____ after close; cleared by ______
Standing notes:  reviewed every ____ months by ________
Archive:         per records schedule: ________________
Index:           rebuilt ____________; removals applied ____
Exports:         kept ____ days; location: ____________

6. STANDING NOTE FORMAT
Every note carries: text, reason, applies to, does not
apply to, owner, review-by date. Notes without these
are removed at the next review.

7. FRESH STARTS
Restart a thread when: ______________________
Carry over: brief, handoff note (job, done, decided,
rejected, open, constraints, next). Nothing else.
Unattended runs stop after ____ steps and hand back.

8. DELETION
Requests go to: ______________________
Deletion must reach: system of record, case files,
traces, index, exports, saved briefs, notes, and
outside providers where we send data.
Proof is kept: ______________________

SIGNED OFF BY (records or privacy owner): ____________
```

## A filled example

This is for a small support team. The numbers and names are examples, and your answers will differ. The shape is what to copy.

```
MEMORY POLICY
Agent / system: Support drafting agent
Owner: Dana Reyes   Backup owner: Sam Okoye
Version: 1.2   Date: 2026-11-12   Next review: 2027-02-12

1. SHELVES AND WHERE THEY LIVE
Brief:           Ticket template in the support tool.
Trace:           Harness log store, access limited to the
                 support lead and engineering.
Case file:       One note per ticket, in the ticket system.
Standing notes:  One page in the team wiki, titled "Agent
                 notes", 12 notes maximum.
Archive/index:   Closed tickets and in-force policies.
                 Index rebuilt nightly.

2. WHO MAY WRITE
Brief:           The agent's operator, per ticket.
Trace:           The harness only.
Case file:       The agent proposes entries with source and
                 date; the operator accepts or edits.
Standing notes:  Dana or Sam only, through a change request.
Archive/index:   Ticket system and the policy owner.
The agent may write by itself: the trace.
The agent may propose, a person approves: case file entries.
The agent may never write: standing notes, policies.

3. WHAT NEVER GOES IN MEMORY
- Card numbers, bank details, government IDs.
- Passwords, API keys, session links.
- Customer names or contact details on the standing-notes
  page.
- Health or legal information a customer volunteers.
  Redact before the case file is saved.

4. PRECEDENCE WHEN ITEMS CONFLICT
1. Hard boundaries (no sending, no refunds, no account
   changes without a person)
2. Today's brief
3. Case file decisions
4. Standing notes
5. Archive (informs, never overrides)
Overridden notes are reported in the handback: yes

5. CLOCKS
Trace:           kept 30 days; cleared by nightly job.
Case file:       kept 90 days after close; cleared by the
                 ticket system retention rule.
Standing notes:  reviewed every 3 months by Dana.
Archive:         closed tickets per company records schedule.
Index:           rebuilt nightly; removals applied on rebuild.
Exports:         kept 7 days; saved only in the "Reviews"
                 folder, which is purged weekly.

6. STANDING NOTE FORMAT
Every note carries: text, reason, applies to, does not
apply to, owner, review-by date. Notes without these
are removed at the next review.

7. FRESH STARTS
Restart a thread when: it repeats a rejected point, loses
an earlier instruction, or exceeds one working day.
Carry over: brief and handoff note. Nothing else.
Unattended runs stop after 25 steps and hand back.

8. DELETION
Requests go to: privacy@ (shared inbox), owner Sam.
Deletion must reach: ticket system, case files, traces,
index, exports, saved briefs, standing notes, and the
model provider's stored inputs where retention applies.
Proof is kept: deletion log, 2 years, no customer data.

SIGNED OFF BY: Priya Natarajan, records owner, 2026-11-12
```

## Why the page is built this way

A few choices deserve a defense.

**A limit on standing notes.** Twelve is arbitrary and useful. A cap forces a choice: to add a note, you must retire one. It is the cheapest protection against the pile. If you have more than a dozen, you probably have briefs and policies masquerading as notes. Move them.

**A named owner and a backup.** A policy owned by "the team" is owned by nobody. People change jobs. Naming a backup is the line that keeps the page alive through a holiday.

**Agent proposes, person approves.** This gives you most of the benefit of an agent that learns and none of the silent drift. The agent can say "this customer asked not to be called, add to case file?" A person confirms.

**A short "never" list.** It is easier to follow than a long "allowed" list. Keep it to things you can recognize on sight.

**Proof of deletion without customer data.** The log should say that a request was handled and when, not whom it was about in detail beyond a reference ID. Do not create a new copy of the thing you are deleting.

**A sign-off.** The records or privacy owner reads the page once. It is not a heavy process. It means someone responsible has seen what you do and had the chance to say "that retention is too long."

## Keeping the page true

A policy ages as quickly as a standing note. Give it a review date and put three tests in the review.

1. **Read it against practice.** Pick one ticket from last week. Can you find the brief, the case file, and the trace, where the policy says they are?
2. **Test a clock.** Pick a trace from before the retention window. Is it gone?
3. **Test the shelf.** Read the standing notes. Does every one carry the six fields? Is there any customer data?

Any failure goes on a list with an owner. If the policy and practice disagree, change one of them. Do not leave both as they are.

Also review after an incident. When an agent says something wrong because of what it remembered, the write-up belongs to the memory policy as much as to the brief. Which shelf held the bad item? Who wrote it? What on the page should have caught it? Add that line.

## If you are a team of one

You can use the same page. Fill it in for yourself. Your answers will be shorter. "Owner: me. Backup: none. Standing notes: a file called notes.txt, twelve lines, I read it on the first of the month."

The page is still worth writing, for a selfish reason: in six months you will not remember what the agent has been told. The page is the way you find out.

## What the policy cannot do

A policy does not make a note true. It does not catch a stale document. It does not stop someone pasting a customer's card number into a chat in a hurry.

It does two modest things. It makes the choices visible, so they can be argued with. And it gives you a standard to measure drift against, so you notice when practice slides.

That is enough. Most memory failures come from an unspoken decision. Say it on one page, and you have removed most of them.
