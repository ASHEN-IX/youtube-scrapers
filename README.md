# YouTube Shorts Scraper

A Python project to scrape trending YouTube Shorts, collect metadata, comments, and captions, clean the data, and output an ML-ready dataset.

## Features

- Scrapes trending YouTube Shorts automatically
- Fetches video metadata, comments, and auto-generated captions
- Cleans and filters English text data
- Merges everything into a JSONL dataset for machine learning

## Requirements

- Python 3.12+
- Dependencies: `pip install -r requirements.txt`

## Installation

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`

## Usage

Run the main script to execute the full pipeline:

```bash
python main.py
```

This will run all scripts in order:
1. Fetch trending Shorts IDs
2. Fetch metadata
3. Fetch comments
4. Fetch captions
5. Clean data
6. Merge dataset

## Configuration

Edit `config/settings.yaml` to adjust:
- Max videos to scrape
- User agents
- Delays
- Fallback options

## Output

The final dataset is saved in `data/processed/merged.jsonl` with fields:
- video_id
- title
- description
- views
- duration
- comments (list)
- captions (text)

## Notes

- Avoids official YouTube API, uses yt-dlp for robustness
- Includes anti-bot measures with delays and user agents
- Cross-platform compatible
- Logs failures in `data/logs/failed.log`