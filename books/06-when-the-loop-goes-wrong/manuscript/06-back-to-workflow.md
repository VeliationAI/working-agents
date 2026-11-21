---
kind: chapter
title: When to take the tools away
---

Some jobs should never have been loops.

You will not find that out in a planning meeting. You will find it out after the fourth incident, when the fixes are getting longer and the exam still has a column that will not turn green. At that point the right move may be to stop improving the loop and replace it.

Book 1 offered a test for this at the start. A workflow is the right design when you can write the steps before you see the case. This chapter is the same test, applied after the evidence has come in.

## Signs it is a workflow

Look at the traces from your last twenty or thirty runs, and ask the following.

Do most runs take the same path? If twenty traces show the same sequence of tool calls, in the same order, with different data, the loop is not choosing. It is following a path you did not write down. The model is doing the work of a flowchart, expensively and with variance.

```
TRACE PATHS   file-rename   last 30 runs

read_folder -> read_doc -> rename -> check            27 runs
read_folder -> read_doc -> ask_user (no date)          3 runs
Any other path                                          0 runs
```

That is a workflow with two exits. It has been paying loop prices for a decision that never varies.

Is the cost of checking close to the cost of doing? If a person must verify every handback by redoing the lookup, the loop has not saved the time it appeared to. You have a draft-generator in front of a manual job.

Do the same failures keep returning in new forms? You fix the stale policy. Next month it is a stale price list. Then it is a stale contact record. The underlying problem is that the loop is allowed to choose what to trust, and your sources are not clean enough to let it. A workflow that names the one source for each field removes the choice.

Is the action hard to undo, and are the tests hard to write? If a wrong action costs a lot and you cannot state the test precisely, you are relying on a person's attention to catch every failure. That is a fragile design, however good the loop is.

Does the job have to be repeatable for an auditor? Some work has to produce the same output from the same input, and be explained step by step. A loop can be made close to that. A workflow gives it to you for free.

Has the fix ladder run out? If every incident's fix sits on rung five or six, in the brief or the prompt, and rungs one through four have nothing left to give, you are patching around a design that is wrong.

None of these signs alone settles it. Two or three together should make you stop and look.

## A rule you can apply

Take the last ten incidents. Count how many had a first wrong step that was a choice by the loop: which source to trust, which tool to call, which of two readings to follow.

Then count how many were failures in something fixed: a stale source, a missing field, a bad tool.

If most were choices, and the choices were all of the same few kinds, you can probably write those choices as steps. Do that. If most were failures in fixed things, fix the things, and the loop is not the problem.

## You do not have to retreat all the way

The choice is not between a full loop and a full workflow. There is a spectrum, and you can move along it a step at a time.

Remove one tool. A loop with a wide tool that caused three incidents is the same loop without it. Replace the wide tool with a narrow one, or with a draft step that a person approves.

Pin one decision. If the loop keeps choosing the wrong source for one field, stop letting it choose. A step that reads the field from the named source, and hands it to the loop as an input, takes the decision out.

Fix the order. If the first three steps never vary, write them as steps. Let the model begin at the first point where judgment is needed.

Keep the model inside a step. A workflow can call a model to write a paragraph, summarize a thread, or classify a ticket. The path stays yours. The model writes within it. Book 1 drew this line: a workflow follows steps you wrote, and a model may write inside a step.

Keep the loop for the one branch that needs it. A support workflow might classify the ticket, fetch the account, and look up the policy as fixed steps, then hand a messy edge case to a loop with a narrow brief. Most tickets never reach the loop.

## A worked retreat

A team runs an agent that prepares weekly renewal briefings. The loop searches the customer record, the support inbox, and billing, and writes a two-page document. Over two months it produces five incidents.

- A briefing named an invoice from another customer with a similar name.
- A briefing reported an open support issue that had been closed the day before.
- A briefing listed unpaid invoices as zero when billing had returned an error.
- A briefing omitted the contract end date.
- A briefing's third question referred to a product the customer had never bought.

The team reads the traces. In four of five, the first wrong step is at an observation: a lookup that returned the wrong record, a stale record, or an error treated as empty. In every trace, the loop followed the same path: customer record, support inbox, billing, write.

They redraw the job.

```
RENEWAL BRIEFING   v2   workflow with one model step

1  Fetch customer record by account id (not by name).
   If missing: stop, report unknown.
2  Fetch support issues for the account id, last 90 days,
   status = open. Include the fetch time.
3  Fetch invoices for the account id, status = unpaid.
   If the call errors: write "billing unavailable",
   never zero.
4  Fetch contract end date from the contract record.
   If missing: write unknown.
5  MODEL STEP. Given only the data from steps 1 to 4, write
   the briefing sections and three questions for the account
   owner. Use no other facts.
6  PROGRAM CHECK. Sections present. Every number in the draft
   appears in steps 1 to 4. Dates in YYYY-MM-DD.
7  Save draft. Hand back with unknowns first.
```

The model is still there. It writes the briefing and suggests the questions. It no longer decides where to look, which record is the right one, or what an error means. The five incidents each map to a step that now cannot fail that way.

The job is cheaper and faster. A person reads the draft with the same tests as before. The exam from the loop version still applies, unchanged, because the exam tested the job, not the design.

That is the point worth remembering. The brief, the tests, and the exam belong to the job. They survive when the design changes.

## Retreat is not failure

Teams treat this as an admission of defeat. It is not. You tried the loop on a job. You collected evidence. The evidence said that the job was mostly a path. You wrote the path down.

The incident log is what makes that decision possible. Without it, the team would be arguing from impressions. With it, they can say: here are the traces, here is the path, here are the five incidents, and here is where the choices were.

It also frees you to use the loop where it is stronger. A job where the sources vary and the right next step depends on what was found is a good loop job. A research task across messy documents. A triage that depends on what the customer's history shows. A software change where the next edit depends on what the tests say. Keep the loop there, and hold it to the same exam.

## When to give the tools back

A retreat can be reversed. If the workflow version runs for a month, stays clean, and a new kind of case appears that the path cannot handle, you can bring the loop back for that branch.

Do it narrowly, with a brief for that branch only, its own exam tasks, and the fix ladder in your back pocket. Add the tool the branch needs and not the one the old loop had. Treat it as a new job.

## A checklist for the decision

Answer these with the traces open.

```
RETREAT CHECK   job: ____________

[ ] Do 70 percent or more of runs follow one path?
[ ] Do most incidents begin at a choice the loop made?
[ ] Are those choices of only a few kinds?
[ ] Does a person redo lookups to trust the handback?
[ ] Have fixes mostly landed on rungs 5 and 6 of the ladder?
[ ] Would an auditor need the same output from the same input?
[ ] Is a wrong action hard to undo, with tests hard to write?

Three or more boxes: write the path as steps, keep the model
inside one step, and run the old exam on the new design.
```

The threshold is a prompt for a conversation, not a law. The checklist will not make the decision for you. It will make the conversation about the traces and not about how everyone feels about agents.

## Try it this week

Take the job with the most incidents. Tabulate the paths of its last twenty runs. If one path dominates, write it as seven numbered steps on a single page, in the style above. Do not build anything yet. Show the page to the owner of the job, and ask whether it would have prevented the last three incidents. If the answer is yes, you have found a workflow.
