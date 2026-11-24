import os

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
text = "I'm out of the office, photosynthesizing. I'll reply when the sun comes back. Please water me before any meetings."
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(text)
