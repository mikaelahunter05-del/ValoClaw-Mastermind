---
name: memory
description: Complete memory system with auto-capture, keyword search, and context recovery. Stores facts, decisions, and insights with fast retrieval.
metadata:
  openclaw:
    requires:
      files: [memory/memories.jsonl]
---

# Memory Skill — Complete Memory System

Store and retrieve important information with automatic capture, keyword search, and context recovery.

## Features

- **Auto-capture**: Save facts, decisions, contacts, ideas automatically
- **Keyword search**: Fast full-text search across all memories
- **Context recovery**: Rebuild session context from stored memories
- **Categorized storage**: facts, decisions, contacts, ideas, tasks, revenue

## Usage

```bash
# Store a memory
openclaw skill memory remember "Kyle's birthday is March 15" --category personal

# Search memories
openclaw skill memory search "birthday"

# List recent memories
openclaw skill memory list --limit 10

# Recover context
openclaw skill memory recover

# Show stats
openclaw skill memory stats
```

## Categories

- `fact` - General facts and information
- `decision` - Decisions made
- `contact` - People and leads
- `idea` - Ideas and insights
- `task` - Tasks and todos
- `revenue` - Revenue ideas and business opportunities
- `personal` - Personal information about Kyle

## Storage

Memories stored in `memory/memories.jsonl` (append-only, never overwritten)