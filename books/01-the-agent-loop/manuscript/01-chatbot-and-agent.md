---
kind: chapter
title: A chatbot answers. An agent finishes.
---

Start with a job, not a definition.

Find three recent papers on retrieval for customer-support agents, and write a one-page brief the team can read before Thursday's meeting. Mark anything you cannot verify.

A chatbot can draft that page if you paste the papers into the conversation. If you only type the sentence, the turn often ends with a fluent general essay, or with papers that were never published. The turn is over when the paragraph is over. Nothing in the setup goes and gets the papers.

An agent, given the same sentence and the means to act, treats the sentence as a job with a finish line. It searches. It opens the sources. It keeps the ones that match and drops the ones that do not. It writes the brief. It checks the brief against the sources. If a search fails, it tries a different query. If it cannot verify a claim, it says so, because you told it to.

That is the whole idea.

An AI agent is a model in a loop. The loop has a goal, a way to see the current situation, a way to act, and a way to decide whether the goal is met.

Memory, extra tools, a team of agents, a polished interface. All of that can be added. None of it replaces the loop. With no goal, no action, and no check, you have a conversation, however impressive the answers are.

## Four words worth separating

Product pages and meetings mix four words together. Separate them once and the rest of this book is easier.

A prompt is the instruction for a turn. It can be a sentence or a page. On its own, it does not go back for a second look.

A workflow is a path you fixed in advance. Step A, then step B, then step C. A model may write the text inside a step. The model does not choose the path. Workflows are the right design when you already know the path. They are easier to test, easier to explain, and usually cheaper to run.

An agent chooses the next action from what it just observed, inside boundaries you set. The path can differ from one case to the next. That flexibility is the reason to use an agent, and the reason an agent can wander.

An assistant is a product name. Some assistants are chatbots. Some are workflows with a chat window. Some are agents. The name on the homepage does not tell you which one you are looking at. The loop does.

## A test you can use in a meeting

If you can write the steps before you see the case, build a workflow.

If the steps depend on what the case contains, you are in agent territory. Then the work needs four things. A goal someone can check. A way to observe the facts. Tools no wider than the job. And a stop, including permission to come back and ask.

Summarize this PDF is a workflow, even when a model writes the summary. The material is already in hand. The path is one step.

Figure out why this customer is unhappy, and draft a reply I can send, using our policy and their tickets from the last 90 days. That job depends on what the tickets say. The next step is not knowable at the start. That is agent work. It is also work that should draft, and wait, before anything is sent.

You will see demos that take many steps and are still workflows. A chain of prompts that always searches, then always extracts, then always drafts, is a workflow with extra motion. It can be an excellent product. Call it a workflow and you will design it honestly. Call it an agent when some step is chosen because of what the previous step returned.

The chapters that follow take the loop apart. Goal. Observation. Action. Check. Then a page you can fill in before you run anything. Then the failures that show up when one of those pieces is missing.

You do not need to build software to use this. If you buy, manage, or turn these systems on, you need to know the finish line you handed them, and what they are allowed to touch while you are in another room.
