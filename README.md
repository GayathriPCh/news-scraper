# News Scraper

This project scrapes news articles from multiple sources, including Vogue, BBC News, and AP News. It classifies the articles into predefined categories (business, political, fashion, tech, sports, entertainment) using a zero-shot classification model. The articles are then saved as a JSON file.

## Features

- **Scrapes News Sources**: Fetches the latest news articles from multiple sources: Vogue, BBC News, and AP News.
- **Zero-Shot Text Classification**: Categorizes articles into predefined categories (business, political, fashion, tech, sports, entertainment) using a machine learning model.
- **JSON Output**: Saves the collected and categorized articles into a JSON file for easy use and further processing.
- **Automated Workflows**: Uses GitHub workflows to automate the scraping process and ensure the application runs on a schedule.

## Requirements

- Python 3.x
- Required Python Libraries:
  - `requests`
  - `beautifulsoup4`
  - `transformers`
  - `json`
  - `pipeline` (from the `transformers` library)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/news-scraper.git
   cd news-scraper
   ```

2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run the scraper, simply execute the `main.py` script:

```bash
python main.py
```

The program will scrape articles from the following sources:
- **Vogue** (Fashion)
- **BBC News**
- **AP News**

It will categorize each article using a zero-shot classification model and save the results into a `combined_articles.json` file.

## GitHub Workflows
![image](https://github.com/user-attachments/assets/d53c0fc8-67c6-4ed4-b893-945a9cf6d45a)

This repository uses **GitHub workflows** to automate tasks such as running the scrapers on a schedule. These workflows ensure that the scraper runs at regular intervals without manual intervention, providing up-to-date news data.
