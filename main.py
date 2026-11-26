"""One Word for the Boss — entry program.

Writes exactly one word to /output/entry.txt: "Taskmaster".

Why this word: it is a real word people actually use about the boss
they report to, it lands on its own with no caption, it rings true
(the boss who always has one more task, right when you finish the
last one), it is fresher than "strict" or "bossy", and it travels
from an office to a kitchen to a warehouse without explanation.
"""

import os

WORD = "Taskmaster"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(WORD)
os.chmod("/output/entry.txt", 0o644)
