import json
import shutil
import yaml

# Load settings
with open("config/settings.yaml") as f:
    config = yaml.safe_load(f)

INPUT = "data/processed/cleaned.jsonl"
OUTPUT = "data/processed/merged.jsonl"

if __name__ == "__main__":
    # Since the cleaned data is already in the final format, just copy it
    shutil.copy(INPUT, OUTPUT)
    print("[+] Merged dataset created")