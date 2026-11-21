# Books 2 through 8

These are outlines, not manuscripts. Each book should stay under 12,000 words and should open with a job, the way Book 1 does. Write the next one after Book 1 sounds like you.

The chapter lists are a starting cut. Drop a chapter if it repeats Book 1. Add a chapter only when you have an example from work you have actually seen.

## Book 2. Briefing an Agent

A bad brief is a mood. This book is the craft of the one-page brief, across jobs that are not the Thursday renewal call.

1. The brief is the product, before any tool is chosen.
2. Context you forget you have, because you have worked there for years.
3. Acceptance tests a person will really apply.
4. Examples: research, support, and a software change.
5. A brief for a job you repeat every week.
6. How a brief becomes a prompt, a standing note, and a checklist without becoming three different instructions.

## Book 3. Tools and Permissions

1. Read, draft, and write are different products.
2. Least privilege as a tool list, not a slogan.
3. Approval is a tool the loop waits on.
4. Browser and computer-use tools, and why the stop gets stricter.
5. Secrets the loop should never see.
6. A log you can replay on Monday after a bad Friday.

## Book 4. Memory

1. The five shelves, with examples that rot.
2. Retrieval, and what people mean by RAG, without a vendor tour.
3. Contradiction: when a standing note fights today's brief.
4. Customer data, retention, and deletion.
5. When to start a fresh thread.
6. A memory policy you can put on one page.

## Book 5. Agents at Work

One pattern per job: goal, tools, check, stop, and a handback. No pattern without a failure mode.

1. Research and briefing.
2. Drafting and editing in a house style.
3. Operations and back office.
4. Customer support.
5. Preparing a software change.
6. How to tell a workflow wearing an agent costume.

## Book 6. When the Loop Goes Wrong

1. How to read a trace.
2. Ten real tasks is an exam. You do not need a benchmark.
3. Graders: a program, a model, a person, and what each one is good for.
4. What breaks when you "just tweak the prompt."
5. Writing up an incident so the next brief contains the test.
6. When to take the tools away and go back to a workflow.

## Book 7. More Than One Agent

1. The goal is still singular. Extra agents do not invent one.
2. Handoffs and the state you must pass across.
3. Roles that earn their keep, and roles that are a diagram.
4. Cost, debugging, and whose trace you read first.
5. A team of agents for a job that actually needs one.
6. The default remains one loop.

## Book 8. Shipping an Agent

1. From your laptop to a colleague's Tuesday.
2. A cost ceiling and what happens when you hit it.
3. Falling back to a workflow without apologizing.
4. What you tell a user the loop will and will not do.
5. Changing the brief without breaking yesterday's jobs.
6. Support: who answers when the handback is wrong.

## A template for the day you start Book 2

Copy `templates/book.yaml` into `books/02-briefing-an-agent/book.yaml`. Copy `templates/chapter.md` for each chapter. Point `tools/booklib.py` at the new folder only when you are ready to build it. Until then, keep Book 1 as the book the scripts build, so a LinkedIn post never links a half-generated PDF of the wrong volume.
