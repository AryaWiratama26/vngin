# Tiktok Scraper

## How to use

1. Clone This Repository
```bash
git clone https://github.com/AryaWiratama26/vngin.git
```

2. Install Requirements
```bash
pip install -r requirements.txt
```

3. Code
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

4. Run
```bash
python bot.py
``` 



## Output

```csv
account_names,likes,comments,captions,video_links
```
[Example CSV](/kaciw.csv)
