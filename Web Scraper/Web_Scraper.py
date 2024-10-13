
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
    
    # Example: Extract titles (adjust this to the website structure)
    titles = soup.find_all('h2')  # Modify based on the website structure

    # Collect data
    data = []
    for title in titles:
        data.append(title.get_text())

    # Save to CSV
    df = pd.DataFrame(data, columns=['Title'])
    df.to_csv(output_file, index=False)
    print(f"Data scraped and saved to {output_file}")
