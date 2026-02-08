#!/usr/bin/env python3
"""
YouTube Shorts Scraper - Main Entry Point
Runs all scraping scripts in sequence with error handling and logging.
"""

import subprocess
import time
import random
import os
import yaml
from pathlib import Path

# Load settings
with open("config/settings.yaml") as f:
    config = yaml.safe_load(f)

DELAY_MIN = config["scraping"]["delay"]["min"]
DELAY_MAX = config["scraping"]["delay"]["max"]
LOG_FILE = "data/logs/failed.log"

def ensure_dirs():
    dirs = [
        "data/raw",
        "data/raw/metadata",
        "data/raw/comments",
        "data/raw/captions",
        "data/processed",
        "data/logs"
    ]
    for d in dirs:
        Path(d).mkdir(parents=True, exist_ok=True)

def run_script(script_name):
    print(f"[+] Running {script_name}...")
    try:
        result = subprocess.run(["python3", f"scripts/{script_name}"], check=True)
        print(f"[+] {script_name} completed successfully")
    except subprocess.CalledProcessError as e:
        error_msg = f"Error in {script_name}: {e}"
        print(f"[!] {error_msg}")
        with open(LOG_FILE, "a") as log:
            log.write(error_msg + "\n")
        return False
    return True

def main():
    ensure_dirs()
    
    scripts = [
        "01_fetch_trending_shorts.py",
        "02_fetch_metadata.py",
        "05_clean_data.py",
        "06_merge_dataset.py"
    ]
    
    for script in scripts:
        if not run_script(script):
            print(f"[!] Stopping due to error in {script}")
            break
        # Delay between scripts
        delay = random.uniform(DELAY_MIN, DELAY_MAX)
        print(f"[+] Waiting {delay:.2f} seconds...")
        time.sleep(delay)
    
    print("[+] All scripts executed. Check data/processed/merged.jsonl for results.")

if __name__ == "__main__":
    main()
