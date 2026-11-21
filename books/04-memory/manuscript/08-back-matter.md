---
kind: back
title: Terms, and how to share this book
---

## Terms

**Archive.** Old tasks, tickets, documents, and policies. Searchable when the goal says the past matters. Not kept in view.

**Brief.** The one-page description of the job, the output, the tests, the boundaries, and the stop. The most authoritative shelf for today's work.

**Case file.** Facts about one task that should survive the session. Each entry carries a date and a source.

**Chunk.** A piece of a document cut for search, usually a few paragraphs.

**Contradiction.** Two items in view that cannot both be followed.

**Handoff note.** A short statement of where a job stands, written to start a fresh thread: job, done, decided, rejected, open, constraints, next.

**Handback.** What the loop returns when it stops. Result, checks, unknowns, and sources. When a standing note is overridden, the handback says so.

**Index.** A searchable copy of the archive, built from chunks. A derived copy: deleting a source does not delete its chunks until the index is updated.

**Memory.** Everything a loop can see or look up that did not come from the present step, organized on shelves with different lifetimes and different writers.

**Precedence.** The order that settles conflicts between instructions: hard boundaries, today's brief, case file decisions, standing notes. The archive informs and never overrides.

**RAG.** Retrieval-augmented generation. Retrieve a passage, then have the model answer with it. A pattern, not a product and not a guarantee.

**Retention.** How long data is kept, and what starts the clock.

**Retrieval.** Finding a passage in a collection and giving it to the model. It can be a fixed step in a workflow or a tool inside a loop.

**Standing note.** A preference or rule that applies across tasks. Written by a person, scoped, dated, owned, and reviewed.

**Thread.** One continuous conversation or run with its accumulated trace.

**Trace.** The record of a run. Each goal, observation, action, and check, in order.

## What this book is claiming

It claims that memory is a set of shelves with owners and clocks, and that a single transcript hides which sentence steered an action.

It claims that most memory failures are old, unscoped, or unowned items that were never deleted.

It claims that retrieval is a tool with failure modes you can name, and that the useful test is ten real questions with known answers.

It claims that you should decide precedence in advance and make overridden notes visible, because a model resolves conflicts by vividness, not authority.

It claims that deletion must reach every copy, and that you can only promise it if you know where the copies are.

It claims that long threads decay, and that a handoff note is better than hoping.

It does not evaluate memory products. It does not compare vector stores, context sizes, or vendor memory features. Those change faster than a field guide should. It is also not legal advice. Ask the person who owns privacy and records in your organization what you owe.

## The rest of the series

Book 1. The Agent Loop. What an agent is, and how to tell it from a chatbot or a workflow.

Book 2. Briefing an Agent. How to turn a real job into a brief a person and a loop can share.

Book 3. Tools and Permissions. Read, draft, and write. Least privilege. Secrets. Logs you can replay.

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

The one-page memory policy is there to travel without the rest of the book. Print it, fill it in with the team that runs the agent, and put the owner's name at the top. The chapters are there for the day a stale note, a long thread, or a deletion request needs a clearer head.
