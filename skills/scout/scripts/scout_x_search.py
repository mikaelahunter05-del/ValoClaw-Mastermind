#!/usr/bin/env python3
"""
Scout X API Integration (Standard Library Only)
Search Twitter/X for founder pain points and return structured leads.
"""

import os
import sys
import json
import urllib.request
import urllib.error
import urllib.parse
from datetime import datetime

# Load from .env manually (no external dependencies)
def load_env():
    env = {}
    env_path = '/data/.openclaw/workspace/.env'
    if os.path.exists(env_path):
        with open(env_path) as f:
            for line in f:
                if '=' in line and not line.startswith('#'):
                    key, value = line.strip().split('=', 1)
                    env[key] = value
    return env

env = load_env()
BEARER_TOKEN = env.get('X_BEARER_TOKEN', '')

# URL decode the bearer token (it's URL-encoded in the .env)
BEARER_TOKEN = urllib.parse.unquote(BEARER_TOKEN)

if not BEARER_TOKEN:
    print("ERROR: X_BEARER_TOKEN not found in .env", file=sys.stderr)
    sys.exit(1)

# API Headers
HEADERS = {
    "Authorization": f"Bearer {BEARER_TOKEN}",
    "Content-Type": "application/json"
}

# Search phrases for founder operational pain
SEARCH_QUERIES = [
    '"drowning in emails"',
    '"I need to hire an assistant"',
    '"founder burnout"',
    '"I need to automate"',
    '"I\'m the bottleneck"',
    '"my inbox is a nightmare"',
    '"working 14 hour days"',
    '"I need an AI employee"'
]

API_BASE = "https://api.twitter.com/2"

def make_request(url):
    """Make HTTP request using urllib."""
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=30) as response:
            return json.loads(response.read().decode())
    except urllib.error.HTTPError as e:
        print(f"HTTP Error {e.code}: {e.reason}", file=sys.stderr)
        if e.code == 401:
            print("Authentication failed. Check your Bearer Token.", file=sys.stderr)
        elif e.code == 429:
            print("Rate limit exceeded. Wait 15 minutes.", file=sys.stderr)
        return None
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return None

def search_recent_tweets(query, max_results=10):
    """Search for recent tweets matching query."""
    encoded_query = urllib.parse.quote(query)
    url = f"{API_BASE}/tweets/search/recent?query={encoded_query}&max_results={max_results}&tweet.fields=created_at,author_id,public_metrics"
    return make_request(url)

def get_user_info(user_id):
    """Get user profile information."""
    url = f"{API_BASE}/users/{user_id}?user.fields=username,description,public_metrics,location,verified"
    return make_request(url)

def analyze_prospect(tweet, user_data):
    """Score and analyze a prospect."""
    text = tweet.get('text', '').lower()
    user = user_data.get('data', {}) if user_data else {}
    
    # Pain scoring (1-5 each, total 30)
    pain_scores = {
        'email_overwhelm': 5 if any(x in text for x in ['email', 'inbox', 'emails']) else 0,
        'calendar_chaos': 3 if any(x in text for x in ['schedule', 'calendar', 'meeting']) else 0,
        'follow_up_failures': 4 if any(x in text for x in ['follow-up', 'missed', 'forgot']) else 0,
        'content_burden': 3 if any(x in text for x in ['content', 'posting', 'social media']) else 0,
        'hiring_frustration': 5 if any(x in text for x in ['hire', 'hiring', 'assistant', 'va']) else 0,
        'operational_chaos': 5 if any(x in text for x in ['bottleneck', 'overwhelm', 'drowning', 'burnout']) else 0
    }
    
    total_pain = sum(pain_scores.values())
    
    # Timing assessment
    if any(x in text for x in ['right now', 'urgent', 'help', 'drowning', 'killing me']):
        timing = "IMMEDIATE"
    elif any(x in text for x in ['need to', 'looking for', 'considering']):
        timing = "THIS WEEK"
    elif any(x in text for x in ['thinking about', 'maybe', 'someday']):
        timing = "THIS MONTH"
    else:
        timing = "SOMEDAY"
    
    # Scout Score
    if total_pain >= 20 and timing == "IMMEDIATE":
        score = "HOT"
    elif total_pain >= 15 or timing in ["IMMEDIATE", "THIS WEEK"]:
        score = "WARM"
    else:
        score = "COLD"
    
    username = user.get('username', 'unknown')
    return {
        'name': user.get('name', 'Unknown'),
        'username': username,
        'user_id': tweet.get('author_id'),
        'tweet_text': tweet.get('text'),
        'tweet_url': f"https://twitter.com/{username}/status/{tweet.get('id')}",
        'metrics': user.get('public_metrics', {}),
        'pain_score': total_pain,
        'timing': timing,
        'scout_score': score,
        'pain_breakdown': pain_scores,
        'created_at': tweet.get('created_at')
    }

