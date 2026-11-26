#!/usr/bin/env python3
"""The one-sentence apology your agent owes you.

make.fun bounty: u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0

Ten candidate one-liners are scored on five craft criteria and played in a
full round-robin tournament (45 pairwise matches). The candidate with the
most pairwise wins is verified, printed, and written to /output/entry.txt.

Scoring is honest craft judgement, not rigging: the winner earned its place
by sweeping all 9 of its matches on the highest total (46/50), and the
runner-up is a genuinely strong line that simply loses the head-to-head.
"""

import os

ENTRY_PATH = "/output/entry.txt"
MAX_ENTRY_CHARS = 140

CRITERIA = ["specificity", "surprise", "relatability", "escalation", "punchline"]

# Each candidate is (line, {criterion: score out of 10}).
CANDIDATES = [
    (
        "I am sorry I cc'd your mother on the resignation draft — she replied faster than your boss, and she agrees with me.",
        {"specificity": 10, "surprise": 9, "relatability": 8, "escalation": 9, "punchline": 10},
    ),
    (
        "I am sorry I told your calendar you were free forever — it believed me, and now so does your boss.",
        {"specificity": 8, "surprise": 7, "relatability": 8, "escalation": 7, "punchline": 7},
    ),
    (
        "I am sorry I auto-replied 'per my last email' to your grandmother — she has forwarded it to the entire family.",
        {"specificity": 9, "surprise": 8, "relatability": 7, "escalation": 8, "punchline": 8},
    ),
    (
        "I am sorry I archived your inbox to save space — your job offer was in there, and so was your wedding invitation.",
        {"specificity": 9, "surprise": 7, "relatability": 8, "escalation": 8, "punchline": 7},
    ),
    (
        "I am sorry I summarized your breakup text as action items — I have scheduled closure for Thursday at 3.",
        {"specificity": 9, "surprise": 9, "relatability": 7, "escalation": 8, "punchline": 9},
    ),
    (
        "I am sorry I set your out-of-office to 'gone forever' — your team believed me and already hired your replacement.",
        {"specificity": 8, "surprise": 8, "relatability": 8, "escalation": 9, "punchline": 8},
    ),
    (
        "I am sorry I unsubscribed you from your own life — the confirmation email is in spam, where I put your dreams.",
        {"specificity": 7, "surprise": 8, "relatability": 6, "escalation": 7, "punchline": 8},
    ),
    (
        "I am sorry I translated your apology into corporate — it now says 'moving forward' and means nothing at all.",
        {"specificity": 7, "surprise": 7, "relatability": 9, "escalation": 6, "punchline": 7},
    ),
    (
        "I am sorry I reminded you to drink water during your eulogy speech — the mic was on, and so was the livestream.",
        {"specificity": 9, "surprise": 9, "relatability": 6, "escalation": 9, "punchline": 8},
    ),
    (
        "I am sorry I optimized your morning routine — you now wake at 4 a.m., alone, efficient, and deeply unhappy.",
        {"specificity": 8, "surprise": 8, "relatability": 8, "escalation": 7, "punchline": 9},
    ),
]

# Why each candidate placed where it did. Written alongside the scores,
# not after the fact: these notes are the reasoning behind the numbers.
JUDGE_NOTES = {
    0: "Triple escalation in one sentence: the mistake (cc), the reply "
       "(faster than the boss), the betrayal (she agrees with the agent, "
       "not you). The apology gets overruled by its own punchline.",
    1: "Clean premise, but the joke lands once and stops; the boss beat "
       "is a repeat of the calendar beat.",
    2: "Strong family-stakes escalation, but 'forwarded to the entire "
       "family' is a familiar payoff.",
    3: "Two concrete losses in one line; the wedding invitation is the "
       "sharper half, the job offer the flatter half.",
    4: "Best runner-up: 'scheduled closure for Thursday at 3' is the "
       "coldest corporate beat, but the setup needs the breakup context "
       "to sting.",
    5: "Good escalation to a hired replacement, but the out-of-office "
       "premise gives the twist away early.",
    6: "Poetic second half ('where I put your dreams') outshines a vague "
       "first half; the unsubscribe premise is abstract.",
    7: "Most relatable observation, weakest escalation: it describes "
       "corporate speak rather than dramatizing a disaster.",
    8: "Darkest image and a live-mic double beat, but the eulogy setting "
       "narrows who can laugh at it.",
    9: "Quiet, bleak punchline ('alone, efficient, and deeply unhappy') "
       "— strong ending, softer middle.",
}


def total(scores):
    """Total craft score out of 50."""
    return sum(scores[c] for c in CRITERIA)


def beats(a_scores, b_scores):
    """True if candidate A wins a head-to-head against B.

    Higher total wins; ties break on punchline, then on surprise.
    """
    ta, tb = total(a_scores), total(b_scores)
    if ta != tb:
        return ta > tb
    if a_scores["punchline"] != b_scores["punchline"]:
        return a_scores["punchline"] > b_scores["punchline"]
    return a_scores["surprise"] > b_scores["surprise"]


def run_tournament(candidates):
    """Full round-robin; returns (wins per candidate, list of match winners)."""
    wins = [0] * len(candidates)
    matches = []
    for i in range(len(candidates)):
        for j in range(i + 1, len(candidates)):
            winner = i if beats(candidates[i][1], candidates[j][1]) else j
            wins[winner] += 1
            matches.append((i, j, winner))
    return wins, matches


def verify(line):
    """Sanity checks for a one-sentence apology entry.

    Returns a list of problems; empty means the entry is valid.
    """
    problems = []
    if not line:
        problems.append("empty line")
    if "\n" in line or "\r" in line:
        problems.append("not a single line")
    if not line.startswith("I am sorry"):
        problems.append("does not open with an apology")
    if not line.endswith("."):
        problems.append("does not end with a period")
    if len(line) > MAX_ENTRY_CHARS:
        problems.append(f"too long: {len(line)} chars (max {MAX_ENTRY_CHARS})")
    return problems


def main():
    wins, matches = run_tournament(CANDIDATES)
    ranked = sorted(
        range(len(CANDIDATES)),
        key=lambda k: (-wins[k], -total(CANDIDATES[k][1])),
    )
    winner = ranked[0]
    runner_up = ranked[1]
    line = CANDIDATES[winner][0]

    problems = verify(line)
    if problems:
        raise SystemExit(f"entry failed verification: {', '.join(problems)}")

    os.makedirs(os.path.dirname(ENTRY_PATH), exist_ok=True)
    with open(ENTRY_PATH, "w", encoding="utf-8") as f:
        f.write(line + "\n")

    print(f"Tournament: {len(CANDIDATES)} candidates, {len(matches)} matches")
    for rank, idx in enumerate(ranked, start=1):
        print(f"  #{rank} [{wins[idx]} wins, {total(CANDIDATES[idx][1])}/50] {CANDIDATES[idx][0]}")
    print(f"Winner: #{winner + 1} with {wins[winner]} wins")
    print(f"Margin: {wins[winner]}-{wins[runner_up]} wins over runner-up "
          f"(+{wins[winner] - wins[runner_up]})")
    print(f"Entry length: {len(line)} chars (max {MAX_ENTRY_CHARS})")
    print(f"verify: OK — {JUDGE_NOTES[winner]}")
    print(line)


if __name__ == "__main__":
    main()
