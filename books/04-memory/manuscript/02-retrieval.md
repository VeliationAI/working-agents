---
kind: chapter
title: Retrieval, and what people mean by RAG
---

A support lead asks an agent: "Can we refund a customer who cancelled eleven days after renewal?" The agent searches the help center, finds a page titled "Refund policy," and answers: "Yes, within fourteen days of renewal." The lead forwards the answer to a customer.

The page was real. The sentence was on it. The page was also the 2024 version. The current policy, in a different folder, says seven days for annual plans. The customer is owed a refusal, and now has a promise.

Nothing in the loop was broken. The search ran. A passage came back. The model quoted it. The failure was in what the search was allowed to find, and in what nobody asked it to check.

This chapter explains retrieval well enough that you can ask the right question when someone tells you "we use RAG."

## What retrieval is

**Retrieval** means finding a passage in a collection and putting that passage in front of the model. That is all.

The collection might be a folder of policy documents, a ticket history, a wiki, a set of contracts, or last quarter's reports. The passage is a piece of one of those: a paragraph, a section, a row. The model reads the passage along with the question and answers using it.

People call a common version of this **RAG**, short for retrieval-augmented generation. The phrase means: retrieve something, then have the model generate an answer with it. That is the entire claim. It is a pattern, not a product, and not a guarantee of correctness.

Two things worth keeping straight.

First, retrieval is a step, or a tool. It can be a fixed step in a workflow: always search, always take the top three passages, always answer. Or it can be a tool inside a loop: the agent decides whether to search, what to search for, and whether the result is good enough or needs a second query. Book 1 made this point and it bears repeating. A system that retrieves a paragraph and answers once is not, by that fact alone, an agent. An agent may use retrieval and still be an agent because of the loop, not because of the search.

Second, retrieval is the archive shelf in motion. It is how the loop reaches into the archive without stuffing the archive into every run.

## How a search finds things

You do not need to build one. You do need a rough picture, because the picture tells you where it fails.

There are two common ways to find a passage.

**Keyword search** looks for the words you typed. Ask for "refund policy" and it returns documents containing those words, ranked by simple signals such as how often and where the words appear. It is predictable. It misses a document that says "money-back guarantee" and never says "refund."

**Meaning-based search**, often called semantic or vector search, converts text into lists of numbers that capture roughly what it is about, then finds passages whose numbers are close to the question's. Ask for "get my money back" and it can find the "refund policy" page without a shared word. It is good at paraphrase. It is weaker at exact things: a part number, an invoice ID, a name, a clause number. It can also return something that sounds related and is not the right document.

Many systems combine both, and then rank the combined results. The details change with the tool. The tradeoff does not. You are choosing between literal and fuzzy, and you will want one or the other depending on the question.

Before any of that works, the collection is usually split into pieces. A long document becomes chunks of a few paragraphs each, so a search can return the relevant part rather than the whole thing. How the pieces are cut matters more than people expect. Cut in the wrong place and you separate the rule from its exception. The chunk that says "Refunds are available within fourteen days" is returned. The chunk with "except annual plans, where the window is seven days" is not.

## Five places retrieval fails

When retrieval gives a wrong answer, it is nearly always one of these. Learn the list and you can diagnose most problems by reading a trace.

1. **The right document was not in the collection.** Nobody indexed the new policy. The agent answered from what existed.
2. **The right document was there and was not returned.** The query used different words. The chunk was cut badly. The ranking preferred a longer, older page.
3. **A stale document was returned.** The one in this chapter's opening. The search matched the text, not the date.
4. **The right passage was returned and was misread.** The model took a general statement and applied it to a special case, or merged two passages that disagree.
5. **Nothing relevant existed, and the model answered anyway.** The system returned the closest thing, not a good thing. The model, handed a passage, wrote as though it answered the question.

The fifth is the dangerous one. A search always returns something. If you do not give the loop a way to say "none of these answer the question," it will treat the best of a bad set as the answer.

## Retrieval as a tool, with a stop

In a loop, retrieval is a tool the agent calls. That means you can write its brief like any other tool's.

