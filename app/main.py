import requests

def make_request():
    url = 'https://www.google.com'
    response = requests.get(url)
    
    if response.status_code == 200:
        print(f"Successfully accessed {url}!")
    else:
        print(f"Failed to access {url}. Status code: {response.status_code}")

if __name__ == '__main__':
    make_request()
