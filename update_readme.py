import feedparser

somjang_blog_rss_url = "https://DagyeongH.github.io/feed.xml"
rss_feed = feedparser.parse(somjang_blog_rss_url)

MAX_POST_NUM = 10

latest_blog_post_list = ""

MAX_POST_NUM = 10

for idx, feed in enumerate(rss_feed['entries']):
    if idx > MAX_POST_NUM:
        break
    feed_date = feed['published_parsed']
    latest_blog_post_list += f"[{feed_date.tm_year}.{feed_date.tm_mon}.{feed_date.tm_mday} - {feed['title']}]({feed['link']}) <br>\n"
    
markdown_text = """
###  :wave: Welcome my github profile :wave:  
  
![header](https://capsule-render.vercel.app/api?type=cylinder&color=7193bd&height=150&section=header&text=DagyeongH&fontColor=ffffff&fontSize=70&animation=fadeIn&fontAlignY=55&desc=%20&descAlignY=62&descAlign=62)

####  🔨 Once I've used 🔨
<a href="링크"><img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white"/></a>
<a href="링크"><img src="https://img.shields.io/badge/pandas-150458?style=flat-square&logo=pandas&logoColor=white"/></a>
<a href="링크"><img src="https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=NumPy&logoColor=white"/></a>
<a href="링크"><img src="https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white"/></a>
<a href="링크"><img src="https://img.shields.io/badge/jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white"/></a>


#### 📓 My log 📓
"""

readme_text = f"{markdown_text}{latest_blog_post_list}"

with open("README.md", 'w', encoding='utf-8') as f:
    f.write(readme_text)
