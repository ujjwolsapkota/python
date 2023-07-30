
import requests

def from_url(url):
    try:
        response=requests.get(url)
        response.raise_for_status()

        print("Content of URl")
        print(response.text)

    except requests.exceptions.RequestException as e:
        print('Error accessing the URL',e)



from_url('https://www.facebook.com')