---
kind: chapter
title: The loop
---

Draw the loop as four beats.

1. Goal. What done looks like, in a form that can be checked.
2. Observe. Read the current state. A message, a file, a search result, an error, a row in a table.
3. Act. Call a tool, write a draft, ask a question, or stop.
4. Check. Compare what you have with the goal. Continue, repair, or hand the work back.

Then repeat.

The model does not hold a private intention. At each beat it predicts a next action from the goal, the history of this loop, and the latest observation. The software around the model is what makes the prediction matter. That software sends the tool call, stores the result, puts the goal back in view, and refuses to treat a half answer as the end.

People call that surrounding software a harness, a runtime, or an agent framework. The name matters less than the job. The purpose you experience lives in the loop you designed, in the goal you wrote, and in the limits you set.

## A small loop, all the way through

Goal: rename a file called report-final-FINAL-v3.docx to the team pattern, and report the new name. The pattern is the date, then the topic, then .docx, with the date written as year, month, and day. Do not invent the date. If the date is not in the document, stop and ask.

Observe: the folder contains that file. The document says the review meeting was held on 2 March 2026. The topic line says Q1 pipeline.

Act: rename the file to 2026-03-02-q1-pipeline.docx.

Check: the new file exists, the old name is gone, the name matches the pattern, and the date came from the document. Stop. Tell the person the new name.

A system that only talks would suggest the new name and leave the file as it is. The loop above includes an action on a real file. That is the difference you can point to.

A trace is the list of those beats, kept so a person can replay the run.

```
Goal. Rename the file to the team pattern. Do not invent the date.
Observe. One matching file. The document includes 2 March 2026 and the topic Q1 pipeline.
Act. Rename to 2026-03-02-q1-pipeline.docx.
Check. New name exists. Old name is gone. Date came from the document. Pattern matches.
Handback. Renamed to 2026-03-02-q1-pipeline.docx.
```

If you cannot replay a run, you cannot explain a mistake. Ask for a trace before you trust a system with anything that is hard to undo.

## Two loops, both designed

The inner loop is one beat sequence. Observe, act, check.

The outer loop is the job. Keep going until the goal is met, or until a limit is hit.

Limits belong in the design from the start. A maximum number of steps. A maximum cost. A maximum time. The list of tools that may be called. The topics that are out of bounds. A loop without limits will keep finding a reason to continue, because "not finished" is always available as a next thought. Continuing spends money, overwrites work, or walks into a task you did not mean to assign.

Stopping to ask is a successful ending. The date is not in the document. I need it before I rename the file. You want that outcome. A guessed date can pass a careless check and fail you later, in someone else's folder, with your name on the action.

## Thinking longer is a different feature

A model can spend more computation on a single answer and still end the turn with nothing done in the world. Extra thinking can make the next act a better act. The loop is what lets a second act happen after the first result comes back. Hard jobs often need both. Any job that requires looking, then looking again, needs the loop.

When you evaluate a tool your team might buy, ask to see a trace of one real task. Goal, observation, action, check, and the next beat. If the vendor can show only a final paragraph, you have seen an answer. Answers can be excellent. They are a different product, with a different risk, and a different way to supervise them.
