---
name: excalidraw-recap
description: Excalidraw diagram of work done — create or update a .excalidraw file that recaps a session (XRPL/MCP transactions, brainstorming, client meeting, system design). Use when the user asks for an Excalidraw diagram, to "excalidraw this", or to update an existing .excalidraw file.
---

# Excalidraw Recap

Turn a body of work into a **recap** diagram: a picture someone who wasn't there can read in under a minute. The `.excalidraw` file is the source of truth; an Excalidraw MCP server, when installed, is a second view onto it.

## Steps

1. **Gather the facts.** Sources, in order: what the user points at (files, notes, transcripts, links), this conversation's tool calls and results, and any record of past work a connected tool keeps (MCP memory or flow records, tickets, meeting notes). List every actor, artifact, decision, and event that belongs in the recap. Done when each fact has a source you can name; drop anything you would have to guess.

2. **Redact.** Credentials never enter the diagram: passwords, API tokens, private keys, seeds, connection strings. Public identifiers stay (addresses, IDs, hashes, ticket numbers, URLs). If the work involves a client or other outside party, ask whether to keep their names or use placeholders.

3. **Pick the target file.** Diagrams live in `~/excalidraw/`; list existing ones, newest first, with `ls -t ~/excalidraw/*.excalidraw`. Take the first rule that matches:
   - **Path given** → use it: update it if it exists, create it otherwise.
   - **Update asked** ("update", "add to", "extend", or a diagram named) → update the matching diagram; if more than one could match, ask which.
   - **Otherwise**: no diagrams yet → create `~/excalidraw/<kebab-topic>.excalidraw`. Diagrams exist → ask once, listing them newest first with their age: update one of them, or create a new one?

   Done when exactly one file path is settled.

4. **Pick the shape** from the work type (one primary shape per diagram):
   - **Flow** — steps or systems acting on each other (API calls, blockchain transactions, pipelines): actors and resources are nodes, actions are labelled arrows in execution order.
   - **Sequence** — multi-party exchanges (agent ↔ MCP ↔ ledger, client ↔ us ↔ partner): lifelines left to right, messages top to bottom.
   - **Mind map** — brainstorming: central idea, branches per theme, leaves per idea; decisions and open questions colour-coded.
   - **Timeline** — client sessions and project summaries: phases left to right, outcomes and next steps beneath.
   - **Architecture** — system design: components grouped by boundary, arrows for data flow.

   Every diagram also gets a title, a date, and a short **Outcome / Next steps** note.

5. **Write the diagram.** Read [FORMAT.md](FORMAT.md) first; it holds the file schema, layout grid, colours, and the update rules.
   - Creating → write the full file.
   - Updating → **preserve + extend**: every existing element keeps its id, position, and style; new work goes in a new region beside the current bounding box; edit an existing element only when a fact it shows has changed.

6. **Check.** Run `python3 <this-skill-dir>/scripts/check.py <file>`. Done when it prints `OK`. Fix and re-run on any error.

7. **Mirror to MCP (optional).** If a tool whose name contains `excalidraw` is available, push the same elements through it so the user sees a live canvas. The file stays authoritative; when the two differ, the file wins.

8. **Report** the file path, the shape chosen, what was added or changed, and how to open it: drag the file onto https://excalidraw.com or open it with the VS Code Excalidraw extension.
