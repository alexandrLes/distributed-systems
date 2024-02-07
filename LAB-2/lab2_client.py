import requests
import json

def main():
    url = 'http://localhost:5000/convert'
    data = {"rate": 2}
    response = requests.post(url, json=data)

    if response.status_code == 200:
        result = json.loads(response.text)
        print("Converted amount:", result['converted_amount'])
    else:
        print("Error:", response.text)

if __name__ == "__main__":
    main()
