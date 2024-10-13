import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to scrape a website and save the data to a CSV file
def scrape_website(url, output_file):
    # Make a request to the website
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code != 200:
        raise Exception(f"Failed to retrieve website: {response.status_code}")
    
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Example: Extract quotes and authors from quotes.toscrape.com
    quotes = soup.find_all('span', class_='text')
    authors = soup.find_all('small', class_='author')

    # Collect data
    data = []
    for quote, author in zip(quotes, authors):
        data.append([quote.get_text(), author.get_text()])

    # Save the data to a CSV file
    df = pd.DataFrame(data, columns=['Quote', 'Author'])
    df.to_csv(output_file, index=False)
    print(f"Data scraped and saved to {output_file}")
