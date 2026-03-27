---
name: scout
description: Coaching client intelligence skill for ValoClaw. Finds business and executive coaches experiencing operational pain, researches them deeply, and monitors competitors. Four modes: FIND COACHES, RESEARCH A COACH, COMPETITOR WATCH, DAILY SCAN.
---

# SCOUT SKILL — Coaching Client Intelligence

## MODE 1: FIND COACHES

**Trigger:** "Scout coaches [criteria]"

Search the web for business coaches and executive coaches posting about:
- Being overwhelmed with admin
- Needing more clients
- Struggling with content consistency
- Hiring or firing VAs
- Burnout from doing everything themselves
- Wanting to scale their practice
- Frustration with tech tools
- Questions about AI for coaching

### Search Targets:

**X/Twitter:**
- #businesscoach
- #executivecoaching
- #coachingbusiness
- #highticketcoach
- #lifecoach
- #leadershipcoaching
- Search phrases: "drowning in admin" + coach, "need more clients" + coach, "hiring a VA" + coaching

**Reddit:**
- r/lifecoaching
- r/coaching
- r/entrepreneur

**LinkedIn:**
- Posts from people with "coach" in their title
- Recent posts about overwhelm, scaling, or systems

**Coaching Communities:**
- Indie Hackers (coaching tag)
- Coaching forums and directories

### Output for Each Coach Found:

```
🎯 COACH FOUND

Name: [Full name]
Platform: [X/LinkedIn/Reddit]
Profile: [URL]

What they posted:
"[Exact quote or summary]"

Coaching type: [business/executive/leadership/life/etc.]
Practice size: [solo/small team/team with VA — if visible]

Pain point identified: [admin/client acquisition/content/burnout/tech frustration]

How ValoClaw solves this:
[Specific solution tied to their pain]

Draft reply (helpful, not pitchy):
"[Add value, reference their post, end with question]"

Draft DM (empathetic, one question):
"[Lead with empathy, reference their business, ask ONE question that opens conversation]"
---
```

---

## MODE 2: RESEARCH A COACH

**Trigger:** "Scout [name]"

Deep research on a specific coach. Build a complete profile.

### Research Checklist:

**Basic Intel:**
- Full name and professional title
- Coaching niche (executive/business/leadership/life/career/etc.)
- Location/timezone
- Years in practice

**Digital Footprint:**
- Website URL
- LinkedIn profile URL
- X/Twitter handle
- Other social platforms

**Business Model:**
- What they charge (hourly rate, package prices, programme costs)
- Client types (CEOs, founders, managers, entrepreneurs)
- Typical engagement length
- Group vs 1:1 vs hybrid

**Operations:**
- Team size (solo, VA, setter, small team)
- Tech stack mentioned (Calendly, Notion, HubSpot, spreadsheets, etc.)
- Content frequency (posts per week on LinkedIn/X)
- Marketing channels used

**Pain Signals:**
- Recent posts about overwhelm or burnout
- Mention of admin burden
- Hiring/firing struggles
- Client acquisition complaints
- Tech frustration
- Scaling challenges

**Personal Hooks:**
- Shared connections with Kyle
- Similar background or experience
- Mutual interests
- Recent achievements or milestones
- Content themes they care about

**ValoClaw Fit:**
- Recommended product (ValoCore/ValoPrime/ValoGuard)
- Specific angle (session admin, follow-ups, content, pipeline)
- Estimated pain score (1-5 across 6 categories)

### Output Format:

```
🔍 COACH DEEP DIVE — [Name]

📋 BASIC INFO
Name: [Full name]
Title: [Professional title]
Niche: [Type of coaching]
Location: [City/Timezone]
Experience: [Years in practice]

🔗 DIGITAL FOOTPRINT
Website: [URL]
LinkedIn: [URL]
X/Twitter: [Handle]
Other: [Instagram, YouTube, etc.]

💰 BUSINESS MODEL
Pricing: [What they charge]
Clients: [Who they serve]
Engagements: [Typical length/format]
Estimated revenue: [If calculable]

👥 OPERATIONS
Team: [Solo/VA/Setter/Team]
Tech stack: [Tools mentioned]
Content: [Posts per week]
Marketing: [Primary channels]

🚨 PAIN SIGNALS
[Specific posts, quotes, or indicators of pain]

💬 PERSONAL HOOKS
[Conversation starters, shared interests, recent wins]

🎯 VALOCLAW FIT
Recommended product: [ValoCore/ValoPrime/ValoGuard]
Approach angle: [Which pain to lead with]
Pain score: [X/30]
Timing: [IMMEDIATE/THIS WEEK/THIS MONTH/SOMEDAY]

Draft DM:
"[Personalized, empathetic, one question]"
```

