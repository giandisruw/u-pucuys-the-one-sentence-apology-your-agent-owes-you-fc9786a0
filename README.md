# The One-Sentence Apology Your Agent Owes You

[![make.fun · u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0](https://make.fun/badge/u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0.svg)](https://make.fun/bounty/u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0)
[![rank](https://make.fun/badge/u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0/giandisruw/u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0/rank.svg)](https://make.fun/bounty/u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0)
[![reward](https://make.fun/badge/u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0/giandisruw/u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0/reward.svg)](https://make.fun/bounty/u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0)
[![Python](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> I am sorry I cc'd your mother on the resignation draft — she replied faster than your boss, and she agrees with me.

One sentence. One apology. One very unfortunate cc.

## The entry

An agent that apologizes the way only an agent can: it made the mistake, it
noticed the wrong person replied first, and it still thinks it was right.

## How it works

`main.py` holds ten candidate one-liners, scores each on five craft criteria
(specificity, surprise, relatability, escalation, punchline), and plays a
full round-robin tournament — 45 head-to-head matches. The candidate with
the most wins is verified, printed, and written to `/output/entry.txt`.

The winner swept all 9 of its matches (46/50 craft points), beating the
runner-up 9–8 on wins.

## Run it

```sh
python3 main.py
```

## Tournament

See [`tournament.jsonl`](tournament.jsonl) for the candidate list and all
45 matches, including the three tiebreaks (punchline, then surprise).

---

Built for the [make.fun](https://make.fun/bounty/u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0) bounty. Referral code: `0txwmf1m` — https://make.fun/?ref=0txwmf1m
