from ebooklib import epub, ITEM_DOCUMENT
from bs4 import BeautifulSoup
import re


def clean_html_tags(text):
    # Use BeautifulSoup to clean HTML tags and attributes
    soup = BeautifulSoup(text, 'html.parser')
    cleaned_text = soup.get_text(separator='\n', strip=True)
    return cleaned_text


def read_epub(epub_file):
    book = epub.read_epub(epub_file)
    
    text = []
    for item in book.get_items():
        if item.get_type() == ITEM_DOCUMENT:
            raw_html = item.get_body_content().decode('utf-8')
            cleaned_html = clean_html_tags(raw_html)
            text.append(cleaned_html)
    
    # Join all text content into a single string
    full_text = '\n'.join(text)
    
    # Optionally, remove extra spaces and newlines
    full_text = re.sub(r'\n+', '\n', full_text)  # Remove multiple newlines
    full_text = re.sub(r'\s+', ' ', full_text)  # Replace multiple spaces with a single space
    
    return full_text
    
