---
name: context-anchor
description: Recovers context after compaction by scanning memory files. Automatically loads MEMORY.md and recent daily logs to restore full operational context.
metadata:
  openclaw:
    requires:
      files: [MEMORY.md, memory/*.md]
---

# Context Anchor Skill

Restores full operational context after session resets or context compaction.

## What It Does

1. Reads MEMORY.md for permanent business context
2. Scans memory/ directory for daily logs
3. Loads the 3 most recent daily memory files
4. Rebuilds full context before proceeding with tasks

## Usage

```bash
openclaw skill context-anchor restore
```

Or run automatically at session start.

## Files Scanned

- `/workspace/MEMORY.md` — permanent business context
- `/workspace/memory/YYYY-MM-DD.md` — daily operational logs (last 3)

## Security

- Read-only operations
- No external network calls
- No credential access
- Local filesystem only