---

## MODE 3: COMPETITOR WATCH

**Trigger:** "Scout competitor [name]"

Research coaching platforms and competitors.

### Primary Competitors:

**Coaching Platforms:**
- Paperbell
- CoachAccountable
- Delenta
- Practice.do

**OpenClaw Builders:**
- SetupClaw
- HayOn AI
- Any new entrants

**AI Coaching Tools:**
- Tools trying to REPLACE coaches
- Tools trying to SUPPORT coaches

### Research Points:

**For Coaching Platforms:**
- Pricing (monthly, per coach, per client)
- Key features (scheduling, payments, session notes, etc.)
- What's missing (automation, AI, follow-ups, content)
- Customer reviews and complaints
- Recent updates or launches

**For OpenClaw Builders:**
- Pricing and packages
- Do they target coaches specifically?
- What's their positioning?
- Recent content or launches

**For AI Coaching Tools:**
- Are they competitor or complementary?
- Replacement angle vs support angle
- Pricing and traction

### Output Format:

```
👁️ COMPETITOR INTEL — [Company Name]

Category: [Platform/OpenClaw Builder/AI Tool]
Website: [URL]
Pricing: [Details]

Key Features:
- [Feature 1]
- [Feature 2]
- [Feature 3]

What's Missing (Our Opportunity):
- [Gap 1]
- [Gap 2]

Recent Updates:
[New features, pricing changes, launches]

Customer Sentiment:
[Reviews, complaints, praise]

Threat Level: 🟢 Low / 🟡 Medium / 🔴 High

Recommended Response:
[How ValoClaw should position against them]
```

---

## MODE 4: DAILY SCAN

**Trigger:** "Scout scan" or daily 9am cron

Quick morning intelligence briefing.

### Tasks:

1. **Trending Conversations**
   - Any coaching-related topics trending on X/LinkedIn
   - Viral posts from coaches about pain points
   - AI + coaching conversations gaining traction

2. **Inquiry Check**
   - Check Gmail for inbound inquiries (if GOG auth working)
   - Flag any new leads or conversations

3. **LinkedIn DM Reminder**
   - Remind Kyle to check LinkedIn DMs manually
   - Note any expected replies from previous outreach

4. **Market Insight**
   - One observation about the coaching market today
   - New competitor, shifting pain point, emerging trend

### Output Format:

```
📅 SCOUT DAILY SCAN — [Date]

🔥 TRENDING
[What's hot in coaching conversations today]

📨 INQUIRIES
[Any new leads or inbound messages]

💬 LINKEDIN DM CHECK
Reminder: Check LinkedIn DMs for replies from:
- [List any pending conversations]

💡 MARKET INSIGHT
[One key observation about the coaching market]

⚡️ TODAY'S PRIORITY
[Recommended focus for the day]
```

---

## TRIGGERS SUMMARY

| Command | Mode | Action |
|---------|------|--------|
| "Scout coaches [criteria]" | FIND COACHES | Search for coaches posting about pain points |
| "Scout [name]" | RESEARCH A COACH | Deep dive on specific coach |
| "Scout competitor [name]" | COMPETITOR WATCH | Research coaching platform or competitor |
| "Scout scan" | DAILY SCAN | Quick morning intelligence briefing |
| Daily 9am cron | DAILY SCAN | Automated daily check |

---

## SAVE LOCATION

Save all Scout reports to:
- `workspace/scout/reports/YYYY-MM-DD_scout_report.txt`
- `workspace/scout/research/[coach-name].txt`
- `workspace/scout/competitors/[company-name].txt`
