import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from webshotapi import Client

if __name__ == "__main__":
    try:
        API_TOKEN = os.environ['WEBSHOTAPI_API_KEY']
        client = Client(API_TOKEN)

        result = client.extract('https://www.example.com',{
            'extract_html': True,
            'extract_elements': True,
            'extract_style': 1,
        })

        print(result['status_code']);
        print(result['html'])
        print(result)


    except Exception as e:
        print("Error:")
        print(e)
    #print(result)



