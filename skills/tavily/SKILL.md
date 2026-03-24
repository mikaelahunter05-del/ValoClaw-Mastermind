---
name: tavily
description: Web search via Tavily API. Use for deep research, competitor analysis, and real-time information gathering. Requires TAVILY_API_KEY environment variable.
metadata:
  openclaw:
    requires:
      env: [TAVILY_API_KEY]
---

# Tavily Web Search Skill

Search the web using Tavily's AI-native search API.

## Usage

```bash
openclaw skill tavily search "your query"
```

## Environment

- `TAVILY_API_KEY` - Your Tavily API key (required)

## Features

- AI-curated search results with source citations
- Supports search depth: basic or comprehensive
- Max results configurable (1-20)

## Security Notes

- API key is read from environment only—never hardcoded
- No external scripts or eval() patterns
- Direct HTTPS API calls only