```
TOOL: search_policies
Reads: policy documents marked status "in force".
Returns: up to 5 passages, each with title, section,
         last-reviewed date, and status.
Does not return: drafts, archived versions, internal notes.

RULES FOR USE
- Quote the passage you rely on, with title and section.
- If the passage is older than 12 months, say so.
- If no passage answers the question, say "not found."
  Do not answer from general knowledge.
- If two passages disagree, return both and stop.
```

Each line removes one of the five failures. "Status in force" addresses stale documents. "Last-reviewed date" lets the loop and you see how old a passage is. "Not found" is an allowed answer, which gives the loop a way out of the fifth failure. "Return both and stop" turns a silent merge into a handback.

Notice how little of this is about the model. It is the shape of the tool and the rules of the brief.

## What to put in view and what to retrieve

You could paste the whole policy handbook into the conversation. Sometimes you should. Usually you should not.

Put it in view when:

- It is short, a page or two.
- It governs every action the loop will take.
- Missing it would be a serious mistake, not a small one.

Retrieve it when:

- The collection is large, and any one run needs a small part of it.
- The relevant part depends on the question.
- The collection changes more often than your briefs do.

Pasting a forty-page document buries the finish line. The model attends to a vivid sentence on page nineteen and loses the goal. On the other hand, retrieval has its own costs: a search can miss, and a missed passage looks identical to a missing rule.

A middle path that works well for many jobs is a short, pinned summary of the rules that must never be missed, plus retrieval for the detail. The summary sits on the standing-notes shelf and points to the sources. "Refunds: see the in-force refund policy. Never promise outside it." The loop knows the rule exists and knows to look.

## Citations are your check

The most useful thing you can demand from a retrieving agent is the passage itself.

Not "according to our policy." A quote, a title, a section, a date. Something you can open in ten seconds and compare.

```
Answer: Refund is not available.
Basis: Refund Policy, section 3.2, reviewed 2026-09-01:
  "Annual plans may be refunded within seven days of renewal."
Customer cancelled eleven days after renewal.
Not checked: whether an account-level exception exists.
```

You can audit that. You can see the review date. You can see what the agent did not check. If it had quoted the 2024 page, the date would have given it away.

A citation can still lie. The agent may quote a passage that does not say what it claims it says. That is why the check should open the source, not trust the quote's presence. Sample a few. Over a week, you will learn how often the quote matches the claim.

## Ten questions, not a benchmark

You do not need a leaderboard to know whether your retrieval works. You need ten questions from real work, with answers you already know, and a source that should be found.

1. Write ten questions people actually ask. Include two that have no answer in the collection, and two where the answer changed recently.
2. For each, write down the correct answer and the document that holds it.
3. Run them through the system.
4. For each, record: was the right document returned, was it first, was the answer correct, did it say "not found" when it should.
5. Read the failures against the five places above.

Do this before you change anything about the system, and again after. Ten questions will show you a pattern a hundred demos hide. It also gives you a regression test, so that when someone adds a thousand documents, you know within a minute whether the answers got worse.

Keep the questions with the brief. They are the acceptance test for the archive.

## Keeping the collection honest

Retrieval is only as current as the collection, so the collection needs an owner.

- Mark each document with a status: in force, draft, superseded.
- Record a review date and a person.
- Remove superseded versions from the search, or exclude them by status. Do not delete the history unless the retention rules say to. Move it out of the path.
- When a policy changes, the change is not finished until the index is updated. Put that step on the list that ships the policy.

That last line is the one that fails in practice. A new refund policy is published on the intranet on Monday. The index rebuilds on its own schedule, or by hand, or never. For two weeks the agent quotes the old one.

## When retrieval is the wrong tool

If the answer is a fact in a database, query the database. Do not search the prose that describes it. "What plan is Acme on?" is a read from the billing system, with a timestamp, not a paragraph from a document.

If the question needs reasoning across many documents, a single retrieval of five passages will not hold it. That is a research job, and Book 5 treats it as one, with sources checked one by one.

If the rule is short and critical, pin it. Do not make the loop go looking for something it must never forget.

Retrieval is a good way to give a loop the page it needs. It is a poor way to give it a conscience. That has to be written down, short, and kept current by a person.
