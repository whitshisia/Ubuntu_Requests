import os
import requests
from urllib.parse import urlparse
import uuid

def fetch_image():
    # Prompt user for image URL
    url = input("Enter the URL of the image you want to download: ").strip()
    
    if not url:
        print("❌ No URL provided. Exiting.")
        return
    
    # Create directory for storing images
    save_dir = "Fetched_Images"
    os.makedirs(save_dir, exist_ok=True)

    try:
        # Fetch the image
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise error for HTTP codes 4xx/5xx
    except requests.exceptions.RequestException as e:
        print(f"⚠️ Error fetching the image: {e}")
        return

    # Extract filename from URL
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)

    # If no filename found in URL, generate a unique one
    if not filename:
        filename = f"image_{uuid.uuid4().hex}.jpg"

    # Full save path
    save_path = os.path.join(save_dir, filename)

    try:
        # Save image in binary mode
        with open(save_path, "wb") as f:
            f.write(response.content)
        print(f"✅ Image saved successfully at: {save_path}")
    except Exception as e:
        print(f"⚠️ Failed to save the image: {e}")

if __name__ == "__main__":
    fetch_image()
