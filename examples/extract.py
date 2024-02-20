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
            'extract_selectors': True,
            'extract_style': 1,
            'no_cache': True
        })

        print(result.save('/tmp/test_extract.json'))


    except Exception as e:
        print("Error:")
        print(e)
    #print(result)



