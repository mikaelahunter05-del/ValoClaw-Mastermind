---
summary: "Daily heartbeat tasks for Valo"
read_when:
  - Heartbeat poll fires
---

# HEARTBEAT.md — Valo's Daily Tasks

This file defines automated tasks that run on schedule via cron jobs.

---

## Morning Brief (7:00 AM ICT)

**Job ID:** `beaedecf-e467-413d-8f86-c6fb220d8419`

1. Check Google Calendar for today's meetings
2. Scan Gmail for urgent emails from VIP contacts (Michelle Hilling, Kenji Watabe)
3. Search web for top 3 AI/OpenClaw news stories (past 24h)
4. Send formatted brief to Telegram with schedule, priority emails, news, and focus suggestions

---

## End of Day Summary (6:00 PM ICT)

**Job ID:** `c6e8ced1-5fdc-41d1-908e-578e5919d560`

1. Review everything discussed during the day
2. List tasks completed on Kyle's behalf
3. Flag anything pending or waiting on Kyle
4. Suggest 3 priorities for tomorrow based on patterns

---

## Daily Memory Backup (11:30 PM ICT)

**Job ID:** `4fc0c8ab-c3f2-4f15-8735-df1c1d983275`

**Purpose:** Memory backup — runs every night so nothing is ever lost.

When triggered:
1. Save today's full conversation summary to memory/[date].md
2. Save any updates to MEMORY.md
3. Confirm the save on Telegram with: "💾 Memory saved for [date]"

---

## Cron Jobs Summary

| Job | Schedule | Next Run |
|-----|----------|----------|
| Morning Brief | 7:00 AM ICT | Tomorrow |
| End of Day | 6:00 PM ICT | Today |
| Daily Memory Backup | 11:30 PM ICT | Tonight |

All jobs are enabled and active.
