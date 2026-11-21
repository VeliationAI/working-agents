---
kind: chapter
title: Tools
---

A model on its own can write. It can see today's files, today's web, or today's tickets only if you hand it a tool that can look.

A tool is a function the loop is allowed to call. Search. Read a page. Query a table. Create a draft. Send an email. Run a test. The industry phrase for this is tool calling, or function calling. The phrase is less useful than the boundary you draw around each function.

## What you write down for every tool

Put three lines where the loop can read them.

- The name, in plain language.
- What it does, and what it returns.
- What it must never be used for.

The third line does real work. Models generalize. If a tool called "send email" is available, a loose goal like "make sure the customer is updated" can become a sent email. If that is unacceptable, the tool stays off the list, or it only creates a draft.

## Read tools and write tools

Reading is how the loop learns the situation. Writing is how it changes someone else's world. A first version of almost every work agent should be allowed to read, and allowed to draft. You send, file, delete, pay, merge, and deploy.

Treat approval as a tool the loop waits on. The loop prepares the action, stops, and a person lets it through. That pause feels slow the first week. It is the difference between a draft you can throw away and a message a customer has already read.

Split the tools to match that pause. "Read the support inbox" is one tool. "Save a draft reply" is another. "Send the reply" is a third, and it can stay unavailable until you have watched the drafts for a while. One permission at a time is a serious design, not a lack of ambition.

## Narrow tools return cleaner facts

Search the web is a wide tool. Search this documentation site is a narrower one. The observations come back smaller, and the check is easier to write. Add breadth when the narrow tool cannot see a fact the goal requires. Breadth you add "just in case" becomes a way for the loop to wander into sources you did not plan to trust.

A browser tool, or a tool that can click around a computer, is still the same loop. The actions are just harder to undo. The goal, the stop, and the approval need to be stricter, not looser, when the tool can touch more of the world.

## A result is evidence

A search snippet can be wrong, old, or about a different company with the same name. Carry the source with the claim. In the briefing, "Acme renewed on 2026-03-12, according to the opportunity marked closed that day" is a claim you can reopen. "Acme renewed in March" is a sentence you have to trust on tone.

When you care about a number, a date, a name, or a promise, the source is part of the output. A paragraph that cannot point back to a tool result is a draft of a memory, and memories of the model are not your files.

## When a tool fails

Decide the next beat before the first run, in plain language.

- On a timeout, retry once. If it fails again, report the gap.
- On a permission error, stop. Do not look for a side door.
- On an empty result, try one reformulated query, then mark the section unknown.

An empty result is not a blank to be filled from the model's general knowledge. The honest handback says the inbox search returned nothing for this customer in the last 90 days. That sentence is useful. An invented summary of tickets that were never opened is a failure.
