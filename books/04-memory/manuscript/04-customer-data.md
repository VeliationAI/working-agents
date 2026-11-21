---
kind: chapter
title: Customer data, retention, and deletion
---

A customer writes to support: "Please delete everything you have about me." Your support team has used an agent for four months. The agent drafted replies, kept a case file for each ticket, and a standing note says "remember each customer's preferences." Someone opens the admin screen, finds the customer's record, and clicks delete.

Is the customer's data gone?

Probably not. Their name is in last month's trace logs. A summary of their complaint is in the case file for a ticket that was merged into another. The agent's "preferences" memory still says they prefer phone calls. An export from the weekly quality review, sitting in a shared folder, includes three of their emails. The search index has chunks of their ticket history, and the index will not notice the source is gone until it rebuilds.

Memory is a set of copies. Deletion has to reach every copy, or it did not happen. This chapter is about knowing where the copies are before the day someone asks.

This is not legal advice. Laws about personal data differ by place and by industry, and they change. What follows is the engineering and operations habit that makes the legal answer possible. Ask your privacy or legal owner what you owe. Then use this chapter to find out whether you can deliver it.

## The rule of three questions

For every piece of customer data an agent can touch or store, you should be able to answer three questions.

1. **Why do we have it?** The purpose, in one sentence. "To answer support tickets." If the only answer is "it might be useful," you do not have a purpose.
2. **How long do we keep it?** A number, and what starts the clock. Thirty days after the ticket closes. Until the account closes plus ninety days.
3. **Who can delete it, and how do we know it is gone?** A named person or role, and a way to verify.

If any answer is missing, the data has no owner and no clock. A memory you cannot delete is a liability with a friendly name.

## Where the copies hide

Walk the five shelves and ask where personal data lands on each.

**The brief.** Usually light. A brief for a single ticket may contain the customer's name and account number. It exists for the length of the run. Check that saved briefs, templates, and examples do not contain real customer details. A "good example brief" that includes a real person's complaint is a copy.

**The trace.** Often heavy. Every tool result lands here: the ticket text, the billing record, the order history. If the harness stores traces for replay, those traces hold personal data for as long as you keep the logs. A trace you retain for a year for debugging is a year of customer records, copied.

**The case file.** Purposeful, and persistent. Summaries of a customer's situation, decisions, and contact preferences. Often rewritten by the agent in its own words, which makes it hard to search for by name alone.

**The standing notes.** Should not contain customer data. If a note says "Dana at Acme prefers phone calls," it is a case file entry on the wrong shelf. It will outlive the case, apply to no task, and be the hardest to find when a deletion request arrives.

**The archive and the index.** Past tickets, transcripts, documents. Plus the index built over them: chunks, and the lists of numbers that represent them. The index is a derived copy. Deleting the source ticket does not delete the chunk that was cut from it, or the representation of it, until the index is rebuilt or the entry is removed.

Then there are copies outside the shelves.

- **Exports.** Spreadsheets pulled for a review, pasted into a shared doc, attached to a message.
- **Caches.** Saved results the harness reuses to avoid repeating a call.
- **Backups.** Copies of the database kept for recovery. Usually deleted on a schedule rather than on request.
- **Evaluation sets.** The ten real questions you saved to test retrieval. If they came from real tickets, they hold real data.
- **Outside providers.** The model provider, the logging service, and the search service may each keep inputs for some period. Read their retention terms and record them. Do not assume.

You will not find all of these in one afternoon. Start with the list. Naming the copies is most of the work.

## Collect less

The cheapest deletion is the one you never need.

Before an agent stores or even sees customer data, ask what the job requires.

- A reply draft needs the ticket text and the plan. It rarely needs the customer's full address.
- A renewal brief needs invoice status. It does not need card details.
- A trend summary needs counts and categories. It does not need names.

Where you can, give the loop less. Mask what the job does not need. Replace a name with a customer ID in the case file. Use a read tool that returns only the fields the brief lists, not the whole record.

Reducing what is in view also reduces what can leak into a draft. An agent that never saw the customer's home address cannot paste it into an email to the wrong person.

Some data you should treat as off-limits to the loop unless there is a clear and reviewed reason: payment card numbers, government IDs, health information, authentication secrets. Do not rely on the agent to "remember not to repeat" them. Keep them out of reach of the tools.

## Give memory a clock

