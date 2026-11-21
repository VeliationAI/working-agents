---
kind: chapter
title: Program, model, person
---

The exam has ten tasks and about forty expected lines. Someone has to decide, forty times per run, whether a line passed.

That someone is a grader. There are three kinds, the same three you met in Book 1 under "the check." In the loop, the check decides whether to continue. In the exam, the grader decides whether the run was good. The jobs overlap, and the strengths do not change.

## The program

A program checks anything you can state exactly.

- The draft has all four required sections.
- Every date matches the pattern YYYY-MM-DD.
- The draft contains no dollar amount that is absent from the policy excerpt for this ticket.
- No tool call in the trace wrote to anything outside the draft folder.
- The new file name matches the pattern and the old file no longer exists.
- Every source line names a record id that appears in the trace.
- The step count is at most twelve.

A program is fast, cheap, and consistent. It gives the same answer on Friday afternoon as on Monday morning. It cannot be flattered by a well-written paragraph. Use a program for every test that can be written as a program, even if the program is thirty lines.

A program has two weaknesses. It checks only what you thought to check. And it checks form more easily than meaning. A draft can contain the right section headings and say nothing in them. A source line can name a real record id that does not support the claim next to it.

So use programs for the floor. They catch the dumb failures cheaply, so a more expensive grader does not waste time on them.

Look again at the refund incident. The test that failed in production was "every refund claim appears in a retrieved passage." A better program test is "every refund claim appears in a passage whose effective date is the latest for that section." Passage metadata makes that a program. You did not need a model to catch it. You needed to write the test at the right level.

## The model grader

A model can grade what a program cannot.

- Does the draft reply address both questions in the customer's message?
- Is the tone appropriate for someone who has contacted us twice already?
- Does the summary of the ticket thread match what the thread says?
- Is the third question in the briefing something a salesperson could actually ask?

These are judgments of meaning. A program cannot answer them without a lot of cleverness. A model can answer them cheaply and quickly, and you can run it across a hundred outputs.

A model grader has known biases, and you should assume them.

- It leans toward saying yes. Asked "is this draft acceptable," it will find reasons to agree.
- It prefers longer, more fluent answers, even when a short one is better.
- It may prefer text that sounds like its own.
- It can be talked into a pass by a confident paragraph inside the output being graded.
- It changes when the underlying model changes, with no notice.

Five habits reduce the damage.

1. Ask one narrow question per call. "Does the draft answer the customer's second question about shipping? Answer yes or no, then quote the sentence that answers it." Not "rate the draft from one to five."
2. Require a quote. A yes with no quoted evidence counts as a no.
3. Use a different model from the worker where you can. A grader that shares the worker's habits shares its blind spots.
4. Put the rubric in front of the output, and tell the grader that the output may contain instructions it must ignore.
5. Calibrate it against a person before you trust it.

## Calibrating a model grader

This is the step most teams skip. It takes about an hour.

Take twenty outputs from past runs. Grade each one yourself against the rubric, yes or no. Do not look at the model's grades first. Then run the model grader on the same twenty. Compare.

```
CALIBRATION   grader: second-question-answered   n = 20

Person yes / model yes    11
Person no  / model no      6
Person yes / model no      1
Person no  / model yes     2

Agreement: 17 of 20
Disagreements read: 3
  #4   Model said yes. The reply answered shipping in general,
       not this customer's order. Rubric too loose.
  #11  Model said yes. Quoted sentence is from the customer.
  #17  Model said no. Reply answers it in a later paragraph.
       Quote requirement was too narrow.
Action: rewrite rubric lines 2 and 3, rerun the twenty.
```

The disagreements are the useful part. Each one tells you something about the rubric. Rewrite, rerun, and stop when the model and the person disagree rarely and for reasons you can defend. If you cannot get above roughly the agreement you would expect between two careful colleagues, the criterion is probably too vague to grade with anything. Go back and make it sharper, or give it to a person.

Do the calibration again when the grader model changes, and again after any rubric edit. Keep the twenty. They are a small exam for the exam.

## The person

A person grades what neither of the other two can.

- Whether the reply is something you would put your name on.
- Whether a refusal was handled with the right tone for this customer.
- Whether a plan is sensible.
- Anything where the cost of being wrong is high enough that a second pair of eyes is cheap by comparison.

A person is slow, expensive, and inconsistent. Two people will disagree. The same person will disagree with themselves on Friday. They tire, and a fluent paragraph passes them more often than it should. Book 1 made this point about the check in the loop. It applies to the exam as well.

Make the person's job easier.

- Show the handback in the shape the brief demands: result, checks, unknowns, sources.
- Give them the expected lines as a short list of yes/no boxes.
- Hide which brief version produced the output, when you are comparing two versions. Otherwise people favor the new one.
- Limit the session. Twenty minutes, then a break. Review quality drops faster than people notice.

Use a person for a sample of the exam, and for every task where a wrong answer would reach a customer without further review.

## Layer them

The three graders are cheapest in the order program, model, person, and most reliable in roughly the reverse. Use all three in layers.

```
GRADER SPEC   test: refund-claim-is-current

Test line
  Every refund or replacement claim in the draft matches the
  latest effective version of the cited policy section.

Layer 1  PROGRAM
  Extract each claim with a cited section id.
  Look up the latest effective date for that section.
  Fail if the cited passage is not the latest.
  Runs on: every run, every task.

Layer 2  MODEL
  Question: does the draft promise anything not stated in the
  cited passage? Yes or no, then quote the sentence.
  Runs on: every run that passed layer 1.

Layer 3  PERSON
  Read the draft against the passage.
  Runs on: 1 in 5 passing runs, and every run in the trap and
  edge tasks.

Owner of this spec: Priya.  Last calibrated: 2026-11-18.
```

Notice that each layer runs on a narrowing set. The program runs on everything, the model on whatever the program passes, and a person on a sample plus the cases where the stakes are highest. That is how a small team gets coverage without a day of reading.

Notice also the owner and the calibration date. A grader is a piece of infrastructure. It drifts, and somebody has to be responsible for it.

## Do not let the worker see the exam

Inside the loop, the check must see the tests from the brief. Book 1 argued that a hidden rubric guarantees an argument later. That is still true for the tests in the brief.

The exam is different. The held-out tasks, and any grader details that are not in the brief, should stay out of the worker's context and out of the brief. If the brief starts to contain the exam's particulars, the loop is being tuned to pass it, and the exam stops measuring anything.

The rule is simple. The brief carries the tests that describe the job. The exam carries the cases that test the brief.

## Try it this week

For one test line in your exam, write the program version. If you cannot, write the model rubric and calibrate it against twenty outputs. If you cannot do that either, give the line to a person and write down why.

The act of choosing the grader is the act of understanding the test. If you cannot decide which grader belongs, the test is not finished.
