---
kind: chapter
title: Monday
---

Pick one job you have already done by hand at least three times. Not the biggest one. Not the one that makes the best story. A job where you know what a good result looks like because you have produced it, and where a bad one would be caught by somebody within a day.

Then spend the morning on the page, not on the tool.

1. **Write the first draft of the brief in fifteen minutes.** Use the Book 1 layout: JOB, OUTPUT, TESTS, BOUNDARIES, STOP, HANDBACK. Do not polish. Where you do not know an answer, write a question mark. Those are the lines that matter.
2. **Answer the five questions.** Finish line a stranger can check. Who uses the result in the next hour. What may be touched. What you would reject on sight. When to stop and ask.
3. **Hand the page to a stranger.** Someone who does not know the job. Ask for their questions, and do not answer them. Collect them on paper.
4. **Sort the questions.** Each goes to the brief, the standing notes, or a reference the loop can look up. Add the lines. Define any special words in a TERMS block.
5. **Sharpen the tests.** For each, write the failing result in a sentence. Add the unknown line. Write who applies each test: a program, a model, or a person.
6. **Name the biggest risk.** What is the single worst thing the loop could do on this job? Check that a test or a boundary catches it. If not, write it now.
7. **Run it read-only.** No send, no edit, no write beyond saving a draft. Timebox the run. Read the trace if it overruns.
8. **Apply the tests exactly as written.** Whatever you find yourself checking that is not on the list is a missing test. Write it down.
9. **Run it again** with the new lines. Compare the two handbacks. If the second is better because the page is better, you have learned something you can reuse.

That is the whole morning. By lunch you have a page that a person and a loop can share.

## If the job repeats

Split the page into the fixed part and the variable part. Put a date at the top and a changelog at the bottom. Run it in draft for four weeks with a named reviewer. In the fifth week, read the four handbacks side by side and add a test for every manual fix that repeated.

Put two things in the calendar before you close the file: a monthly review of the brief, and a quarterly day when someone redoes one number from scratch.

## If you lead a team

The most useful hour this week is not a tool demo. Ask each person for one job they repeat. Have them write the brief, hand it to a colleague, and bring the colleague's questions to the meeting.

You will learn three things at once. Which jobs are well enough understood to hand to a loop. Which depend on one person's head. And where the team's words mean different things in different departments.

Write down the standing notes you agree on, and give each a date and an owner. Keep the list under fifteen lines.

## If you build the harness

Build the prompt from the brief, not beside it. Log the exact prompt sent on each run. Make the step limit, the allowed tools, and the stop conditions read from the same file the brief is generated from. When someone edits one, the others should change, or the build should fail.

A brief that exists only as a document will drift from the system that runs it. Make the page the source.

## What to ignore for now

Ignore the search for the perfect prompt wording. A brief with specific tests survives a model swap, because the tests do not depend on the model's habits.

Ignore the urge to make the brief longer after one failure. Add the one test that would have caught it. Delete a line that has not mattered in ten runs.

Ignore the idea that a good brief means a hands-off loop. It means the review is short, specific, and possible. You are still the person who checks.

The next book goes one level down, into the tools themselves: what the loop may read, what it may draft, what it may write, and the limits that keep it honest. The brief says what is allowed. Tools and permissions are where that sentence becomes true.

For Monday, you need a page that fails when the work is wrong, a stranger who has read it, and a run you can check in a few minutes.
