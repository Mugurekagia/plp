import os
import requests
from urllib.parse import urlparse
import sys

def fetch_image():
    url = input("Enter the image URL: ").strip()
    
    save_dir = "Fetched_Images"
    os.makedirs(save_dir, exist_ok=True)
    
    try:
        response = requests.get(url, stream=True, timeout=10)
        response.raise_for_status()
        
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)
        
        if not filename:
            filename = "downloaded_image.jpg"
            
        filepath = os.path.join(save_dir, filename)
        
        with open(filepath, "wb") as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        print(f"Image saved successfully at: {filepath}")
        
    except requests.exceptions.MissingSchema:
        print("Invalid URL. Pease include http:// or https://")
    except requests.exceptions.ConnectionError:
        print("Connection failed. Please check your internet connection")
    except requests.exceptions.Timeout:
        print("Request timed out. Try again later.")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error occured: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)
        
if __name__ == "__main__":
    fetch_image()
        
        