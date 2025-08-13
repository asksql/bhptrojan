import requests
import base64

GITHUB_API_URL = "https://api.github.com/repos/asksql/bhptrojan/contents/data/abc"
RAW_BASE_URL = "https://raw.githubusercontent.com/asksql/bhptrojan/main/data/abc/"

def read_and_print_github_txt_files():
    response = requests.get(GITHUB_API_URL)
    response.raise_for_status()
    files = response.json()
    for file in files:
        #if file['name'].endswith('.txt'):
        print(f"--- {file['name']} ---")
        raw_url = RAW_BASE_URL + file['name']
        print("raw_url: ", raw_url)
        file_resp = requests.get(raw_url)
        file_resp.raise_for_status()
        print(base64.b64decode(file_resp.text))
        print()

if __name__ == "__main__":
    read_and_print_github_txt_files()