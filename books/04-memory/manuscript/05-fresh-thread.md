---
kind: chapter
title: When to start a fresh thread
---

It is Thursday afternoon. You have been working with an agent since Monday on a competitive analysis. The thread is long. On Monday the agent was sharp. Now it repeats a point you rejected on Tuesday, formats a table the way you told it not to on Wednesday, and has started calling your own product by the competitor's name.

You paste a correction. It apologizes and fixes the sentence. Two answers later, the error is back.

You do not have a stubborn agent. You have a long thread, and the thread is the problem.

A **thread**, in this book, is one continuous conversation or run with its accumulated trace. It carries everything said and done in it. That is its value, and in time its weakness.

## Why long threads decay

Three things happen as a thread grows.

**The goal gets diluted.** The brief was in view at the start, near the top. Now it is a small part of a very large context. Newer text, such as drafts, corrections, side questions, and tool output, dominates.

**Dead ends stay in view.** The approach you rejected is still there, along with the reasoning that led to it. A rejection is one sentence. The idea is three paragraphs. When the model weighs what to do next, the three paragraphs have more pull than the one sentence.

**Corrections pile up as patches.** "Actually, not that." "No, shorter." "Use the other table." The current intent is now the sum of twenty edits, and no single place states it. The model has to reconstruct your intent from the corrections, and it will sometimes reconstruct it wrong.

Some systems compress or summarize older parts of a thread automatically to fit a limit. That helps with size and can quietly drop a constraint you stated early. You do not control what the summary kept. Do not trust it with a boundary.

## Signs it is time

You do not need a number of messages. Watch for behavior.

- It repeats a point or approach you already rejected.
- It forgets an instruction from earlier that it followed before.
- It mixes up names, versions, or facts that it had straight.
- It answers a question you did not ask, from an older part of the thread.
- Your corrections have started to need corrections.
- You find yourself retyping the goal "to remind it."
- The run is making the same tool call again with the same arguments.

One of these can be noise. Two together, in the same thread, is a signal.

The cost side matters too. A long thread is slower and costs more per turn, since each step carries the whole history. That is a reason to be tidy, not a reason to hold on.

## When not to start fresh

A fresh thread is not free. It forgets everything, including what is useful.

Do not restart if:

- The task is nearly done and the next step depends on details in view.
- The problem is the brief and not the thread. A fresh thread with the same vague brief will fail the same way.
- The agent is in the middle of a multi-step action with state that only the trace holds, such as a half-finished batch. Restarting could repeat or skip work. Finish or stop it deliberately, and write down where it stopped.
- The issue is a single bad answer. Correct it, once, and see if it holds.

If correction after correction does not hold, the next move is a restart with a handoff. If correction holds, keep going.

## The handoff note

The skill is carrying what matters across the gap, and leaving the rest. You do that with a handoff note, written before you close the old thread.

A handoff note is a case file for the work so far, short enough to read in a minute. It is not a summary of the conversation. It is a statement of where the job stands.

```
HANDOFF NOTE
Date: 2026-11-19. From thread started 2026-11-16.

JOB
Competitive analysis of Northwind versus our Team plan,
for the Friday leadership review. Two pages, internal.

DONE
- Pricing comparison table, checked against both pricing
  pages on 2026-11-18.
- Feature comparison, drafted, not yet reviewed.

DECIDED
- Compare list prices only. Do not estimate discounts.
  (Decided by me, 2026-11-17.)
- Use the "seat-based" framing, not "per user."

REJECTED
- A market share section. No reliable source. Dropped.
- The "total cost over three years" model. Too many
  assumptions.

OPEN
- Northwind's support tiers: page unclear, need a second
  source.

CONSTRAINTS (unchanged)
- Internal use only. Dates as YYYY-MM-DD.
- Every claim cites a source or is marked unknown.

NEXT
Review feature comparison; resolve support tiers; write
the summary paragraph.
```

Look at what it contains. The job. What is finished. What was decided, and by whom. What was rejected, written as a decision. What is still open. The constraints that never changed. The next step.

Look at what it leaves out: the exploration, the apologies, the formatting back-and-forth, the three paragraphs about the market share idea.

## Write rejections as decisions

A rejected idea is the item most likely to return. A fresh thread has no memory of rejecting it, and a handoff that omits it invites the same suggestion on the first turn.

"Rejected: a market share section. No reliable source." That is a decision with a reason. It tells the new thread not to propose the idea, and tells you why, so you can reverse it when a source appears.

Compare "we talked about market share and decided against it," which is a story and not an instruction.

## Who writes the note

You can ask the agent to draft the note before you close the thread. That is a good use of the loop. It has read everything.

Then you read it, because the agent is summarizing a thread that has already confused it. Check three things.

1. **Decisions.** Does it say what you decided, and not what the agent suggested? Models sometimes promote their own proposals to decisions.
2. **Rejections.** Is everything you killed on the list?
3. **Facts.** Are the sources and dates intact? A handoff note that drops a date turns a checked fact into a rumor.

Edit it. Delete anything you cannot stand behind. Then start the new thread with the note and the original brief, in that order, and nothing else.

A prompt you can use for the draft:

```
Write a handoff note for a fresh start on this job.
Sections: JOB, DONE, DECIDED (with who decided and when),
REJECTED (with reason), OPEN, CONSTRAINTS, NEXT.
Include only what a new reader needs to continue.
Do not include discussion, apologies, or your own
suggestions that I did not accept.
If you are unsure whether something was decided, put it
under OPEN.
```

The last line is the safety. Anything uncertain goes to a place where you will look at it.

## Checking the new thread

Do not assume the handoff worked. Test it before you continue.

Ask the fresh thread two or three questions whose answers are in the note and one whose answer is a decision.

- "What are we comparing, and for whom?"
- "What have we ruled out, and why?"
- "What is the next step?"

If the answers match your note, proceed. If it improvises, the note is unclear, or it was not given priority. Fix the note, not the question.

Then give it the next step and watch the first few actions. A fresh thread working from a good note usually looks faster and calmer than the old one. If it does not, go back and check whether the brief is the real problem.

## Fresh threads for agents that run alone

Everything above is about a person watching a thread. An agent that runs for a long time without you has the same decay, with no one to notice.

For unattended runs, put the restart in the design.

- **Set a step limit.** The brief's stop rule handles this. "Stop after 30 steps and hand back" is a fresh-thread rule in disguise. The handback is the handoff note.
- **Checkpoint the case file.** At natural boundaries, such as after each source or each record, the loop writes what it learned to the case file and trims the trace.
- **Resume from the case file.** The next run, or the next segment, starts from the brief and the case file. It does not inherit the whole trace.
- **Bound the context.** If the harness lets you, keep a short window of recent steps in view, not everything.

A job split into short segments, each starting clean from a case file, is more reliable than one long loop. It also gives you more places to look and to stop. A run that fails at step 190 of 200 and cannot be resumed is a bad design. A run that fails at the end of segment six and resumes at segment seven is merely a bad afternoon.

## A habit worth keeping

Start fresh on purpose, at natural boundaries.

- A new deliverable.
- A change of audience.
- After a long tangent.
- At the end of the day, with a note.
- When you feel the urge to type "as I said before."

Writing the handoff note is also a check on yourself. If you cannot write down where the job stands in half a page, you do not know either. The thread may have been hiding that from both of you.
