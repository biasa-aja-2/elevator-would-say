"""What the Elevator Would Say.

The elevator speaks in its own voice about its own job — carrying people and their baggage, literally and emotionally — then turns on the passenger with the universal sin of button-mashing, likened to playing piano. Surprise twist, no pun, fresh angle.
Pure stdlib, no network, no secrets.
"""

import os
import sys

LINE = 'I have carried your secrets, your groceries and your ex — please stop pressing all the buttons like a piano.'


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
    if out_dir.endswith(".txt"):
        path = out_dir
        directory = os.path.dirname(path) or "."
    else:
        directory = out_dir
        path = os.path.join(directory, "entry.txt")
    os.makedirs(directory, exist_ok=True)
    if not (1 <= len(LINE) <= 120):
        sys.exit("gate failed: length %d not in 1..120" % len(LINE))
    if LINE.strip() == "":
        sys.exit("gate failed: line is whitespace-only")
    if "\n" in LINE or "\r" in LINE:
        sys.exit("gate failed: line is not a single line")
    if LINE.count(".") != 1 or not LINE.endswith("."):
        sys.exit("gate failed: not exactly one sentence")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(path, 0o644)
    with open(path, "rb") as f:
        raw = f.read()
    if raw.decode("utf-8") != LINE:
        sys.exit("verification failed: read-back differs from LINE")
    print("wrote %d chars to %s" % (len(LINE), path))


if __name__ == "__main__":
    main()
