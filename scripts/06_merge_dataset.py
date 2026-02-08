import json
import shutil
import yaml
import csv

# Load settings
with open("config/settings.yaml") as f:
    config = yaml.safe_load(f)

INPUT = "data/processed/cleaned.jsonl"
OUTPUT = "data/processed/merged.csv"

if __name__ == "__main__":
    # Convert JSONL to CSV
    with open(INPUT, 'r') as infile, open(OUTPUT, 'w', newline='') as outfile:
        writer = None
        for line in infile:
            data = json.loads(line.strip())
            if writer is None:
                writer = csv.DictWriter(outfile, fieldnames=data.keys())
                writer.writeheader()
            writer.writerow(data)
    print("[+] Merged dataset created as CSV")