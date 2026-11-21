---
kind: chapter
title: The brief is the product
---

On Tuesday afternoon you type this into an agent: "Look into our three main competitors and tell me where we're behind."

Twenty minutes later you have four pages. They are fluent. They name features, quote a pricing page, and end with a confident ranking. You read the first page, nod, and forward it to your director.

On Thursday someone asks which three competitors. You do not remember choosing them. The agent did. It also chose what "behind" meant, how recent a source had to be, and where to stop. You approved all of those decisions by not making them.

That is the failure this book is about. The loop did its job. The brief did not exist.

## The brief is where the work gets decided

When you hand a job to a colleague, a lot of decisions travel with it in the hallway, in a nod, in the shared sense of what the boss cares about. A loop has none of that. Whatever you do not write down, the model fills in from its general sense of what a task like this usually looks like.

The general sense is often reasonable. That is what makes it dangerous. A reasonable guess at a competitor list looks the same on the page as a correct one.

So treat the brief as the product you are actually making. The agent's output is a consequence of it. When a run goes wrong, read the brief first. Most of the time, the loop did what the page allowed.

## What a brief is not

A brief is not a prompt, though it may become one. A prompt is the instruction for a turn. A brief is the agreement about the whole job: what finished looks like, what may be touched, when to stop.

A brief is not a policy manual. If it tries to hold the whole company, nobody reads it, including the loop. Company-wide rules belong on the standing-notes shelf from Book 1. The brief points at them in a line.

A brief is not a wish. "Make it great" cannot fail, so it cannot guide.

## Five lines that carry the weight

Book 1 gave you the page: JOB, OUTPUT, TESTS, BOUNDARIES, STOP, HANDBACK. In practice, five questions do most of the work. If you can answer these, the page nearly writes itself.

1. What is the finish line, in a sentence a stranger could check?
2. Who will use the result, and what will they do with it in the next hour?
3. What may the loop touch, and what is off the table?
4. What would make you reject the result on sight?
5. When should the loop stop and ask you, rather than push on?

Notice that none of them ask how the loop should work. A good brief is silent about method unless the method is the point. You are specifying the result and the limits. The loop can find its own way between them.

## The rewrite

Here is the Tuesday request again, as a brief.

```
JOB
Tell me which of three named competitors has shipped a feature in the
last 90 days that we do not have. Three competitors: Northwind,
Fabrikam, Contoso. "Feature" means something listed on their public
release notes or changelog.

OUTPUT
A one-page table, as a document draft. One row per feature.
Columns: competitor, feature, date shipped, source link, and whether
we have an equivalent (yes, no, or unknown).

TESTS
- Only the three named competitors appear.
- Every row has a source link and a date in YYYY-MM-DD.
- No row is older than 90 days from today.
- "Equivalent: yes" requires a link to our own documentation.

BOUNDARIES
Do not read paywalled content or log in anywhere.
Allowed tools: web fetch on the three release-note pages, search over
our public docs.
No write actions.

STOP
Stop when all three release-note pages have been read.
Stop if a page cannot be fetched; report it as a gap.
Stop after 15 steps.

HANDBACK
Table first, then gaps, then a list of pages read.
```

It is not longer because you are being careful. It is longer because Tuesday's request was missing seven decisions. This version moves them from the loop's guess to your page.

## Why the page is cheaper than the fix

Writing this takes ten minutes. Finding out on Thursday that the competitor list was wrong costs a meeting and some trust. A bad brief makes a run that looks fine and is not. The cost shows up later, and it lands on whoever relied on the result.

There is a second saving, which people miss. A brief you wrote last month is a brief you can rerun, hand to a teammate, and improve. A prompt you typed once is gone. The page is how a one-time effort becomes a reusable job.

## What to do with this chapter

Take the last request you made to an agent or an assistant. Open it beside the five questions. For each question, mark whether your request answered it, or whether the loop had to guess.

Count the guesses. Then write the brief again, and keep the count on a sticky note. By the end of the book, that number should be lower on the first draft, not the third.
