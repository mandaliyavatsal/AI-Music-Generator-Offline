import os
from scripts.download_models import is_apple_m1, download_models

def main():
    if is_apple_m1():
        download_models()
    # Add the rest of your application logic here

if __name__ == "__main__":
    main()
