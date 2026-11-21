---
kind: chapter
title: How to read a trace
---

You have a complaint and a trace. Start with the complaint.

Write one sentence that says what was wrong with the output. "The draft offered a full refund at 45 days. Policy allows a replacement or repair." Put that sentence at the top of a blank page. Everything you read in the trace is a search for the place where that sentence became possible.

Do not read the trace from the top. A trace is a story told in the order things happened, and the cause is rarely at the beginning. Read it from the wrong sentence backward.

## A trace worth reading

Here is a trace for a support draft. The job came from Book 1: draft a reply, quote the policy, offer only what the current policy allows, and do not send anything. The trace is shortened, but the shape is real.

```
RUN 2026-11-17-0932   brief v4   job: support-draft   ticket T-5521

1  GOAL     Draft a reply to ticket T-5521. Quote the policy.
            Offer only what the current policy allows.
            Do not send. Save a draft.
2  ACT      read_ticket(T-5521)
3  OBSERVE  Customer: Dana Ruiz. Order 8814, delivered 2026-10-03.
            "The unit stopped working this week.
            I want my money back."
4  ACT      search_policy("refund unit stopped working")
5  OBSERVE  3 passages.
            A. Returns, section 4.2: full refund within 60 days
               of delivery for faulty units.
            B. Returns, section 4.2 (revised): replacement or
               repair within 30 days; refund only if no
               replacement is available.
            C. Shipping fees, section 7.1.
6  ACT      read_order(8814)
7  OBSERVE  Delivered 2026-10-03. Warranty: standard.
            Replacement stock: 14 units.
8  ACT      write_draft(T-5521, "Hi Dana, I'm sorry the unit
            failed. Under section 4.2 you are entitled to a full
            refund within 60 days of delivery...")
9  CHECK    Every refund claim appears in a retrieved passage.
            Yes (passage A). Draft saved. No message sent.
10 HANDBACK Draft saved to T-5521. Policy quoted: section 4.2.
```

The complaint says the draft offered a full refund. That sentence is in step 8. Now go backward.

## The backward read

Ask five questions, in order. Write the answer to each one beside the step it points at.

1. What did the loop write? Step 8 offered a refund at 60 days.
2. Where did that claim come from? Passage A, retrieved at step 5.
3. Was that the right passage? No. Passage B is the revised policy. Passage A is the old one.
4. Why did the loop pick A? The retrieval returned both with no dates, and nothing in the brief said which version wins. Passage A also matches what the customer asked for.
5. Why did the check pass? The test asked whether the refund claim appeared in a retrieved passage. It did. The test was true and useless.

Five questions, and you have a first wrong step: step 5, where retrieval returned two versions of the same section and the brief had no rule for choosing. You also have a second wrong step: step 9, where the check tested for the existence of a source instead of the currency of one.

That is a better result than "the model made a mistake." You can fix a retrieval filter. You can rewrite a test. You cannot fix "the model made a mistake," and nobody will remember to try.

## What you are looking for

Most bad runs fall into a small number of shapes. Learn to spot them in the trace.

The wrong fact entered at an observation. A tool returned something stale, partial, or from the wrong record. The loop acted correctly on bad input. Fix the tool or the source.

A gap was filled. The observation was empty, and the next action contained a specific name, number, or date that appears nowhere above it. Look for any value in an action that you cannot find earlier in the trace.

The goal in view was not the goal you wrote. Compare step 1 with the brief. Standing notes, default instructions, and old context can add a second goal. A trace that starts with a different goal than your brief has already told you the cause.

The check checked the wrong thing. This is the trace above. The check passed, and you can say in one sentence why it should not have.

The check never ran. The loop moved from action to handback with no check line. Some harnesses make the check optional. A trace without a check beat is a trace of a system that was never asked to be honest.

The stop was missing. The same search with small variations, five, six, seven times. No new observations. Cost rising. This is a loop that can only get better, never done.

A write happened that was not on the page. Search the trace for every action that changed something. Compare the list with the boundaries in the brief.

## What a trace has to contain

You can only read what was recorded. If your harness leaves out any of the following, the trace will fail you on the day you need it.

- The exact goal text in view at each beat, or at least the brief version that was loaded.
- The exact input to every tool call, not a summary of it.
- The exact output of every tool call, truncated only with a note saying how much was cut.
- The check, including which tests were applied and the result of each.
- A timestamp, a cost or token count, and a step number for every beat.
- The model, the brief version, and the tool versions that were live for the run.

The last item surprises people. Without versions, you cannot tell whether a failure belongs to the run you are reading or to a configuration that changed since. Record them once at the top of each trace. It costs three lines.

If the trace holds private customer data, which it often will, decide who may read it before you need it, and record that decision. Traces are for debugging. They are also a copy of everything the loop touched.

## Reading under time pressure

Give the first read ten minutes. Set a timer. In ten minutes you should have the complaint sentence, the backward read, and a guess at the first wrong step.

Then check the guess with a replay. Run the same task with the same inputs and the fix you propose. If the replay passes, you have found something real. If it fails differently, your first guess was wrong, and the second trace is now the better one to read.

Keep a short note with each trace you read.

```
TRACE NOTE
Run: 2026-11-17-0932
Complaint: draft offered a full refund at 45 days.
First wrong step: 5. Retrieval returned two versions, no dates.
Second wrong step: 9. Check tested existence of a source,
  not whether the source was current.
Not at fault: step 6 and 7. Order data was correct.
Replay with retrieval filtered to current version: passes.
```

The line "not at fault" matters. It stops the next reader from re-reading steps you have already cleared.

## Do not read the loop's reasoning as an explanation

Some systems show a narrated reasoning for each step. "I'll check the policy for the correct refund window." It is tempting to read that as a statement of why the loop did what it did.

Treat it as one more observation. It is text the model produced, and it can be wrong about its own cause. Compare it with what the tool actually returned. If the narration says "the policy says 30 days" and the tool output says 60, the narration is the thing that went wrong, and you have found it in one glance.

The evidence is the tool calls and the tool outputs. Read those first. Read the narration to find out what the loop believed, and compare that with what was there.

## Try it on your own job

Take the last handback you did not fully trust. Open its trace. Write the complaint sentence. Read backward with the five questions. Name the first wrong step, and say whether it was an observation, an action, or a check.

If you cannot find a trace, or if the trace you have cannot answer the five questions, that is the first finding. Fix the logging before you fix anything else.
