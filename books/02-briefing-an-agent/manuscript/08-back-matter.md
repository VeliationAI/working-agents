---
kind: back
title: Terms, and how to share this book
---

## Terms

**Acceptance test.** A line in the brief that says how a result will be judged. A good one can fail, and a tired stranger can apply it without redoing the work.

**Agent.** A model in a loop with a goal, a way to observe, a way to act, and a check, inside limits you set.

**Boundary.** What the loop may not do, and which tools it may use. Boundaries are written as a list, not a tone.

**Brief.** The one-page description of the job, the output, the tests, the boundaries, and the stop.

**Changelog.** A dated list at the bottom of a brief that records why each rule exists.

**Checklist.** The tests from a brief, rewritten as questions a reviewer can tick.

**Fixed and variable parts.** In a repeating brief, the fixed part stays the same each run. The variable part is filled in each time, usually by a person.

**Handback.** What the loop returns when it stops. Result, checks, unknowns, and sources.

**Harness.** The software that runs the loop around the model. It sends tool calls, stores the trace, and enforces limits.

**Prompt.** The instruction for a turn, built from the brief and from what the loop has seen so far.

**Standing note.** A preference or rule that applies across jobs. Short, dated, owned, and easy to delete.

**Stranger test.** Giving a draft brief to someone who does not know the job and collecting their questions without answering them.

**Stop.** The rule that ends a run: the tests pass, a required fact is missing, or the step limit is reached.

**Trace.** The record of a run. Each goal, observation, action, and check, in order.

**Unknown.** A legal answer. A claim the loop could not source, marked as such rather than filled in.

## What this book is claiming

It claims that the brief is the product, and that most bad runs are bad briefs.

It claims that the context you forget is the context that costs you, and that a stranger finds it faster than you do.

It claims that a test is worth writing only if someone tired can apply it.

It claims that a brief, a prompt, a standing note, and a checklist should be four views of one set of decisions, each written once.

It does not evaluate tools or models. It does not promise that a good brief removes the need for review. It makes the review smaller and possible.

## The rest of the series

Book 1. The Agent Loop. What an agent is, when to use one, and how the loop works.

Book 3. Tools and Permissions. Read, draft, and write. Least privilege. Secrets. Logs you can replay.

Book 4. Memory. The shelves, in practice. Retrieval. Rot, contradiction, and deletion.

Book 5. Agents at Work. Patterns for research, writing, operations, support, and software changes.

Book 6. When the Loop Goes Wrong. Traces, a small exam from real jobs, and what to do after a bad run.

Book 7. More Than One Agent. Handoffs, shared state, and the many times a single agent is the better design.

Book 8. Shipping an Agent. Cost, fallbacks, and putting a loop in front of people who did not build it.

Each one is meant to stay short, free, and paired with an audio reading of the same text.

## How to share this book

{{BOOK}} by {{AUTHOR}}, part of {{SERIES}}. Licensed under CC BY 4.0. {{LICENSE_URL}}

You may copy it, send it to a colleague, assign it, translate it, and teach from it. Give credit. Link the license. If you change the text, say what you changed, and do not imply that the author endorses the new version.

A credit line you can paste:

{{BOOK}}, by {{AUTHOR}}. {{SERIES}}, CC BY 4.0.

The contact link, for corrections and for the current edition: {{CONTACT}}

If you teach from this book in public, teach one idea at a time, and hand people the page. The filled briefs in chapter four are meant to travel on their own. The chapters are there for the moment a hand-off, a purchase, or a bad run needs a clearer head.
