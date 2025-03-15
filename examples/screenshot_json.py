import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from webshotapi import Client

if __name__ == "__main__":
    try:

        API_TOKEN = os.environ['WEBSHOTAPI_API_KEY']
        client = Client(API_TOKEN)

        result = client.screenshot_json('https://www.example.com',{
            'remove_modals': True, # Remove cookies popup with AI
        })

        print(result['url'])
        print(result)

    except Exception as e:
        print("Error:")
        print(e)
    #print(result)



