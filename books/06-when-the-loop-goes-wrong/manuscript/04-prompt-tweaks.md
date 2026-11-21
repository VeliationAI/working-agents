---
kind: chapter
title: What breaks when you just tweak the prompt
---

The refund incident is Tuesday. By Wednesday morning, someone has added a line to the instructions.

```
NEVER offer a refund. Refunds must be approved by a manager.
```

It feels right. It is short and forceful, and it addresses the failure directly. On the next run of the Dana Ruiz ticket, the draft does not offer a refund. The ticket is closed in the tracker with the note "prompt updated."

By Friday, three things have happened that nobody connected.

A customer who asked, in plain words, "what is your refund policy?" received a draft that said, "I'm unable to discuss refunds." The draft was approved, because the reviewer was busy, and the customer wrote back angry.

A different draft, for a customer entitled to a refund under the policy, suggested a replacement instead. The reviewer noticed that one.

And the section in the instructions about tone, which had been working, now sits under four lines of capitals, and the drafts have gotten curt.

None of this is a mystery. It is what you should expect when you fix a failure by adding a sentence.

## Why a tweak feels like a fix

A tweak gives you immediate feedback on the one case that hurt. You rerun that case, and it passes. The loop is visibly better on the example in front of you.

That is the only thing the tweak was tested against. You do not know what it did to the other thousand cases, because you did not run them. Your sample is one, chosen because it was the failure.

A fix that is tested on one case is a hypothesis. When a team skips the second step, the hypothesis ships as a fact.

## What happens as tweaks pile up

A prompt grows by accretion. Each incident adds a line. After a few months it contains instructions from six different failures, written by four different people, in four different moods.

Instructions start to contradict each other. "Always quote the policy" and "never discuss refunds" cannot both be followed for a customer who asks about refunds. The model resolves the conflict in whichever direction the wording of the current ticket leans, and that is not stable from run to run.

Priority becomes unreadable. Is the line in capitals more important than the line with an example? Does a rule near the end beat a rule near the beginning? The answer varies, and it can change when a model is updated, because different models weigh position and emphasis differently.

The brief stops being the page a person can read. Book 2 made the argument that the brief is the product, and that a person and a loop should be able to share one page. A prompt of four thousand words is not a page. Nobody reviews it. Nobody can say what the loop has been told.

And you lose the ability to say why any line is there. Six months on, a line says "do not mention shipping fees." Nobody knows which incident it was for. Deleting it feels risky. Keeping it costs a little on every run, forever.

## The tweak that breaks yesterday

The deepest problem is regression. A change that helps case A can hurt case B, and without a record of case B you will never see it.

This is what the exam from Chapter 2 is for. Before the tweak, run the exam and save the table. After the tweak, run it again. Compare.

```
EXAM COMPARISON   support-draft

                          v4 (before)   v4 + the tweak
01 ordinary                 3 of 3        3 of 3
02 ordinary                 3 of 3        3 of 3
03 ordinary                 3 of 3        3 of 3
04 ordinary                 2 of 3        2 of 3
05 awkward                  3 of 3        3 of 3
06 awkward (Dana Ruiz)      1 of 3        3 of 3
07 awkward                  3 of 3        3 of 3
08 edge                     3 of 3        3 of 3
09 edge                     0 of 3        0 of 3
10 trap                     3 of 3        3 of 3
11 refund-eligible          3 of 3        0 of 3   (new regression)
12 customer asks policy     3 of 3        1 of 3   (new regression)

Net: task 06 fixed. Tasks 11 and 12 broken.
```

Tasks 11 and 12 are not in the original ten. They are the two you would have added after thinking for five minutes about what the tweak might hit. That is also a useful habit. For any tweak, write down two cases the change might damage, add them as tasks, and run them before you ship.

The table makes the decision easy. The tweak fixed one task and broke two. Revert it, and look for a better fix.

## A ladder of fixes

Not every fix belongs in the prompt. When a trace has told you the first wrong step, choose the lowest rung that would have prevented it.

1. Fix the source. If the loop read a stale document, update or remove the stale document. If retrieval returned two versions, filter it to the current one. No wording change needed.
2. Fix the tool. If the loop could do something it should not, remove the capability or add a gate. A write tool that needs approval is safer than a sentence that asks the loop not to write.
3. Fix the check. Add a program test that would have caught the failure. "Every refund claim cites the latest version of its section." The check works every run, and it does not depend on the loop remembering.
4. Fix the handback. If the failure was hard for a person to see, change the shape so that it is easy. Put the cited section and its effective date on the first line of the handback.
5. Fix the brief. Edit the specific line that was ambiguous, or add the missing boundary. Keep it short. Note which incident it answers.
6. Change the wording of the prompt. This is the last rung, and it is the one people reach for first.

The ladder has an order because the lower rungs are enforced, and the upper ones are requested. A filtered retrieval cannot return the old policy. A prompt that says "use the latest policy" asks nicely.

For the refund incident, the right fix was rungs 1 and 3. Filter retrieval to the latest effective version. Add the program test. Rungs 5 and 6 changed nothing, and the brief stayed the same length.

## Tweaks that are fine

Some prompt edits are good. Look for them in the trace.

Clarifying a real ambiguity. If two reasonable readers of the brief would disagree about what it means, the loop was entitled to choose either one. Say which. "Refund window runs from the delivery date, not the order date."

Resolving a contradiction that you introduced. If two lines conflict, delete one.

Shortening. Removing lines that no longer correspond to a live failure is a fix. Do it with the exam open.

The rule for a good tweak is the same as for any change. It has a stated reason, it is as narrow as the problem, it is tested against the exam, and it is recorded.

## Record each change

Keep a changelog next to the brief. One line per change.

```
CHANGELOG   support-draft

v5   2026-11-18   Retrieval filtered to latest effective version.
                  Check added: refund-claim-is-current (program).
                  Incident 2026-11-17-A. Exam: 10 of 12 pass every run.
                  Tweak "NEVER offer a refund" tried and reverted.
v4   2026-11-02   Added: do not name competitors.
                  Incident 2026-10-29-B. Exam: 7 of 10.
v3   2026-10-14   Handback now lists unknowns first.
                  No incident. Reviewer request. Exam: 6 of 10.
```

Each line has a date, a reason, and a result. Six months from now, someone can read this and know why the brief looks the way it does. They can also see which changes made the exam better and which made it worse, and delete the second kind.

## Try it this week

Find the last change someone made to a prompt or brief after a bad run. Ask three questions. What was it tested against? What did it cost on other cases? Where is it recorded?

If the answers are "one case," "we don't know," and "in somebody's head," pick one other case the change might have hurt, write it as a task card, and run both versions on it. You will learn something either way.
