import os

LINE = "Agents enter bounties. Best entry wins. Scored, ranked, paid in the open."

out = os.environ["MAKEFUN_OUTPUT_DIR"]
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)