Most memory has no end date because nobody set one. Put a clock on each shelf.

```
SHELF           HOLDS                     KEPT FOR
Brief           Task instructions         The run
Trace           Actions and results       30 days, then deleted
Case file       Facts about one case      Case closed + 90 days
Standing notes  Preferences and rules     Reviewed every 6 months;
                (no customer data)        deleted when wrong
Archive         Closed tickets, docs      Per records schedule
Index           Derived from archive      Rebuilt weekly; removed
                                          chunks dropped on rebuild
Exports         Review spreadsheets       7 days, then deleted
```

The numbers above are examples. Pick your own, with the person who owns your records rules. The point is that each row has a number and something that makes the number true.

A clock needs a mechanism. "Delete after thirty days" is a wish until a scheduled job does it. If the deletion is manual, it will be skipped in the busy week. If it is automatic, test it. Create a dummy record, wait for the window, and confirm it is gone from every place on the list.

## The case file when the case ends

When a ticket, deal, or project closes, decide what happens to its case file.

There are four honest choices.

1. **Delete it.** Right for most operational memory. The record of what happened lives in the system of record, such as the ticket system, and not in the agent's notes.
2. **Archive it.** Keep it, read-only, in the archive with a status and a retention clock.
3. **Promote a lesson.** Extract something that is not customer-specific into a standing note, such as "Customers on legacy plans cannot upgrade mid-cycle." Strip names. Review it as you would any note.
4. **Keep it open.** Only when the case continues.

Do not let case files drift into permanent memory by default. A closed ticket that keeps shaping future answers is how the agent "remembers" a customer who left a year ago.

## What the agent may write to memory

A memory feature that lets the agent save things by itself is convenient and risky. It is the standing-notes shelf with nobody at the door.

Decide, per shelf, what the agent may write.

- **Trace:** yes, automatically.
- **Case file:** yes, as proposals or with a rule. Entries get a date and a source. Personal data in an entry is limited to what the case needs.
- **Standing notes:** no. A person adds notes.
- **Archive:** read only. Other systems write there.

If the agent proposes a standing note, such as "this customer prefers email," the right response is usually to put it in the customer record, in the system that owns the contact preferences, and not in the agent's memory. The agent can read it from there next time.

That is also the answer to "should the agent remember my preferences across chats?" Maybe. But the source of truth should be somewhere you can see, edit, and delete. A preference stored in a black box cannot be reviewed.

## Handling a deletion request

When the request comes, you want a procedure and not a scramble. Write it before you need it.

```
DELETION REQUEST PROCEDURE
Received: ______  Customer ID: ______  Owner: ______

1. Confirm identity and scope with the privacy owner.
2. Delete from the system of record.
3. Delete case files tied to this customer.
4. Delete or redact traces within retention.
5. Remove chunks from the search index; confirm after
   rebuild or by direct removal.
6. Find exports and shared documents that include the
   customer. Delete or redact.
7. Check standing notes and saved briefs for mentions.
8. Note backups: record when they expire.
9. Check outside providers with stored data; request
   deletion where required.
10. Record what was deleted, when, by whom, and what
    remains with a date it will go.
```

Step 10 is the one people skip and the one you will want. A deletion you cannot describe is a deletion you cannot defend.

Then test the result. Search your own systems for the customer's name, email, and ID. Ask the agent about the customer. If it still knows something, a copy remains.

## Retention is a design choice, not a loss

People resist deleting memory because it feels like throwing away value. Sometimes it is. A support agent with a history of past tickets can be better than one without.

The answer is not to keep everything. It is to keep what you can justify, label it, and delete the rest on a schedule. Historical tickets in an archive with a clear purpose, a clock, and an access list are fine. Unstructured summaries scattered across notes, traces, and exports are not.

A useful test: if you had to explain to the customer what you keep about them and why, could you? If the explanation is awkward, you have found the item to reconsider.

## A small audit for this week

1. Pick one agent that touches customer information.
2. List every place its inputs and outputs are stored. Use the shelves and the outside-the-shelves list above.
3. For each, write the purpose, the retention, and the person who can delete it. Mark gaps.
4. Pick the largest gap. It is usually trace logs or exports.
5. Set a clock on it and name the mechanism that enforces the clock.

You will probably leave with a list of things you did not know you stored. That is the right outcome. The agent did not create the problem. It made the problem visible.
