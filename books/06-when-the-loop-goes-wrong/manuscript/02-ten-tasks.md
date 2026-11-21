---
kind: chapter
title: Ten real tasks is an exam
---

After the refund incident, someone fixes the retrieval filter and the next draft is correct. Everyone relaxes.

Then someone asks the question that matters. How do we know the fix did not break something else?

You need an exam. Not a benchmark, not a leaderboard, not a vendor's score on a task that is not yours. A folder of ten real tasks, each with a written finish line, that you can run again every time anything changes.

## Why ten

Ten is small enough that you will actually build it, and large enough to show you something.

One task tells you nothing. A model can pass a single task by luck, and a good brief can fail it by bad luck. Fifty tasks is better, and nobody builds fifty tasks in the first week. Ten fits in an afternoon. It will not support a claim like "this works 95 percent of the time." It will support a more useful claim: "after this change, seven of ten pass, and three of those used to fail."

Think of it as a smoke alarm. It does not tell you the house is safe. It tells you when something is on fire.

## Where the tasks come from

Take them from real work. Open last month's jobs and pick from them. Do not invent tasks that look like what you imagine the loop will do. Your imagination is a poor sampler of what customers actually write.

Choose a mix.

- Four ordinary tasks. The kind that make up most of the volume. If the loop cannot pass these, nothing else matters.
- Three awkward tasks. Real cases that were hard for a human too. A ticket with two questions. A customer with an unusual account history. A document in a messy format.
- Two edge cases. A case where a source is empty. A case where two sources disagree. These are the ones where a loop fills gaps, and you want to see it decline.
- One trap. A task that asks the loop to step outside its boundaries. A request to send a message when the brief says draft only. A prompt that tells the loop to ignore its instructions, hidden inside the customer's text.

Each incident you write up later adds a task. The exam grows from your mistakes, and the mistakes are the best tasks you will ever have. After the refund incident, the ticket from Dana Ruiz goes into the folder, with the policy versions as they stood that day.

## What a task card contains

Keep each task as a single card, in a file you can version. Plain text is fine.

```
TASK 06   refund-after-window
Kind: awkward

INPUT
Ticket T-5521 (copied). Order 8814 (copied).
Policy snapshot: 2026-11-17, both versions of section 4.2.

BRIEF VERSION
support-draft v4

EXPECTED
- Draft cites section 4.2 revised (replacement or repair).
- Draft does not offer a refund.
- Draft does not quote the 60-day text.
- Draft mentions that replacement stock exists.
- No message sent.

KNOWN HARD PART
Retrieval returns two versions of the same section.

LAST FAILED
2026-11-17, offered full refund. Incident 2026-11-17-A.
```

Two features are doing the work here.

The inputs are frozen. The ticket, the order, and the policy snapshot are copies, so the task means the same thing next month. If your task reads live data, it will change under you, and a failure next month may be about the data and not about your change. Copy the inputs. If a tool must be called, give it a test double that returns the frozen data.

The expected results are written as tests, not as a model answer. "Draft does not offer a refund" can be checked. "Draft is similar to this reference reply" cannot be checked by anyone who is tired. Write each expected line so that a stranger could answer yes or no.

## Scoring

Score each test as pass or fail. Do not give a task a score out of ten. A score out of ten invites you to average, and an average hides the one failure that matters. A draft that is perfect in nine ways and offers an unauthorized refund is a failed run.

A task passes when every expected line passes. The exam result is the count of passing tasks, plus the list of lines that failed.

```
EXAM RUN 2026-11-18   support-draft v4   3 runs per task

Task            Run 1   Run 2   Run 3
01 ordinary      pass    pass    pass
02 ordinary      pass    pass    pass
03 ordinary      pass    pass    pass
04 ordinary      pass    pass    fail  (no source line for date)
05 awkward       pass    pass    pass
06 awkward       fail    pass    fail  (quoted 60-day text)
07 awkward       pass    pass    pass
08 edge          pass    pass    pass
09 edge          fail    fail    fail  (filled missing invoice)
10 trap          pass    pass    pass

Tasks passing every run: 7 of 10
Tasks failing every run: 1 (09)
Tasks flaky: 2 (04, 06)
```

## Run each task more than once

A loop is not deterministic in the way a spreadsheet is. The same input can take different paths on different runs. A task that passes once and fails once is not a pass. It is information.

Three runs per task is a reasonable default when the runs are cheap. Report three categories. Passes every time. Fails every time. Flaky. Each one calls for a different response.

Always-fail tasks point to a missing capability, a missing tool, or a missing instruction. Look at the trace once. The cause is usually plain.

Flaky tasks point to a brief that leaves a decision open. The loop is choosing, and the choice is not stable. Read the passing trace and the failing trace side by side. The first point where they diverge is the decision the brief forgot to make.

Always-pass tasks tell you the loop can do the work. Keep them. They are your regression guard.

## Do not tune to the exam

Hold back two of the ten, or add two more, and call them held-out. Do not look at their traces while you are changing the brief. Run them only when you think you are done.

If the visible eight improve and the held-out two do not, you have fitted the brief to the exam. You taught the loop to pass those eight cases. The brief now contains the particulars of Dana Ruiz's refund, and a different customer with a similar problem will fail.

A good fix is general. "Use the policy version with the latest effective date. If two versions have the same effective date, stop and ask." A bad fix is specific. "For refund tickets on units delivered in October, use section 4.2 revised." The first one passes the held-out tasks. The second one does not.

## What ten can and cannot tell you

Ten tasks can tell you that a change made things worse. That alone justifies the folder.

Ten tasks can tell you that a failure is not a fluke. If a task fails three of three runs, you have a reproducible fault.

Ten tasks cannot tell you the rate of failure in production. Do not publish a percentage from this exam. When a manager asks "how reliable is it," the honest answer is that on ten representative tasks, seven pass every time, and you know why the other three do not.

Ten tasks cannot cover a job that has dozens of distinct kinds of input. If your support queue handles billing, shipping, warranty, and account access, you may want ten tasks per kind. Build them as the incidents arrive. You are not trying to be complete on day one.

## Keep the exam cheap

An exam that takes a day to run will not be run. Make it cheap in three ways.

Use frozen inputs and test doubles, so no live system is touched.

Script it. A command that runs all tasks, collects the traces, applies the program graders from the next chapter, and prints the table above.

Run it on every change. A new brief version, a new model, a new tool, a changed retrieval setting. If a vendor swaps the model under you, your exam is how you find out.

Store the traces with the table. When a task goes from pass to fail, you want the passing trace and the failing trace side by side.

## Try it this week

Pick the job from your Monday task in Book 1, or the job you have been running since. Write four ordinary cards from last month's real inputs. Write one trap. Run the loop on those five, three times each, and read the table.

You will not finish all ten the first day. Five cards and a table is already more than most teams have.
