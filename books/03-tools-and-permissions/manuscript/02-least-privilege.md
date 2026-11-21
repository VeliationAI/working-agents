---
kind: chapter
title: Least privilege as a tool list
---

An intern joins the finance team. On day one, IT gives them administrator access to every system, "to make things easy." Nobody means harm. Three weeks later, a spreadsheet is overwritten, and nobody can say who did it.

Everyone recognizes this as a mistake for a person. For an agent, it is often the default setup.

Least privilege is an old idea from security. Give each person, and each program, exactly the access the job needs and no more. For an agent, the idea becomes concrete. The privilege is the tool list. Nothing is hidden in a tone of voice. If a tool is not on the list, the loop cannot use it.

## The slogan is not the work

"We follow the principle of least privilege" is easy to say and hard to check. The work is a list, and the list has four properties.

1. Every tool is named in plain language, with its level: read, draft, or write.
2. Every tool is scoped: which folder, which table, which account, which fields.
3. Every tool has a reason, written as the job step that needs it.
4. Tools not on the list stay off, including ones that would be convenient.

You can audit a list like that in ten minutes. You cannot audit a slogan.

## The scoping questions

For each tool, answer these before it goes on the list.

- **Which data can it reach?** One folder or the whole drive? One customer's records or all of them? The last 90 days or everything?
- **Which actions can it perform?** Search only, or search and export? Edit one field, or any field?
- **Whose identity does it act as?** A shared account with broad rights, or a dedicated account created for this job?
- **How much can it do per run?** Ten reads or ten thousand? One draft or unlimited?
- **Where does the output go?** Back to the loop only, or to another system?

The third question deserves care. If the loop uses your personal login, it has all your access, including the access you forgot you had. Give the loop its own account, with its own limited rights. When something happens, the log shows the loop's name, not yours.

## A worked list

Take the competitor research job from Book 2. Here is its tool list.

```
TOOLS FOR: competitor release-notes research

1. fetch_page  (read)
   Fetches one URL and returns the text.
   Scope: only the three release-note URLs named in the brief.
   Why: the job reads three pages.
   Never: logs in, follows links off these domains.

2. search_our_docs  (read)
   Searches our public documentation.
   Scope: public docs only. No internal wiki.
   Why: to check whether we have an equivalent.

3. save_draft_document  (draft)
   Saves a document to the folder "Research drafts".
   Scope: that folder only. Cannot share. Cannot overwrite.
   Why: the output is a one-page draft.

NOT ON THE LIST
- Web search of the open internet. The brief names the sources.
- Any email or chat tool. Nothing in the job needs to reach people.
- Any file tool outside "Research drafts".
```

The "not on the list" block is as important as the list. It records decisions. When someone asks next month whether the agent could also post to the team channel, the page shows that the question was already considered and refused, with a reason.

## Narrow tools beat wide ones with a rule

You can try to get safety by giving the loop a wide tool and a rule: "You have file access, but only touch the research folder." That works until it does not. Rules in a prompt are requests. They can be ignored, misread, or pushed aside by text the loop reads along the way.

A narrow tool does not rely on obedience. A tool that can only write to one folder cannot write to another, however the loop reasons. Prefer a restriction that is enforced by the tool to one that is requested in the prompt.

When you cannot narrow the tool, enforce the boundary in the layer around it: a check that rejects any call outside the allowed path before it runs. If you are not the engineer, this is a sentence you can put in a request: "Please enforce this at the tool, not in the prompt."

## Start at zero and add

The safest process for building a list runs in one direction.

1. Start with no tools.
2. Write the brief, and list the facts the loop needs that it cannot get without a tool.
3. Add the narrowest read tool that retrieves each one.
4. Run the job and read the trace. Note where it needed something it did not have.
5. Add a draft tool for the output.
6. Run for a week, in review.
7. Only then consider whether any write tool is worth its risk.

Each addition should be a decision you can explain. The common failure runs the other way: start with everything connected, and remove tools after an incident.

## Reviewing the list

Put the tool list on a calendar, next to the brief's review from Book 2.

- **Monthly**, ask for each tool: was it used in the last month? A tool that was never called is a tool that does not need to be there. Remove it.
- **After any incident**, ask which tool made the incident possible, and whether a narrower one would have avoided it.
- **When the job changes**, rewrite the list from zero rather than editing it. Edited lists accumulate leftovers.

Keep the list in the same file as the brief, or one click away. A list nobody can find is a list nobody reviews.

## Who owns it

A tool list needs a named owner, in the same way a standing note does. The owner is the person who can say yes or no to a new tool, and who gets asked when something goes wrong. If no one owns it, everyone assumes someone else approved the last addition.

If you are not the builder, ask who owns the tool list. If nobody can answer, treat the agent as having every tool it can reach.

## What to do with this chapter

Take the list you made in the previous chapter. For every tool, write the scope in one line, and the reason in one line. Cross out any tool whose reason you cannot write.

Then write the "not on the list" block, with at least three items you were tempted to add. Date the page, name the owner, and put the first monthly review in the calendar.
