---
kind: chapter
title: Brief, prompt, standing note, checklist
---

Your team has a prompt saved in one tool. It says, "Be concise and professional." A checklist lives in a wiki, and says, "Verify all figures." A policy document in a shared drive says figures must come from the finance system. A standing note in the agent's settings says, "Use approved sources."

Four documents, written by four people, in four months. Nobody knows which one wins when they disagree. On Thursday, they disagree.

This is what happens when one instruction becomes four without anyone deciding it. The fix is not a better prompt. It is to treat them all as views of the same instruction.

## The same instruction, four shapes

A brief, a prompt, a standing note, and a checklist are not four kinds of content. They are four ways of presenting a smaller set of decisions to different readers at different moments.

- The **brief** is for the job. It states the finish line, tests, boundaries, stop, and handback, once, for this task.
- The **prompt** is for a turn. It is the text the model actually receives on a step, built from the brief and whatever the loop has seen so far.
- The **standing note** is for every job. It holds preferences and rules that outlast any single brief.
- The **checklist** is for the person who reviews. It is the tests, rewritten as questions a human can tick.

The decisions underneath are the same. Dates are YYYY-MM-DD. Claims need sources. No promises of refunds. Each decision should be written once, in one place, and shown in the other shapes by copying or by reference.

## Write each decision once

Pick the home for each decision, and let everything else point at it.

- Dates as YYYY-MM-DD live in the standing note. They appear as a test in the brief and a tick on the checklist.
- "Never promise a refund" lives in the standing note for support jobs. It appears as a test in the support brief and a tick on the checklist.
- This week's five metrics live in the weekly brief. They appear as a line in the prompt and a tick on the checklist.
- "Stop after 15 steps" lives in the brief. It appears as a harness limit, set from the same number.

The rule is that the number 15 lives in one file. The harness reads it. The brief shows it to the person. If someone changes it, they change it once, and every view updates, because every view is generated from the same source or points at it.

If you cannot generate the views, then at least keep a single source file, mark the others "copy of", and date them. A copy with a date is a copy you can distrust at the right moment.

## Generating the prompt from the brief

The mistake in most prompt-writing is to start from nothing. Start from the brief, and let the prompt be a faithful rendering of it.

A workable prompt for a loop has five parts, in this order.

1. **Role and job.** One or two sentences, taken from JOB.
2. **Output and tests.** The OUTPUT and TESTS lines, unchanged.
3. **Boundaries.** What not to do, and the tools allowed, taken from BOUNDARIES.
4. **Stop and handback.** The STOP and HANDBACK lines, unchanged.
5. **Standing notes.** The short list of rules that apply to every job.

Notice that nothing in the prompt is new. You add no clever phrasing, no pleading, and no capital letters. When the prompt contains a rule the brief does not, you have found a decision that was made in the wrong place. Move it to the brief, or the standing note, and regenerate.

Keep wording stable. If the brief says "mark unknown" and the prompt says "flag uncertainty", you have two instructions, and the model may treat them as two. Copy the words. Do not paraphrase your own rules.

## Standing notes: small, dated, defensible

The standing notes shelf is the one that grows without anyone noticing. Every incident adds a line, and nobody removes one. After a year it has sixty lines, three of which contradict each other.

Rules for the shelf.

- **Keep it under fifteen lines.** If it grows, ask which lines are really per-job and belong in a brief.
- **Date every line,** and name the owner. "2026-04-02, policy owner: no goodwill refunds on the Basic plan."
- **Write the rule, not the story.** The story belongs in the changelog.
- **Review it with the briefs,** at the same monthly meeting, by the same person.
- **Delete before you add.** If a new line conflicts with an old one, pick which stays, and remove the other. Do not let both sit in view.

When a standing note fights a brief, the brief should win for that job, but only if the brief says so on its face. "This job overrides the standing note on competitor names, because the audience is the internal strategy team." An override that is written down is a decision. One that happens by accident is a bug.

## The checklist is the tests, again

A reviewer should not have to read the brief to review the result. Give them a checklist built from the TESTS section, one line per test, in the order they are quickest to apply.

```
REVIEW CHECKLIST: weekly ops note
[ ] Four sections, in order (script checks)
[ ] Five metrics present, each with a dashboard name (script checks)
[ ] Under 450 words (script checks)
[ ] Open two dashboards: do these two numbers match? ____ ____
[ ] Any metric moved 15 percent or more: is it flagged in words?
[ ] "Unknown" or "not retrieved" appears where something is missing?
[ ] Sources read: expected count matches?
Reviewer: ______  Date: ______
```

The checklist is not a second set of rules. It is the same tests in a form that fits on one side of paper. If a test is on the checklist and not in the brief, one of them is wrong.

Put the reviewer's name on the checklist. A name changes how people tick boxes.

## When the views drift apart

Eventually they will. Someone edits the prompt in the tool's settings to fix one bad run. Someone adds a line to the checklist and forgets the brief.

Two habits slow this. Give each job one owner, the only person who edits the source. And once a month, print the brief, the prompt as actually sent, and the checklist, and mark every decision where they disagree. If the harness logs the exact prompt on each run, use that log. The prompt you intended and the prompt that ran are different documents more often than anyone expects.

## What to do with this chapter

Gather every instruction that touches one job: the saved prompt, the checklist, the policy excerpt, the standing notes. Lay them out together and underline each decision.

Pick a home for each decision. Delete the duplicates, or mark them as copies with a date. Then regenerate the prompt and checklist from the brief, change nothing by hand, and run once. If the result is different from last week's, you have found a decision that was living in the wrong place.
