# StudySprint

A small flashcard and quiz trainer you run in the terminal. Load a deck of cards
from a JSON file, quiz yourself, and see your score at the end. This is your
squad's starting product for Elite 101 - you'll grow it one ticket at a time.

## Run it
## What's new in v1.0

- **Mark cards as known:** flag flashcards you've mastered so you can focus on the ones you haven't.
- **Review missed cards:** a `review_missed` helper lets you go back over the questions you got wrong.
- **Accurate scoring:** fixed the score counting and percent calculation so results match your answers.
- **Bug fixes:** corrected typos in the `category` and `top_card` functions.
- **Better tests and docs:** added unit tests for `average_score` and documented `check_answer`.
```bash
python main.py
```

## Run the tests

```bash
python -m unittest
```

## How it's laid out

| File | What it does |
|---|---|
| `main.py` | The menu loop you interact with |
| `storage.py` | Loads and saves the JSON data file |
| `features/core.py` | The deck, the quiz loop, and small helpers |
| `features/reports.py` | Summary reports (half-built - finish it via a ticket) |
| `data/studysprint.json` | The card deck and score history |
| `tests/test_core.py` | Example tests to copy from |

## Team

-Lakshitha Vengadeswaran

## Where to start

Pick a ticket from the `tickets/` folder (or the Issues tab once your section
repo exists). Read `CONTRIBUTING.md` for the Definition of Done every pull
request has to meet.
