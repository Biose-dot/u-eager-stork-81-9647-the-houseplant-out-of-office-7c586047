import os

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)
entry = "Out of office: I am busy turning sunlight into leaves. For urgent matters, talk to the cactus. - Fern"
with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(entry)
