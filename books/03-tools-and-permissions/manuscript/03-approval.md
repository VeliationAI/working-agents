---
kind: chapter
title: Approval is a tool the loop waits on
---

The loop has drafted a reply to a customer who was charged twice. It is a good draft. It is also ready to send, and the tool to send it is one call away.

What happens next is a design decision, not a matter of the model's character. Either the loop sends, and you find out later. Or the loop stops, a person reads the draft, and the person lets it through.

Book 1 said that approval is a tool the loop waits on. This chapter is how to build that so it is real.

## Approval is part of the tool list

An approval step is not a policy hung beside the system. It is a tool, with a name, an input, and an output. The loop calls it, and then it waits.

```
TOOL: request_approval  (draft)
Input:  the action to be taken, the exact content, and the reason.
Output: approved, rejected with a note, or no answer.
Effect: nothing else happens until an answer arrives.
```

The write tool, in turn, is built so that it will not run without a matching approval. The loop cannot send a message that no person has approved, because the send tool checks for the approval record. That check lives in the tool, not in the prompt.

Compare two designs. In one, the prompt says, "Always ask the user before sending." In the other, the send tool refuses any call that lacks an approval ID. The first depends on the loop remembering. The second does not.

## What the person must be shown

An approval is only as good as what the approver sees. A button that says "Approve action?" with no detail is a rubber stamp.

A real approval screen shows five things.

1. **The exact action.** Send this message, to this address, from this account.
2. **The exact content.** The full text, not a summary of it.
3. **The reason.** Which step of the brief led here, in a sentence.
4. **The evidence.** The sources the content relies on, linked.
5. **What cannot be undone.** A plain line: "This sends an email. It cannot be recalled."

The last one is easy to omit and it changes behavior. A person who sees "cannot be undone" slows down.

The approver should also be able to edit. Often the right answer is not yes or no but "yes, after I change the second sentence." If the loop must start over for every edit, people will accept imperfect drafts to avoid friction. What the person approves must be exactly what runs. If they edit the draft, the action uses the edited version, and the log records both.

## Approval fatigue

The failure that spoils approvals is not malice. It is boredom.

Imagine fifty approvals a day. By the thirtieth, the approver is clicking. The system has a human in the loop in the diagram, and no human in the loop in practice.

Defenses that help.

- **Approve less, but approve what matters.** Keep read and draft actions free of approval. Reserve approval for writes. An approver who sees five requests a day will read them.
- **Rank by risk.** An approval to send to one known colleague is lighter than an approval to send to a customer list. Show the risk on the screen.
- **Sample.** For repeated low-risk writes, a person can review a sample after the fact. Be honest that this is after the fact, and that the first week is always before the fact.
- **Make rejection easy and informative.** A rejection with a note is training data for your brief. Count them. A high rejection rate means the brief or the tests are wrong. A rejection rate of zero for weeks is also a signal: either the work is excellent, or no one is reading.

## When nobody answers

Decide in advance what the loop does when no approval arrives. There are three honest choices.

- **Wait, then expire.** The request lapses after a set time. The loop reports it as not done. This is the safe default.
- **Escalate.** A named second person is asked. This works when the job has a deadline.
- **Never proceed by default.** Silence is not consent. A loop that takes a missing answer as a yes will, eventually, send the wrong thing during a holiday.

Write this in the brief's STOP section: "If no approval arrives within 24 hours, stop and report. Do not send."

## Who may approve

Not everyone should be able to approve every action. Decide who can approve what, and write it down.

- A support agent can approve a reply draft to a customer.
- Only the policy owner can approve a refund.
- Two people must approve a change to billing records.

The loop should not know who tends to say yes. It should not be able to choose its approver. The approver is set by the action type, in the harness, not by the loop's judgment.

Also check that the person approving is not the loop. This sounds absurd, but it happens when one account is shared by the human and the agent. Give the loop its own identity, as the previous chapter suggested, so the approval record names a person.

## Approval is not a check

It is worth being clear about what approval does and does not do. A person who approves a message is accepting responsibility for the action. That is useful. It is not the same as verifying the content.

Book 1's check, comparing the result against the goal, happens before the request is made. By the time the person sees the draft, the tests from the brief should have passed, and the approval screen should say so: "Tests: 6 of 6 passed. Unknown: 1." The person's time then goes into the judgment that tests cannot make, such as tone, timing, and relationship.

An approval step with no tests behind it asks a person to do the entire check in a few seconds. That fails quietly.

## Where approval is overkill

A system that asks permission for everything gets ignored. Some actions do not need a person.

Reading a file. Saving a draft to a private folder. Running a test on a branch. Writing to the loop's own scratch space. These are reversible and contained. Asking for approval on them teaches the approver to click without looking, which damages the approvals that matter.

Use the rule: if you can undo it before anyone else sees it, no approval. If you cannot, approval.

## What to do with this chapter

Find the writes on your tool list from the previous chapters. For each, sketch the approval screen: the five things the approver sees. If you cannot fill in one of them, the loop is not ready to ask.

Then write the no-answer rule in your brief's STOP section, and name who may approve each write. Last, make sure the write tool refuses to run without an approval ID, and test that it does.
