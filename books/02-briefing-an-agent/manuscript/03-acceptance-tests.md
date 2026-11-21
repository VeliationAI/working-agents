---
kind: chapter
title: Tests a person will really apply
---

A colleague hands you a handback and says, "It passed the checks." You ask which checks. The answer is: "It looked complete and the tone was right."

That is not a test. It is a mood that has been given a name.

The TESTS section of the brief is where you decide, before the run, how you will know the result is acceptable. Done well, it is the most useful ten lines on the page. Done badly, it is decoration.

## The problem with good-sounding tests

Most first-draft tests look like this.

- The summary is accurate.
- The tone is professional.
- The analysis is thorough.
- The result is well organized.

Each of these is reasonable. None of them can be applied quickly by a stranger. "Accurate" requires you to redo the work. "Thorough" has no edge. When a test cannot be applied in under a minute, it will be skipped on a Friday afternoon, which is when you need it most.

The rule for this chapter: a test is worth writing only if a tired person, who did not write the brief, can apply it without redoing the job.

## Three kinds of test

Most useful tests fall into three kinds. A good brief mixes them.

**Presence tests.** Is the thing there? The sections exist. The table has the columns. Every row has a source link. Presence tests are mechanical. You can apply them in seconds. A program can apply them too.

**Format tests.** Is it shaped correctly? Dates are YYYY-MM-DD. Amounts have a currency code. The document is under two pages. The output is a draft, not a sent message. Like presence tests, they are quick, and a program can do them.

**Sampling tests.** Is a claim true? You cannot check every claim, so you check some. "Open three source links and confirm each supports the sentence beside it." "Pick two rows at random and check the date against the source." These take a few minutes. They are the tests that catch fluent nonsense, and they are the ones you most want to skip.

If you only write presence and format tests, you will have a result that looks right and might not be. If you only write sampling tests, you will skip them. Mix them.

## Writing the test so it can fail

Take a vague test and ask: what would a failing result look like, concretely?

```
Vague:   The summary is accurate.
Sharper: Every number in the summary appears in a cited source.
         Open any two and confirm.

Vague:   Don't be too long.
Sharper: At most 400 words. Count them.

Vague:   Professional tone.
Sharper: No exclamation marks. No first names for people we have
         not met. No promise of a date.

Vague:   Cover the main issues.
Sharper: Covers each ticket tagged P1 or P2 in the last 30 days.
         The count in the first line matches the rows below.
```

The sharper versions share a trait. You can imagine a result that fails them, and you can say exactly why. If you cannot imagine a failing result, the test is not doing work.

## The unknown test

One test belongs in almost every brief, and it is the one that matters most for fluency.

```
- Every factual claim has a source, or is marked "unknown".
```

This changes what the loop is allowed to do when it hits a gap. Without it, the cheapest way to finish is to fill the gap with something plausible. With it, "unknown" is a passing answer, and a plausible invention is a failure.

Book 1 said that fluency is a weak test of truth. This line is how you act on that. It gives the loop a legal exit that is honest.

Then apply it. When a handback has no "unknown" anywhere, that is not good news. A real job, with real sources, almost always has a gap. A handback with no gaps either got lucky or filled them.

## Who applies the test

Decide this in the brief, not afterward. There are three options, and each is good at something.

- **A program** applies presence and format tests. Is every row dated? Is the file under the limit? It is fast, consistent, and tireless. It cannot judge meaning.
- **A second model call** can apply softer checks, such as "does each claim have a source nearby?" It is useful, but it can share the first model's blind spots. Treat its verdict as a flag, not a verdict.
- **A person** applies sampling tests and anything where the stakes are high. A person is slow and costly, so give them a short list.

The mistake is to leave this unspecified, so that everyone assumes someone else is checking.

## How many tests

Five to eight. Fewer than five usually means the brief has not been thought through. More than eight usually means some are redundant, or too fussy for anyone to apply.

If a test has never failed in ten runs, ask whether it is worth its line. If a run failed in a way no test caught, add the test. The tests are the part of the brief that should grow, slowly, from real failures.

## A worked example

A team asks a loop to summarize last month's support queue for the Monday meeting. Here is the first draft of the tests.

```
TESTS
- The summary is accurate and covers the main themes.
- It is concise.
```

Here is the version after the team read it as strangers.

```
TESTS
- Exactly three sections: volume, top three themes, open escalations.
- Volume section gives the ticket count for the month and for the
  month before, as numbers.
- Each theme cites at least two ticket IDs.
- Open escalations lists every ticket tagged P1 open for more than
  7 days. If none, it says "none".
- Under 350 words.
- Anything the loop could not retrieve is listed under "unknown".

Applied by: a script checks sections, word count, and that the
ticket IDs exist. A person opens two cited tickets and confirms each
matches its theme.
```

The first version could not fail. The second can fail in six distinct ways, each of which takes seconds to see. The extra effort was four minutes.

## What to do with this chapter

Take the tests from your own draft brief. For each one, write the failing result in a sentence. If you cannot, rewrite the test.

Then add the unknown line, and write who applies each test. Run the brief once and apply the tests exactly as written. Whatever you find yourself checking that is not on the list is your next test.
