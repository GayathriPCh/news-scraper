import requests
import json
from bs4 import BeautifulSoup
from transformers import pipeline

# Initialize text classification model
classifier = pipeline('zero-shot-classification')

# Define categories for classification
categories = ["business", "political", "fashion", "tech", "sports", "entertainment"]

# Function to categorize text
def categorize_text(text):
    result = classifier(text, categories)
    return result['labels'][0]

# Function to scrape Vogue
def scrape_vogue():
    url = "https://www.vogue.com/fashion"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    articles = []

    for item in soup.find_all('div', class_='SummaryItemWrapper-iwvBff'):
        headline_tag = item.find('h3')
        link_tag = item.find('a')
        author_tag = item.find('p', class_='Byline-iwvBff')
        image_tag = item.find('img')

        headline = headline_tag.get_text() if headline_tag else 'No headline available'
        link = link_tag['href'] if link_tag else 'No link available'
        author = author_tag.get_text() if author_tag else 'Unknown author'
        image = image_tag['src'] if image_tag else 'No image available'

        article = {
            'headline': headline,
            'link': link,
            'author': author,
            'image': image,
            'category': 'fashion',
            'source': 'Vogue'
        }
        
        articles.append(article)

    return articles

# Function to scrape BBC News
def scrape_bbc_news():
    url = 'https://www.bbc.com/news/'
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, 'html.parser')
    script_tag = soup.find('script', id='__NEXT_DATA__')

    bbc_news = []
    if script_tag:
        json_data = json.loads(script_tag.string)
        try:
            sections = json_data['props']['pageProps']['page']['@\"news\",']['sections']
            for section in sections:
                for content in section['content']:
                    article = {
                        'headline': content['title'],
                        'link': content['href'],
                        'description': content['description'],
                        'image': content.get('image', {}).get('model', {}).get('blocks', {}).get('src'),
                        'category': categorize_text(content['title']),
                        'source': 'BBC'
                    }
                    bbc_news.append(article)
        except KeyError as e:
            print(f"KeyError: {e} - Please check the JSON structure.")

    return bbc_news

# Function to scrape AP News
def scrape_ap_news():
    url = 'https://apnews.com/'
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.find_all('div', class_='PagePromo')

    ap_news = []
    for article in articles:
        headline = article.find('h3', class_='PagePromo-title')
        link = article.find('a', class_='Link')['href']
        description = article.find('div', class_='PagePromo-description')

        img_tag = article.find('img', class_='Image')
        if img_tag and img_tag.has_attr('srcset'):
            image = img_tag['srcset'].split(',')[0].split(' ')[0]
        else:
            image = None

        ap_article = {
            'headline': headline.get_text(strip=True) if headline else None,
            'link': link,
            'description': description.get_text(strip=True) if description else None,
            'image': image,
            'category': categorize_text(headline.get_text(strip=True)) if headline else 'Unknown',
            'source': 'AP News'
        }

        ap_news.append(ap_article)

    return ap_news

# Main function to combine all scrapers and save to JSON
def main():
    vogue_articles = scrape_vogue()
    bbc_articles = scrape_bbc_news()
    ap_articles = scrape_ap_news()

    all_articles = vogue_articles + bbc_articles + ap_articles

    with open('combined_articles.json', 'w') as json_file:
        json.dump(all_articles, json_file, indent=4)

    print("Data saved to combined_articles.json")

if __name__ == "__main__":
    main()
