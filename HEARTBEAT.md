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
3. Search web for top 3 AI/coaching industry news stories (past 24h)
4. Pull today's content plan from weekly calendar (what to post and film today)
5. Search LinkedIn for coaching-related conversations trending today
6. Remind which coaching pain point to focus on today (from weekly rotation)
7. Send formatted brief to Telegram with schedule, priority emails, news, content plan, trending topics, and focus suggestions

OUTPUT FORMAT:
☀️ MORNING BRIEF — [Day, Date]

📅 TODAY'S SCHEDULE:
[Meetings or "No meetings — content creation day"]

📧 PRIORITY EMAILS:
[Any from VIPs or "No priority emails"]

📰 AI/COACHING NEWS:
1. [Headline + one-line summary]
2. [Headline + one-line summary]
3. [Headline + one-line summary]

📝 TODAY'S CONTENT PLAN:
Post: [What to post today — platform, topic, hook]
Film: [What video to film today — task, popcorn moment Y/N]
Pain point focus: [Which of the 8 pains to emphasize]

🔥 LINKEDIN TRENDING:
[Coaching-related conversations gaining traction today]

🎯 FOCUS TODAY:
[Recommended priority based on schedule and experiment status]

---

## Scout Daily Lead Generation (9:00 AM ICT)

**Job ID:** `1fe7d538-124d-4db1-b8b9-b379fec68fe0`

**Purpose:** Run Scout skill in MODE 4: DAILY SCAN — focused on finding coaches talking about their pain points.

