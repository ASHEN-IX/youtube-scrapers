import json
import re
import os
import time
from pathlib import Path
import yaml

# Load settings
with open("config/settings.yaml") as f:
    config = yaml.safe_load(f)

INPUT_DIR = Path("data/raw/metadata")
OUTPUT = "data/processed/cleaned.jsonl"

def clean_text(text):
    if not text:
        return ""
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^\w\s]", "", text)
    return text.strip().lower()

if __name__ == "__main__":
    cleaned_data = []
    
    for file_path in INPUT_DIR.glob("*.json"):
        with open(file_path) as f:
            data = json.load(f)
        
        video_id = data.get("id", "")
        title = data.get("fulltitle", "")
        description = data.get("description", "")
        views = data.get("view_count", 0)
        likes = data.get("like_count", 0)
        comments = data.get("comment_count", 0)
        shares = 0  # YouTube doesn't expose share count
        
        # Calculate post_age_hours
        timestamp = data.get("timestamp", 0)
        current_time = time.time()
        post_age_hours = (current_time - timestamp) / 3600 if timestamp else 0
        
        # Extract hashtags from description
        desc = data.get("description", "")
        hashtags = re.findall(r'#\w+', desc)
        hashtag = ", ".join(hashtags) if hashtags else "trending"
        
        # Extract sound
        music = data.get("music", {}) or data.get("originalSound", {})
        if music:
            sound = music.get("title", "") or music.get("album", "") or music.get("authorName", "") or "original sound"
        else:
            sound = "original sound"
        
        video_url = f"https://www.youtube.com/shorts/{video_id}"
        
        entry = {
            "platform": "YouTube",
            "hashtag": hashtag,
            "video_url": video_url,
            "views": views,
            "likes": likes,
            "comments": comments,
            "shares": shares,
            "post_age_hours": round(post_age_hours, 1),
            "sound": sound,
        }
        
        cleaned_data.append(entry)
    
    with open(OUTPUT, "w") as out:
        for entry in cleaned_data:
            out.write(json.dumps(entry) + "\n")
    
    print(f"[+] Cleaned data for {len(cleaned_data)} videos")