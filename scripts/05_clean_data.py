import json
import os
import yaml

# Load settings
with open("config/settings.yaml") as f:
    config = yaml.safe_load(f)

INPUT_DIR = "data/raw/metadata"
OUTPUT = "data/processed/cleaned.jsonl"

if __name__ == "__main__":
    with open(OUTPUT, "w") as out:
        for file in os.listdir(INPUT_DIR):
            if file.endswith(".json"):
                with open(os.path.join(INPUT_DIR, file)) as f:
                    data = json.load(f)
                    # Extract relevant fields
                    cleaned = {
                        "platform": "YouTube",
                        "title": data.get("title", ""),
                        "description": data.get("description", ""),
                        "hashtags": [],  # Not available in yt-dlp
                        "links": [],  # Not available
                        "video_url": data.get("webpage_url", ""),
                        "views": data.get("view_count", 0),
                        "likes": data.get("like_count", 0),
                        "comments": data.get("comment_count", 0),
                        "shares": 0,  # Not available
                        "post_age_hours": 0,  # Calculate if needed
                        "sound": "original sound"  # Assume
                    }
                    out.write(json.dumps(cleaned) + "\n")
    print("[+] Cleaned data created")