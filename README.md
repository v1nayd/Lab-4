# Scenario 18 — Blackjack vs Dealer

A terminal blackjack game with a deck, player/dealer hands, chips, and multiple rounds.

## Provided files

- `main.py` — entry point.
- `game.py` — round flow, decisions, and chip balance.
- `cards.py` — deck operations and hand scoring.
- `requirements.txt` — dependency declaration.

## Setup

```bash
python main.py
```

## Before changing the code

Inspect the hand-value function and manually reason through hands containing one and
multiple Aces. Reproduce incorrect totals before changing it.

## Task 1 — Correct Ace scoring

Implement blackjack hand scoring so an Ace is counted as 11 when that does not bust the
hand and as 1 when necessary.

**Done when:** hands such as A+9, A+9+5, and A+A+9 receive correct totals.

## Task 2 — Complete round resolution

Handle natural blackjack, player bust, dealer bust, dealer drawing rules, and pushes
consistently. Prevent actions after a round has already ended.

## Task 3 — Multi-round bankroll

Make chips persist across rounds and add a simple wager mechanism with validation.
A round must settle exactly once.

## Task 4 — Action feedback and robustness

Add concise feedback for actual card draws and round outcomes. Invalid commands and
invalid wagers must not change the bankroll.

## Required testing

Test one/multiple Aces, blackjack, busts, dealer draws, pushes, wagers, repeated
commands, invalid wagers, empty/depleted deck handling, and quitting.


## LLM usage

You may use an LLM during the lab. The goal is to use it as a coding assistant while
retaining responsibility for understanding and testing the result.

- Inspect the existing code before asking for changes.
- Ask for explanations when you do not understand a proposed change.
- Test generated code against the stated behaviour and edge cases.
- Keep your complete LLM chat history for submission.
- Do not replace the whole project with an unrelated implementation.
- Keep all state in memory; do not add CSV, JSON, SQLite, or other persistence.

## Submission checklist

- [ ] Task 1 completed and the original defect was reproduced and fixed.
- [ ] Tasks 2–4 completed and tested.
- [ ] Boundary and invalid-input cases tested.
- [ ] No unnecessary external dependencies added.
- [ ] No persistent storage added.
- [ ] Code remains understandable and modular.
- [ ] Complete LLM chat-history link included.

## Folder structure

```text
scenario-06-blackjack/
├── README.md
├── requirements.txt
├── main.py
├── game.py
└── cards.py
```

## Submission Checklist

Submission is only the following three things:

- [ ] A 10-second video of gameplay **before** your changes, showing the bug/broken behavior
- [ ] A 10-second video of gameplay **after** your changes, showing the bug fixed and the new features working
- [ ] The Chat/LLM used page link, with the complete chat history

---

## Lab 4 Notes: Blackjack (Vibe Coding)

Run the game with `python main.py`. No extra packages are needed, and nothing is saved to files.

### Errors found in the original code

| # | Error | Where |
|---|-------|-------|
| 1 | Every Ace counted as 11 and never dropped to 1. A+9+5 showed 25 (should be 15), A+A showed 22 (should be 12), so players busted wrongly. | `cards.py` |
| 2 | A bust ended the round before any chips changed, so busting cost nothing. | `game.py` |
| 3 | No natural blackjack (Ace + 10-value card) handling. Any 21 was treated the same. | `game.py` |
| 4 | The bet was fixed at 10 chips. There was no wager prompt and no checking. | `game.py` |
| 5 | Dealer cards were drawn silently, and wrong commands were ignored with no message. | `game.py` |
| 6 | An empty deck made `draw()` return `None`, which could crash the game. | `cards.py`, `game.py` |
| 7 | The game stopped silently when chips reached 0. | `game.py` |

### Fixes, one commit per task

- **Task 1 (Ace scoring):** Aces start as 11. While the total is over 21, one Ace at a time is changed to 1. Only `hand_value` was changed.
- **Task 2 (round results):** Added natural blackjack checks (player only wins, dealer only wins, both is a push). A bust now loses. The dealer draws until 17 or more, and a dealer bust is a player win. Otherwise the higher total wins and equal totals push. One `settle` method changes the chips, so each round is settled exactly once. Every ending returns, so no action is possible after a round ends.
- **Task 3 (chips and wagers):** The game asks for a wager each round (whole number, more than 0, no more than the chips, or `q` to quit). Wins and losses use the wager, and a push changes nothing. Chips carry over between rounds. Quitting mid-round does not change chips. At 0 chips it prints "Out of chips. Game over."
- **Task 4 (feedback and safety):** Prints each card drawn ("Player draws: 5S", "Dealer draws: 3S"). The result shows the amount and the new chips ("Player wins 20. Chips: 120."). Invalid commands and invalid wagers print a clear message and do not change chips. If the deck runs out, the round ends as a push without crashing.

### How it was tested

- **Ace check:** a one-line command scores A+9+5 and A+A. It printed `25 22` before the fix and `15 12` after.
- **Fixed-card tests:** the deck and `input` were replaced with fixed values, so each case can be forced: win, loss, push, natural blackjack (player, dealer, both), player bust, dealer bust, invalid wagers (`abc`, `0`, `-5`, too large, blank), invalid commands, quit mid-round, all-in loss with game over, two rounds in a row, and an empty deck.
- **Repeatable demo:** `random.seed(37)` always deals `6S AH`, then a hit of `5S`. The old code busted at 22, and the fixed code shows 12. This hand is used in both videos.

### Other information

- **Design choices:** natural blackjack pays 1:1 (not 3:2). The dealer stands on every 17, including soft 17. An empty deck ends the round as a push.
- **LLM issues:** some test commands from the LLM failed. One used `.__next__`, which cannot take the prompt text passed to `input()`. Another used quote escapes that PowerShell does not accept. Each was fixed by sending the exact error back to the LLM.
- **Files:** only `cards.py` and `game.py` were changed. `main.py` and `requirements.txt` are unchanged.
- **Deliverables:** one video in `videos/` shows the "before" run (wrong Ace scores) followed by the "after" run (fixed game). The full chat history is included as a PDF.

### Chat history link

https://chatgpt.com/share/6ac160a9-edc4-83ec-a9d2-d785b0996592