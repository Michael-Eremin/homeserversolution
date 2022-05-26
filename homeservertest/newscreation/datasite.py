
from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
from dateutil.parser import parse



# News source:
BIOLOGY = 'https://scitechdaily.com/news/biology/'
PHYSICS = 'https://blogs.cardiff.ac.uk/physicsoutreach/'
MATH = 'https://news.mit.edu/topic/mathematics/'


# Type alias for variables
url = str
path = str


def get_source(content_link: url) -> url:
    """Retrieving a resource from a link."""
    source = content_link.split('/')[2]
    return source


def convert_to_path(url: url, cat: str) -> path:
    """The image link is converted into a save path for the Models field format."""
    str_url = str(url)
    ext_img = ['.jpg', '.png', '.gif', '.tif', '.JPG', '.PNG', '.GIF', '.TIF', '.bmp', '.BMP']
    for i in range(0, len(ext_img)):
        if ext_img[i] in str_url:
            end_str = str_url.split(ext_img[i], 1)[0]
            body_link = end_str.rsplit('/', 1)[-1]
            list_path = ['images/'] + [body_link] + ['_'] + [cat] + [ext_img[i]]
            path = ''.join(list_path)
            return path


def save_image(url: url, image_path: path):
    """Saving a image to a specified path local server."""
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 YaBrowser/19.10.2.195 Yowser/2.5 Safari/537.36'}
    image = requests.get(url, headers=headers).content
    # Specify the path on the local server
    path_local = '/home/michael/code/homeserversolution/homeservertest/media/' 
    path_image = path_local + image_path
    with open(path_image, 'wb') as f:
        f.write(image)


def make_format_date(date_text: str) -> str:
    """Converts the date string to a uniform format for the field in Models."""
    date_parse = parse(date_text)
    date_format = date_parse.strftime('%Y-%m-%d')
    return date_format


def get_math_news() -> list[dict[str, str]]:
    """Gets data from a web resource."""
    math_news = []
    rtext = requests.get(MATH).text
    soup = BeautifulSoup(rtext, "lxml")
    
    # with open('/home/michael/code/scienceworldnews/scienceworldnews/news/templates/news/example_m.html') as fp:
    #     soup = BeautifulSoup(fp, "lxml")

    posts = soup.find_all("div", class_="page-term--views--list-item")
    for post in posts:
       
        date_text = post.find("time").get_text().strip()
        date_published = make_format_date(date_text)    
        title = post.find("a", class_="term-page--news-article--item--title--link").get_text().strip()
        description = post.find("p", class_="term-page--news-article--item--dek").get_text().strip()
        content_link = 'https://news.mit.edu' + post.find("a", class_="term-page--news-article--item--title--link").get("href")
        img_link = 'https://news.mit.edu' + post.find("div", class_="term-page--news-article--item--cover-image").a.img.get("data-src")
        img_path = convert_to_path(img_link, 'math')
        save_image(img_link, img_path)
        source = get_source(content_link)

        data = {'title': title,
                'description': description,
                'content_link': content_link,
                'date_published': date_published,
                'img_link': img_link,
                'img_path': img_path,
                'source': source,
                'cat_id': '1'
                }
        math_news.append(data)
    return math_news


def get_physics_news() -> list[dict[str, str]]:
    """Gets data from a web resource."""
    physics_news = []
    rtext = requests.get(PHYSICS).text
    soup = BeautifulSoup(rtext, "lxml")

    # with open('/home/michael/code/scienceworldnews/scienceworldnews/news/templates/news/example_p.html') as fp:
    #     soup = BeautifulSoup(fp, "lxml")

    posts = soup.find_all("article", "with-image")
    for post in posts:
       
        date_text = post.find("p", class_="teaser-date posted-on").a.get_text().strip()
        date_published = make_format_date(date_text)
        title = post.find("h1", class_="teaser-title").a.get_text().strip()
        description = post.find("div", class_="teaser-body").find_all("p")[1].contents[0].get_text().strip()
        content_link = post.find("div", class_="teaser-body").a.get("href")
        img_link = post.find("figure", class_="teaser-image").a.img.get("src")
        img_path = convert_to_path(img_link, 'physics')
        save_image(img_link, img_path)
        source = get_source(content_link)

        data = {'title': title,
                'description': description,
                'content_link': content_link,
                'date_published': date_published,
                'img_link': img_link,
                'img_path': img_path,
                'source': source,
                'cat_id': '2'
                }
        physics_news.append(data)
    return physics_news


def get_biology_news() -> list[dict[str, str]]:
    """Gets data from a web resource."""
    biology_news = []
    rtext = requests.get(BIOLOGY).text
    soup = BeautifulSoup(rtext, "lxml")

    # with open('/home/michael/code/homeserversolution/homeservertest/newscreation/templates/newscreation/example_b.html') as fp:
    #     soup = BeautifulSoup(fp, "lxml")

    posts = soup.find_all("article", "content-list")
    for post in posts:
       
        date_text = post.find("span", class_="entry-meta-date updated").get_text().strip()
        date_published = make_format_date(date_text)
        title = post.find("a").get("title").strip()
        description = post.find('div', class_="content-list-excerpt").get_text().strip()
        content_link = post.find("a").get("href")
        img_link = post.find("div", class_="content-thumb content-list-thumb").a.img.get("src")
        img_path = convert_to_path(img_link, 'biology')
        save_image(img_link, img_path)
        source = get_source(content_link)
        
        data = {'title': title,
                'description': description,
                'content_link': content_link,
                'date_published': date_published,
                'img_link': img_link,
                'img_path': img_path,
                'source': source,
                'cat_id': '3'
                }
        biology_news.append(data)
    return biology_news
        
        
def get_list_data() -> list[dict[str, str]]:
    """Starts the data retrieval functions."""
    math_list = get_math_news()
    physics_list = get_physics_news()
    biology_list = get_biology_news()
    news_list = math_list + physics_list + biology_list
    return news_list
    
