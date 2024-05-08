# url_shortener.py

import hashlib

url_mapping = {}  # Dictionary to store mappings between short URLs and original URLs

# Function to generate a short URL for a given long URL
def shorten_url(url):
    hash_code = hashlib.md5(url.encode()).hexdigest()[:6]  # Generating hash code from URL
    short_url = f"short.url/{hash_code}"  # Constructing short URL
    url_mapping[short_url] = url  # Storing mapping between short URL and original URL
    return short_url

# Function to retrieve the original URL for a given short URL
def retrieve_url(short_url):
    return url_mapping.get(short_url, "URL not found.")

# Main function to manage the application flow
def main():
    while True:
        print("\n1. Shorten URL")
        print("2. Retrieve URL")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            original_url = input("Enter the URL to shorten: ")
            short_url = shorten_url(original_url)
            print(f"Shortened URL: {short_url}")
        elif choice == "2":
            short_url = input("Enter the shortened URL: ")
            original_url = retrieve_url(short_url)
            print(f"Original URL: {original_url}")
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()
