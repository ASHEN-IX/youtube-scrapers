import subprocess
from pathlib import Path
import yaml

# Load settings
with open("config/settings.yaml") as f:
    config = yaml.safe_load(f)

INPUT = "data/raw/video_ids.txt"
OUTPUT_DIR = Path("data/raw/captions")
OUTPUT_DIR.mkdir(exist_ok=True)

if __name__ == "__main__":
    with open(INPUT) as f:
        video_ids = [v.strip() for v in f if v.strip()]
    
    print(f"[+] Fetching captions for {len(video_ids)} Shorts...")
    
    for vid in video_ids:
        subprocess.run([
            "yt-dlp",
            "--write-auto-sub",
            "--skip-download",
            "--sub-lang", "en",
            "-o", str(OUTPUT_DIR / f"{vid}"),
            f"https://www.youtube.com/shorts/{vid}"
        ])