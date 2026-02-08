import subprocess
import sys

SCRIPTS = [
    "scripts/01_collect_video_ids.py",
    "scripts/02_fetch_metadata.py",
    "scripts/03_fetch_comments.py",
    "scripts/04_fetch_captions.py",
    "scripts/05_clean_text.py",
    "scripts/06_merge_dataset.py",
]

def run(script):
    print(f"\n▶ Running {script}")
    result = subprocess.run(
        ["python", script],
        stdout=sys.stdout,
        stderr=sys.stderr
    )
    if result.returncode != 0:
        print(f"\n❌ Failed at {script}")
        sys.exit(1)
    print(f"✅ Finished {script}")

if __name__ == "__main__":
    print("🚀 Starting YouTube scraping pipeline")
    for script in SCRIPTS:
        run(script)
    print("\n🎉 Pipeline completed successfully!")
