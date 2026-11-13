# ai-happy-01 — "Sunflower for You"

Make the AI judge happy: a small round robot offers a big yellow
sunflower to a laughing little girl in a golden-hour park. Warm light,
rolling green hills, butterflies, and two smaller sunflowers framing
the scene.

## How it works

`entry.png` (1024x1024, 166,449 bytes) was drawn procedurally with
Pillow at build time (see `../build/ai-happy-01/` for the drawing code
and the two other variants considered). At grading time `main.py`
(Python 3.13 stdlib only) copies it to `/output/entry.png` — the
simplest entry form the kit explicitly allows. Deterministic: the same
bytes are copied on every run.

## License

MIT — see `LICENSE`.
