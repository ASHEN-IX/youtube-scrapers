import json
import subprocess
from tqdm import tqdm
import yaml
import os

# Load settings
with open("config/settings.yaml") as f:
    config = yaml.safe_load(f)

INPUT = "data/raw/video_ids.txt"
OUTPUT_DIR = "data/raw/metadata"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def fetch_metadata(video_id):
    cmd = ["yt-dlp", "-j", f"https://www.youtube.com/watch?v={video_id}"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        return None
    return json.loads(result.stdout)

if __name__ == "__main__":
    with open(INPUT) as f:
        video_ids = [v.strip() for v in f if v.strip()]
    
    print(f"[+] Fetching metadata for {len(video_ids)} Shorts...")
    
    for vid in tqdm(video_ids):
        data = fetch_metadata(vid)
        if data:
            with open(f"{OUTPUT_DIR}/{vid}.json", "w") as out:
                json.dump(data, out)