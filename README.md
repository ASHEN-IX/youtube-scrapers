# YouTube Shorts Scraper

A Python project to scrape trending YouTube Shorts by domain (e.g., sports, tech), collect metadata, clean the data, and output an ML-ready dataset.

## Features

- Scrapes viral YouTube Shorts by specified domain
- Filters videos for relevance based on keywords
- Filters for viral videos based on high likes and views
- Fetches video metadata including descriptions, likes, comments, and hashtags
- Cleans and filters data
- Merges everything into a JSONL dataset for machine learning

## Requirements

- Python 3.12+
- Dependencies: `pip install -r requirements.txt`
- Docker and Docker Compose (for automation with n8n)

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
3. Clean data
4. Merge dataset

## Automation with n8n and Docker

To automate the scraping process using n8n workflows:

1. Ensure Docker and Docker Compose are installed.

2. Build the scraper image and start the services:
   ```bash
   docker-compose up --build -d
   ```

3. Access n8n at http://localhost:5678 (username: user, password: password)

4. Create a new workflow in n8n:
   - Add a **Schedule Trigger** node to run periodically (e.g., daily).
   - Add an **Execute Command** node with the following command:
     ```
     cd /path/to/your/youtube_scraper && docker-compose run --rm scraper
     ```
     Replace `/path/to/your/youtube_scraper` with the absolute path to your project directory.

5. Save and activate the workflow.

This will run the scraper automatically at the scheduled times.

## Configuration

Edit `config/settings.yaml` to adjust:
- Domain to scrape (e.g., "technology", "sports")
- Keywords for filtering relevant videos
- Minimum likes and views for viral videos
- Max videos to scrape
- User agents
- Delays
- Fallback options

## Output

The final dataset is saved in `data/processed/merged.jsonl` with fields:
- platform
- title
- description
- hashtags (list)
- links (list of URLs from description)
- video_url
- views
- likes
- comments
- shares
- post_age_hours
- sound

## Notes

- Avoids official YouTube API, uses yt-dlp for robustness
- Includes anti-bot measures with delays and user agents
- Cross-platform compatible
- Logs failures in `data/logs/failed.log`