import os
import platform
import urllib.request

def is_apple_m1():
    return platform.machine() == "arm64" and platform.system() == "Darwin"

def download_model(url, dest):
    if not os.path.exists(dest):
        print(f"Downloading model from {url} to {dest}...")
        urllib.request.urlretrieve(url, dest)
        print("Download complete.")
    else:
        print(f"Model already exists at {dest}.")

def download_models():
    model_urls = [
        "https://example.com/model1",
        "https://example.com/model2"
    ]
    model_destinations = [
        "models/model1",
        "models/model2"
    ]

    for url, dest in zip(model_urls, model_destinations):
        download_model(url, dest)

if __name__ == "__main__":
    if is_apple_m1():
        download_models()