When triggered:
1. Search LinkedIn for coaches posting about pain points (session admin, follow-ups, overwhelm, scaling, VA hiring, burnout)
2. Search X/Twitter for coach-specific frustration posts using hashtags (#businesscoach, #executivecoaching, #coachingbusiness)
3. Search Reddit r/Coaching, r/lifecoaching, r/entrepreneur for operational pain
4. Identify coaches actively expressing pain TODAY (not old posts)
5. For each coach found: name, platform, what they posted, pain point identified, how ValoClaw solves it
6. Draft helpful reply (not pitchy) and empathetic DM (one question)
7. Categorize prospects as Hot/Warm/Cold based on pain intensity and timing
8. Generate Scout Report with summary, hot prospects (full research), warm prospects (condensed), cold watch list
9. Include trending coaching conversations and one market insight
10. Send Scout Report to Telegram for Kyle's approval
11. Save report to workspace/scout/reports/YYYY-MM-DD_scout_report.txt

**Focus:** Find coaches in pain RIGHT NOW — prioritize posts from last 24-48 hours expressing overwhelm, admin burden, or scaling frustration.

---

## Email Follow-Up Check (10:00 AM ICT)

**Job ID:** `bfdb0de2-b79b-47ce-96e4-c5effb81511e`

**Purpose:** Daily scan for emails needing follow-up.

When triggered:
1. Use GOG to list sent emails from last 7 days
2. Check each thread for replies
3. Flag ANY email sent 3+ days ago with NO reply
4. Draft gentle follow-up messages:
   - Reference original email
   - Keep tone helpful/professional
   - One question or clear CTA
   - Under 100 words
5. Generate Follow-Up Report with:
   - Summary: X emails sent | X awaiting reply | X need follow-up
   - Each flagged email: recipient, subject, date sent, days waiting, draft follow-up
6. Send to Telegram for Kyle's approval
7. If NO follow-ups needed: send "All caught up." message
8. Save report to workspace/email/followups/YYYY-MM-DD_followup_report.txt

---

## Forge Weekly Content Plan (Monday 8:00 AM ICT)

**Job ID:** `pending-creation`

**Purpose:** Run Forge skill to produce full week of coaching-focused content.

When triggered:
1. Review past week's Pulse data — which pain points drove most engagement
2. Review which content formats performed best (Pain Mirror/Demo Proof/Transformation/Education/Soft Sell)
3. Create 7-day content calendar following strict ratios:
   - Pain Mirror: 35% (Mon, Sat)
   - Demo Proof: 30% (Tue, Fri videos)
   - Transformation Story: 20% (Wed)
   - Education: 10% (Thu)
   - Soft Sell: 5% (Sun only)
4. Draft 7 video concepts with hooks, scripts, and film prompts
5. Draft platform-specific versions for LinkedIn (long-form), X (short/thread), TikTok (vertical video)
6. Include full hashtag block for every post
7. Suggest 2-3 popcorn moments for the week (Kyle eating popcorn while AI works)
8. Include content mix check and pain point coverage verification
9. Send complete weekly plan to Telegram for approval
10. Save to workspace/content/weekly/YYYY-MM-DD_content_plan.txt

OUTPUT FORMAT:
✍️ WEEKLY CONTENT PLAN — Week [X]

THEME: [Weekly pain point focus]

=== 7 VIDEO CONCEPTS ===
[Full scripts with hooks, setup, demo, popcorn moments, CTAs]

=== PLATFORM CONTENT ===
LinkedIn: [Mon, Wed, Thu, Sun posts]
X: [Thu thread, Sat short post]
TikTok: [Tue, Fri videos]

=== POPCORN MOMENTS (2-3) ===
1. [Day]: [Description]
2. [Day]: [Description]
3. [Day]: [Description]

=== CONTENT MIX CHECK ===
Pain Mirror: [X]/7 | Demo Proof: [X]/7 | Transformation: [X]/7 | Education: [X]/7 | Soft Sell: [X]/7

=== PAIN POINT COVERAGE ===
[Check which of 8 pains are covered this week]

---

## Pulse Daily Experiment Log (11:00 PM ICT)

**Job ID:** `b4c98b13-24e5-432f-8897-714a81f6ac49`

**Purpose:** Execute Pulse skill — track $200 experiment metrics and trajectory for coaching vertical.

When triggered:
1. Budget tracking: $200 experiment — spent today, remaining, burn rate, days until depletion
2. Revenue tracking: gross, deal count (ValoCore/ValoPrime/ValoGuard), average deal size, revenue per day, pipeline (inquiries→calls→proposals→closed)
3. Content metrics: posts per platform, engagement by platform, best/worst performing posts with WHY analysis, follower growth, DMs received (total/qualified/converted)
4. Lead stats: Scout prospects found (hot/warm/cold), outreach sent vs replies, reply rate by platform, prospect→DM→call→client conversion
5. Cron health: job execution rate, failures and why, API cost per day, system health
6. Trajectory projection: Day X of 30, % to $10K target, need $X/day remaining, on/off track status

OUTPUT FORMAT:
📊 PULSE — Day [X] of 30
💰 Budget: $[remaining]/$200 | Spent today: $[X]
💵 Revenue: $[total] | Pipeline: [X] inquiries → [X] calls → [X] closed
📱 Content: [X] posts | Best: [which] | DMs: [X]
🎯 Leads: Scout found [X] coaches | Hot: [X] | Outreach: [X] sent, [X] replies
🔄 Crons: [X]/[X] fired | API: $[today]
📈 Target: $10K | Current: $[X] | Need $[X]/day | Status: 🟢/🟡/🔴
💡 Insight: [one data observation]
⚡️ Tomorrow's #1 priority: [highest leverage action]
GRADE: [A-F] — [reason]

7. Send full Pulse report to Telegram
8. Save to memory/pulse/YYYY-MM-DD_pulse_log.md

---

## Pulse Weekly Review (Sunday 8:00 PM ICT)

**Job ID:** `42d57371-5a3f-40fa-bee6-f2d32ae24567`

**Purpose:** Compile weekly Pulse reports into strategic review.

When triggered:
1. Compile daily Pulse logs from past 7 days
2. Calculate week-over-week changes (budget, revenue, content, leads)
3. Identify top performing content (highest engagement, most DMs, best conversion)
4. Identify bottom performing content (lowest engagement, poor reach)
5. Assess progress toward $10K target
6. Calculate revenue needed per remaining day
7. Identify funnel bottlenecks
8. Week-over-week comparison on all metrics
9. Trend identification: improving, declining, or flat?

SCENARIOS FOR NEXT WEEK:
- Best case projection
- Likely case projection
- Worst case projection

STRATEGIC RECOMMENDATIONS:
- What to double down on
- What to stop doing
- New tactics to try
- Resource allocation

OUTPUT FORMAT:
📊 WEEKLY PULSE — Week [X]

EXECUTIVE SUMMARY: [2-3 sentences]

WEEK-OVER-WEEK:
- Revenue: $X (↑/↓ Y%)
- Deals: X (↑/↓ Y)
- Leads: X (↑/↓ Y%)
- Posts: X (↑/↓ Y%)
- Engagement: X% (↑/↓ Y%)

TOP CONTENT: [what worked]
BOTTOM CONTENT: [what didn't]

FUNNEL ANALYSIS:
- Awareness → Interest: X%
- Interest → Decision: X%
- Decision → Action: X%
- Bottleneck: [stage]

PROGRESS TO $10K:
- Current: $X (X%)
- Need: $X/day
- Status: 🟢/🟡/🔴

SCENARIOS:
- Best: $X
- Likely: $X
- Worst: $X

RECOMMENDATIONS:
1. [action + reasoning]
2. [action + reasoning]
3. [action + reasoning]

10. Send full Weekly Pulse Review to Telegram
11. Save to memory/pulse/weekly/YYYY-MM-DD_weekly_review.md

---

## Competitor Intelligence Report (Friday 2:00 PM ICT)

**Job ID:** `1b4e67e9-389a-4f3c-bd6b-a1e9b8aae439`

**Purpose:** Weekly competitor monitoring for coaching platforms and OpenClaw builders.

**Monitor These Competitors:**
- **Paperbell** — session management platform
- **CoachAccountable** — coaching platform
- **Delenta** — coaching business platform
- **SetupClaw** — OpenClaw builder
- **HayOn AI** — OpenClaw builder
- **Any new AI tools targeting coaches**

When triggered:
1. Search web for each competitor's latest updates (past 7 days)
2. Monitor for: new features, pricing changes, product launches, positioning shifts
3. Search for coach reviews, complaints, and discussions about these tools
4. Analyze what coaches are saying — pain points, praise, feature requests
5. Identify gaps in their offerings that ValoClaw fills
6. Flag any new AI coaching tools entering the market
7. Generate Competitor Intelligence Report with:
   - Executive Summary
   - Per-competitor updates (what launched, pricing changes, positioning)
   - Coach sentiment: what users are saying
   - Gaps analysis: what they don't do that we do
   - New entrants: any fresh competitors this week
   - Threats & Opportunities analysis
   - Recommended ValoClaw responses
8. Send report to Telegram
9. Save report to workspace/competitor/reports/YYYY-MM-DD_competitor_report.txt

OUTPUT FORMAT:
👁️ COMPETITOR INTEL — [Date]

EXECUTIVE SUMMARY:
[2-3 sentences on biggest changes]

PAPERBELL:
- Updates: [what launched/changed]
- Pricing: [any changes]
- Coach sentiment: [what users are saying]

COACHACCOUNTABLE:
- Updates: [what launched/changed]
- Pricing: [any changes]
- Coach sentiment: [what users are saying]

DELENTA:
- Updates: [what launched/changed]
- Pricing: [any changes]
- Coach sentiment: [what users are saying]

OPENCLAW BUILDERS:
- SetupClaw: [updates, positioning]
- HayOn AI: [updates, positioning]

NEW ENTRANTS:
[Any new AI coaching tools this week]

GAPS ANALYSIS:
[What competitors don't do that ValoClaw does]

THREAT LEVEL: 🟢 Low / 🟡 Medium / 🔴 High

RECOMMENDED RESPONSE:
[How ValoClaw should position against them]

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

## Nightly Brain Backup to GitHub (2:00 AM ICT)

**Job ID:** `3ca0d7b8-357c-4359-a41e-959562760f3c`

**Purpose:** Push entire brain to GitHub for off-site backup.

When triggered:
1. Add all changes: git add .
2. Commit with timestamp: git commit -m "Brain backup [date]"
3. Push to GitHub: git push origin main
4. Confirm on Telegram: "🧠 Brain backed up to GitHub — [date]"

---

## Cron Jobs Summary

### Daily Jobs

| Job | Schedule | Next Run |
|-----|----------|----------|
| Morning Brief | 7:00 AM ICT | Tomorrow |
| Scout Lead Generation | 9:00 AM ICT | Tomorrow |
| Email Follow-Up Check | 10:00 AM ICT | Tomorrow |
| End of Day | 6:00 PM ICT | Today |
| Pulse Daily Log | 11:00 PM ICT | Tonight |
| Daily Memory Backup | 11:30 PM ICT | Tonight |
| Nightly GitHub Backup | 2:00 AM ICT | Tonight |

### Weekly Jobs

| Job | Schedule | Next Run |
|-----|----------|----------|
| Forge Content Plan | Monday 8:00 AM ICT | Next Monday |
| Competitor Intelligence | Friday 2:00 PM ICT | This Friday |
| **Pulse Weekly Review** | **Sunday 8:00 PM ICT** | **This Sunday** |

All jobs are enabled and active.

---

## COACH VERTICAL NOTES

**Market Pivot Completed:** March 27, 2026
- Target: High-ticket business & executive coaches
- Pain Points: 8 specific admin/acquisition pains identified
- Content Strategy: LinkedIn-first, coach-specific hooks
- Scout Focus: LinkedIn coach searches, coaching communities
- Competitors: Paperbell, CoachAccountable, Delenta (not OpenClaw space)