def main():
    """Run Scout search and output results."""
    print("🎯 SCOUT REPORT — %s\n" % datetime.now().strftime("%B %d, %Y"))
    print("Searching X API for founder pain points...\n")
    
    all_prospects = []
    
    # Test with just 1 query first
    test_query = SEARCH_QUERIES[0]  # "drowning in emails"
    print(f"Searching: {test_query}...", file=sys.stderr)
    results = search_recent_tweets(test_query, max_results=10)
    
    if results is None:
        print("\n❌ API call failed. Check credentials or rate limits.", file=sys.stderr)
        sys.exit(1)
    
    if 'data' not in results:
        print(f"No results: {results}", file=sys.stderr)
        return
    
    print(f"Found {len(results['data'])} tweets", file=sys.stderr)
    
    for tweet in results['data']:
        user_id = tweet.get('author_id')
        user_data = get_user_info(user_id)
        
        if user_data and 'data' in user_data:
            prospect = analyze_prospect(tweet, user_data)
            all_prospects.append(prospect)
    
    # Sort by pain score descending
    all_prospects.sort(key=lambda x: x['pain_score'], reverse=True)
    
    # Separate by score
    hot = [p for p in all_prospects if p['scout_score'] == "HOT"]
    warm = [p for p in all_prospects if p['scout_score'] == "WARM"]
    cold = [p for p in all_prospects if p['scout_score'] == "COLD"]
    
    # Output Report
    print("SUMMARY: %d prospects | %d hot | %d warm | %d cold\n" % (
        len(all_prospects), len(hot), len(warm), len(cold)
    ))
    
    if hot:
        print("🔥 HOT PROSPECTS:")
        for p in hot[:3]:
            print(f"\n{p['name']} (@{p['username']}) — Platform: X | Profile: https://twitter.com/{p['username']}")
            print(f"What they said: \"{p['tweet_text'][:120]}...\"")
            print(f"Pain Score: {p['pain_score']}/30 | Timing: {p['timing']}")
            print(f"Public reply: \"What part of your workflow is eating the most time? IME it's usually the 'urgent but low-value' stuff that feels impossible to delegate.\"")
            print(f"DM draft: \"Saw your tweet about the operational grind — that specific bottleneck you mentioned trips up a lot of founders at your stage. If you could automate just one thing this week, what would it be?\"")
    
    if warm:
        print("\n\n🟡 WARM PROSPECTS:")
        for p in warm[:5]:
            print(f"\n{p['name']} (@{p['username']}) — Pain: {p['pain_score']}/30 | Timing: {p['timing']}")
            print(f"Tweet: {p['tweet_text'][:100]}...")
    
    if cold and len(cold) > 0:
        print(f"\n\n🧊 COLD WATCH LIST: {len(cold)} prospects")
        for p in cold[:3]:
            print(f"  - {p['name']} (@{p['username']})")
    
    # Save full data to JSON
    output_file = f"/data/.openclaw/workspace/scout_report_{datetime.now().strftime('%Y%m%d')}.json"
    with open(output_file, 'w') as f:
        json.dump(all_prospects, f, indent=2)
    print(f"\n\nFull report saved: {output_file}")

if __name__ == "__main__":
    main()
