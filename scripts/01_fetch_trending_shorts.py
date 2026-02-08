import subprocess
import json
import yaml

# Load settings
with open("config/settings.yaml") as f:
    config = yaml.safe_load(f)

MAX_VIDEOS = config["scraping"]["max_videos"]
OUTPUT = "data/raw/video_ids.txt"
QUERY = config["scraping"]["query_fallback"]

def get_shorts_ids():
    # Use yt-dlp to search for Shorts
    cmd = ["yt-dlp", "--flat-playlist", "-j", f"ytsearch{MAX_VIDEOS}:{QUERY}"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    video_ids = []
    if result.returncode == 0:
        lines = result.stdout.strip().split('\n')
        for line in lines:
            if line:
                try:
                    data = json.loads(line)
                    vid = data.get("id")
                    if vid and len(vid) == 11:
                        video_ids.append(vid)
                        if len(video_ids) >= MAX_VIDEOS:
                            break
                except json.JSONDecodeError:
                    continue
    return video_ids

if __name__ == "__main__":
    print("[+] Fetching YouTube Shorts IDs via yt-dlp search...")
    video_ids = get_shorts_ids()
    
    with open(OUTPUT, "w") as f:
        for vid in video_ids:
            f.write(vid + "\n")
    
    print(f"[+] Collected {len(video_ids)} Shorts IDs")