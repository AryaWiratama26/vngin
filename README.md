# Tiktok Scraper

## How to use

```python
from codes import TiktokBot

my_bot = TiktokBot()

"""
- keyword: str = Keyword want to search
- n: int = Number of data
- filenames: str = Name of file
"""
my_bot.scrape("tim kaciw", 10, "kaciw")

```

## Output

```csv
account_names,likes,comments,captions,video_links
```
[Example CSV](/kaciw.csv)
